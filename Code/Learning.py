import random

from Weight import Weight
from Code.Calculate_map import calculate_map
initWeights = [3, 3, 3, 3]
calculator = calculate_map()


list = []

for i in range(5):
    w = Weight()
    w.score = 5 + 5 * random.random()
    w.weights = initWeights
    #set score for 3333 search
    list.append(w)
    list.sort()

                                     #we use evolutionary algorithms for finding best weights
                                     #to ways to generate new weights, that is decided randomly

                                     #in first way, we take 2 array and combine weights 
                                     # based on a nrandom alpha number
for n in range(1000):

    choice = random.randint(0, 1)
    w1 = Weight()
    l1 = []


    if choice == 0: 
        alpha = random.random()
        c1 = random.randint(0, 3)
        c2 = random.randint(0, 3)

        for i in range(4):
            w1.weights[i] = (list[c1].weights[i] * alpha) + (list[c2].weights[i] * (1-alpha))


    else:
        alpha = random.randint(1, 3)
        c1 = random.randint(0, 3)
        c2 = random.randint(0, 3)

        for i in range(0, alpha):
            w1.weights[i] = list[c1].weights[i]
        for i in range(alpha, 4):
            w1.weights[i] = list[c2].weights[i]

    l1 = w1.weights


        #here we call ealsticSearch and calculate score, forexample imagine score is 9
        #w1.score = f(l1[0], l1[1], l1[2], l1[3])
        #w1.score = f(l1)
        
    w1.score = calculator.cal_map(w1.weights[0],w1.weights[1],w1.weights[2],w1.weights[3])
    list.append(w1)
    list.sort()
    list.pop()

    print(n)

print("done")

