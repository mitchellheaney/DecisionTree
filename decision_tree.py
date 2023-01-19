

class DecisionTree:
    
    def __init__(self, num_feats, max_depth=100):
        self.num_feats = num_feats
        self.max_depth = max_depth
        self.root = None
    
    