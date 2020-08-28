#Evaluation Sessions to Model

import numpy as np

#Hyperparameter
minDuration = 2000

# Weights
w0 = 2.0   # Bounce
w1 = 2.0   # SearchFieldClick
w2 = 2.0   # SearchButtonClick
w3 = 1.0   # ScrollBehaviour
w4 = 1.0   # ItemClick
w5 = 1.0   # ECommerceClick
w6 = 0.25  # RandomClick

# load Sessions and Model
Sessions = []
Model = []

# Simulated test data
Sessions = np.random.randint(2,size=(100,9))
Sessions[:,0] = np.random.randint(5, size=100)
Sessions[:,1] = 247
Sessions[:,2] = np.random.randint(100000, size=100)
Sessions[0,-6:] = 0
Sessions[0,2] = 1000

Model = np.zeros((5,2))
Model[:,0] = np.arange(5, dtype = int)

# The Magic 
def evaluation(Sessions, Model):
    
    for setupID in Model[:,0]: 
        events = Sessions[Sessions[:,0] == setupID][:,-7:]
        means  = np.mean(events[:,-6:], axis=0)
        sums   = np.sum(events[:,-6:], axis=1)

        bounceRate = len(events[(sums == 0),0] < minDuration)/len(sums)
        Model[int(setupID)][1] = reward(bounceRate, means)
        
    return Model

def reward(bounceRate, means):
    reward = -w0*bounceRate + w1*means[0] + w2*means[1] + w3*means[2] + w4*means[3] + w5*means[4] + w6*means[5]
    return reward