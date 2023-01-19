from numpy import shape

class DecisionTree:
    
    def __init__(self, num_feats, max_depth=100):
        self.num_feats = num_feats
        self.max_depth = max_depth
        self.root = None
    
        """
        This function will grow the tree from its root and print the
        tree out
        """
    def __fit__(self, data, target):
        self.root = self.__grow_tree__(data, target)
        self.__print_d_tree__(self.root)
    
    
    
    def __grow_tree__(self, data, target, depth=0):
        num_samples = len(data)
        
    
    
    def __print_d_tree__(self, root):
        pass