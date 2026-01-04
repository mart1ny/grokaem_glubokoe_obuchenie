# weights = [0.3, 0.2, 0.9]
# wlrec = [0.65, 0.8, 0.8, 0.9]
# input = wlrec[0]
# def ele_mul(number, vector):
    
#     output = [0, 0, 0]

#     assert(len(output) == len(vector))
#     for i in range(len(vector)):
#         output[i] = number * vector[i]
#     return output

# def neuro_network(weights, input):
#     prediction = ele_mul(weights, input)
#     return prediction

# pred = neuro_network(weights, input)
# print(pred)


import numpy as np

# игр % побед болельщики 
ih_wgt = np.array([[0.1, 0.2, -0.1],    #hid[0]
                   [-0.1, 0.1, 0.9],    #hid[1]
                   [0.1, 0.4, 0.1]]).T  #hid[2]

#hid[0] hid[1] hid[2]
hp_wgt = np.array([[0.3, 1.1, -0.3],    #травмы?
                   [0.1, 0.2, 0.0],     #победа?
                   [0.0, 1.3, 0.1]]).T  #печаль?

weights = [ih_wgt, hp_wgt]

def neural_network(weights, input):
    hid = np.dot(weights[0], input)
    pred = np.dot(weights[1], hid)
    return pred

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
fans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wlrec[0], fans[0]])

pred = neural_network(weights, input)
print(pred)
