import numpy as np
from node import Node
from collections import Counter

class DecisionTree:
    
    def __init__(self, num_feats, max_depth=100, min_sample_split=2):
        self.num_feats = num_feats
        self.max_depth = max_depth
        self.min_sample_split = min_sample_split
        self.root = None
    
        """
        This function will grow the tree from its root and print the
        tree out
        """
    def __fit__(self, data, target):
        self.root = self.__grow_tree__(data, target)
        #self.__print_d_tree__(self.root)
    
    
    
    def __grow_tree__(self, data, target, depth=0):
        num_samples = np.shape(data)[0]     # number of data entries
        num_options = len(np.unique(target))     # number of options in target column
        
        # check base case --> tree depth, pure node or splitting range less than 2
        if depth >= self.max_depth or num_options == 1 or self.min_sample_split > num_samples:
            return Node(leaf=self.__common_label__(target))

        feat_idxs = np.random.choice(len(data[0]), self.num_feats, replace=False)
        

    
    
    def __print_d_tree__(self, root):
        pass
    
    
    def __common_label__(self, target):
        count = Counter(target)
        return count.most_common(1)[0][0]
        