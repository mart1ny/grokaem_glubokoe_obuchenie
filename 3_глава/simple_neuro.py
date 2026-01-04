weights = [0.1, 0.2, 0]
# def neural_network(weight, input):
#     prediction = input * weight
#     return prediction

number_of_toes = [8.5, 9.5, 10, 9]
# input = number_of_toes[0]
# pred = neural_network(weights, input)
# print(pred)

# Более сложная сеть на 3 входных признака

toes = [8.5, 9.5, 9.9, 9.0]
wins = [0.65, 0.8, 0.8, 0.9]
fans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wins[0], fans[0]]

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

def neural_network(weights, input):
    prediction = w_sum(weights, input)
    return prediction

pred = neural_network(weights, input)
print(pred)

