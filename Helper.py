from random import randint
import numpy as np

def splitTrainTest(*args, splitSize):
    
    newData = []
    for sets in args:
        train = []
        accessedIdx = []
        limit = int(len(sets) * splitSize)
        
        # train set
        i = 0
        while i < limit:
            idx = randint(0, len(sets) - 1)
            if idx not in accessedIdx:
                train.append(sets[idx])
                accessedIdx.append(idx)
                i += 1
                
        train = np.array(train)
        test =  np.array([sets[idx] for idx in range(0, len(sets)) if idx not in accessedIdx])
        newData.append(train)
        newData.append(test)
    return newData
        
        
        