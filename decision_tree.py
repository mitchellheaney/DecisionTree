import numpy as np
from collections import Counter
import math
from Helper import __change_numerical__
from Node import Node


class DecisionTree:
    
    def __init__(self, num_feats=None, max_depth=100, min_sample_split=2):
        self.num_feats = num_feats
        self.max_depth = max_depth
        self.min_sample_split = min_sample_split
        self.root = None
    
    
    def __fit__(self, data, target):
        '''
        Fits the given data and target into the model to grow branches
        
        Arguments:
            data (ndarray)      - core data samples
            target (ndarray)    - target data column
            
        Exceptions:
            N/A
            
        Return Value:
            (Node)              - root node of tree 
        '''
        
        self.root = self.__grow_tree__(data, __change_numerical__(target))
        return self.root
            
    
    def __grow_tree__(self, data, target, depth=0):
        '''
        Recursively grows the tree through considering highest info gain and
        increasing depth
        
        Arguments:
            data (ndarray)      - core data samples
            target (ndarray)    - target data column
            depth (int)         - tree depth
            
        Exceptions:
            N/A
            
        Return Value:
            (Node)              - either decision or leaf node
        '''
        
        num_samples = np.shape(data)[0]
        num_options = len(np.unique(target))
        
        # check base case --> tree depth, pure node or splitting range less than 2
        if depth >= int(self.max_depth) or num_options == 1 or self.min_sample_split > num_samples:
            return Node(leaf_val=self.__common_label__(target))

        feat_idxs = np.random.choice(len(data[0]), self.num_feats, 
            replace=False)
        
        best_feat, best_thres_q = self.__best_split__(feat_idxs, data, 
            target)
        
        left_idxs, right_idxs = self.__child_split__(data[:, best_feat], 
            best_thres_q)
        left = self.__grow_tree__(data[left_idxs, :], target[left_idxs], 
            depth + 1)
        right = self.__grow_tree__(data[right_idxs, :], target[right_idxs], 
            depth + 1)
        
        return Node(feature=best_feat, thres_quant=best_thres_q, left=left, 
            right=right)
        
        
    def __best_split__(self, feat_idxs, data, target):
        '''
        This function performs a split in the dataset to return the best split 
        index and the threshold for that feature
        
        Arguments:
            feat_idxs (ndarray) - indexes for features randomly selected
            data (ndarray)      - core data samples
            target (ndarray)    - target data column
            
        Exceptions:
            N/A
            
        Return Value:
            (list)              - best split index and threshold
        '''
        
        highest_gain = 0
        best_idx, best_thres = None, None
        
        for idx in feat_idxs:
            idx_col = data[:, idx]
            thresholds = np.unique(idx_col)
            
            for thr in thresholds:
                gain = self.__info_gain__(idx_col, target, thr)
                
                if gain > highest_gain:
                    highest_gain = gain
                    best_idx = idx
                    best_thres = thr
        
        return best_idx, best_thres


    def __info_gain__(self, data_col, target, thres):
        '''
        Returns the numerical information gain for a feature column
        
        Arguments:
            data_col (ndarray)  - feature column
            target (ndarray)    - target data column
            thres (float)       - tested threshold number
            
        Exceptions:
            N/A
            
        Return Value:
            (float)             - information gain
        '''
        
        parent_entropy = self.__entropy__(target)
        
        # child nodes idxs
        left_branch, right_branch = self.__child_split__(data_col, thres)
        
        left_len, right_len = len(left_branch), len(right_branch)
        entropy_l, entropy_r = self.__entropy__(target[left_branch]), self.__entropy__(target[right_branch])
        child_wa_entropy = (left_len / len(target)) * entropy_l + (right_len / len(target)) * entropy_r
        
        return parent_entropy - child_wa_entropy
        
        
    def __child_split__(self, data_col, thres):
        '''
        Splits the data_col into 2 children sets according to threshold values
        
        Arguments:
            data_col (ndarray)  - feature column
            thres (float)       - tested threshold number
            
        Exceptions:
            N/A
            
        Return Value:
            (list)              - left and right children subsets
        '''
        
        left = np.argwhere(data_col <= thres).flatten()
        right = np.argwhere(data_col > thres).flatten()
        return left, right
        
        
    def __entropy__(self, target):
        '''
        Calculates the numerical entropy or degree of disorder of the target 
        
        Arguments:
            target (ndarray)    - target data column
            
        Exceptions:
            N/A
            
        Return Value:
            (float)             - entropy value
        '''
        
        hist = np.bincount(target)
        probs = hist / len(target)
        return -sum([prob * math.log2(prob) for prob in probs if prob > 0])
        
    
    def __print_d_tree__(self, root):
        '''
        Prints the tree given root in preorder traversal
        
        Arguments:
            root (Node)         - tree root node
            
        Exceptions:
            N/A
            
        Return Value:
            (void)
        '''
        
        self.__recurse_print__(root)
        
        
    def __recurse_print__(self, node, level=0):
        '''
        Prints the tree given root recursively with incrementing depth
        
        Arguments:
            node (Node)         - current node in tree
            level (int)         - depth of the tree
            
        Exceptions:
            N/A
            
        Return Value:
            (void)
        '''
        
        if node.feature is not None:
            print(str("    " * level), node.feature, " ", node.thres_quant)
            self.__recurse_print__(node.left, level + 1)
            self.__recurse_print__(node.right, level + 1)
    
    
    def __predict__(self, X):
        '''
        Uses testing data to predict outcomes of the model
        
        Arguments:
            X (ndarray)         - core data samples
            
        Exceptions:
            N/A
            
        Return Value:
            (ndarray)           - array of string labels for each column 
        '''
        
        return np.array([self.__traverse_tree__(x, self.root) for x in X])


    def __traverse_tree__(self, x, node):
        '''
        Recursively traverses the tree and returns most common target label 
        for leaf nodes once reached
        
        Arguments:
            x (ndarray)         - sample data entry row
            node (Node)         - current node
            
        Exception:
            N/A
            
        Return Value:
            (string)            - leaf value
        '''
        
        if node.__is_leaf__():
            return node.leaf_val

        if x[node.feature] <= node.thres_quant:
            return self.__traverse_tree__(x, node.left)
        return self.__traverse_tree__(x, node.right)
        
    
    def __common_label__(self, target):
        '''
        Counts the highest frequency option in target and returns it
        
        Arguments:
            target (ndarray)    - array of options for target column
            
        Exceptions:
            N/A
            
        Return Value:
            (string)            - most common target option
        '''
        
        count = Counter(target)
        return count.most_common(1)[0][0]