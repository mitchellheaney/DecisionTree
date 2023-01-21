class Node:
    
    def __init__(self, feature=None, thres_quant=None, left=None, right=None, *, leaf_val=None):
        self.feature = feature
        self.thres_quant = thres_quant
        self.left = left
        self.right = right
        self.leaf_val = leaf_val
        
    
    def __is_leaf__(self):
        '''
        Returns true if node is a leaf node or false if a decision node
        
        Arguments:
            N/A
        
        Exceptions:
            N/A
            
        Return Value:
            (boolean)       - true if node is leaf, false if node is decision
        '''
        
        return self.leaf_val is not None