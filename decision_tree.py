import numpy as np
from node import Node
from collections import Counter
import math

class DecisionTree:
    
    def __init__(self, num_feats, max_depth, min_sample_split=2):
        self.num_feats = num_feats
        self.max_depth = max_depth
        self.min_sample_split = min_sample_split
        self.root = None
    
    
    """
    This function will grow the tree from its root and print the
    tree out
    """
    def __fit__(self, data, target):
        
        self.root = self.__grow_tree__(data, self.__change_numerical__(target))
        return self.root


    """ 
    This function changes the target column into binary or numerical
    indicators to represent a target option for calculations in entropy
    """
    def __change_numerical__(self, target):
        
        tar_options = np.unique(target)
        new_target = []
        
        assigned_nums = {}
        i = 0
        for options in tar_options:
            assigned_nums[options] = i
            i += 1
        
        for idx in range(0, len(target)):
            label = target[idx]
            new_target.append(assigned_nums[label])
            
        return np.array(new_target)
            
    
    def __grow_tree__(self, data, target, depth=0):
        
        num_samples = np.shape(data)[0]     # number of data entries
        num_options = len(np.unique(target))     # number of options in target column
        
        # check base case --> tree depth, pure node or splitting range less than 2
        if depth >= int(self.max_depth) or num_options == 1 or self.min_sample_split > num_samples:
            return Node(leaf_val=self.__common_label__(target))

        feat_idxs = np.random.choice(len(data[0]), self.num_feats, replace=False)    # change later to getting just the best split from whole numebr of feats
        
        best_feat, best_thres_q = self.__best_split__(feat_idxs, data, target)
        
        left_idxs, right_idxs = self.__child_split__(data[:, best_feat], best_thres_q)
        left = self.__grow_tree__(data[left_idxs, :], target[left_idxs], depth + 1)
        right = self.__grow_tree__(data[right_idxs, :], target[right_idxs], depth + 1)
        
        return Node(feature=best_feat, thres_quant=best_thres_q, left=left, right=right)
        
        
    def __best_split__(self, feat_idxs, data, target):
        
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
        
        parent_entropy = self.__entropy__(target)
        
        # child nodes idxs
        left_branch, right_branch = self.__child_split__(data_col, thres)
        
        left_len, right_len = len(left_branch), len(right_branch)
        entropy_l, entropy_r = self.__entropy__(target[left_branch]), self.__entropy__(target[right_branch])
        child_wa_entropy = (left_len / len(target)) * entropy_l + (right_len / len(target)) * entropy_r
        
        return parent_entropy - child_wa_entropy
        
        
    def __child_split__(self, data_col, thres):
        left = np.argwhere(data_col <= thres).flatten()
        right = np.argwhere(data_col > thres).flatten()
        return left, right
        
        
    def __entropy__(self, target):
        hist = np.bincount(target)
        probs = hist / len(target)
        return -sum([prob * math.log2(prob) for prob in probs if prob > 0])
        
    
    def __print_d_tree__(self, root):
        pass
    
    
    def __common_label__(self, target):
        count = Counter(target)
        return count.most_common(1)[0][0]
        
    
    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        if node.__is_leaf__():
            return node.leaf_val

        if x[node.feature] <= node.thres_quant:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)