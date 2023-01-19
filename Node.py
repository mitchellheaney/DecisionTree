
class Node:
    
    def __init__(self, feature=None, thres_quant=None, left=None, right=None, leaf_val=None):
        self.feature = feature
        self.thres_quant = thres_quant
        self.left = left
        self.right = right
        self.leaf_val = leaf_val
        
    def is_leaf(self):
        return self.leaf_val is not None