import random

from Weight import Weight
from Code.Calculate_map import calculate_map
initWeights = [3, 3, 3, 3]
calculator = calculate_map()
list = []

class ML():
    def learn_method(self):


        for i in range(5):
            l = [0, 0, 0, 0]
            score = 0.0
            for v in range(4):
                l[v] = random.randint(1, 10)

            cal = calculator.cal_map(l[0], l[1], l[2], l[3])
            score = cal.get("map") * cal.get("ndcg")

            w = Weight(l, score)
            list.append(w)
        list.sort()

                                     #we use evolutionary algorithms for finding best weights
                                     #to ways to generate new weights, that is decided randomly

                                     #in first way, we take 2 array and combine weights 
                                     # based on a nrandom alpha number
        for n in range(1000):

            choice = random.randint(0, 1)
            # w1 = Weight()
            l1 = [0, 0, 0, 0]
            s = 0.0


            if choice == 0:
                alpha = random.random()
                c1 = random.randint(0, 3)
                c2 = random.randint(0, 3)

                for i in range(4):
                    l1[i] = (list[c1].weights[i] * alpha) + (list[c2].weights[i] * (1-alpha))


            else:
                alpha = random.randint(1, 3)
                c1 = random.randint(0, 3)
                c2 = random.randint(0, 3)

                for i in range(0, alpha):
                    l1[i] = list[c1].weights[i]
                for i in range(alpha, 4):
                    l1[i] = list[c2].weights[i]



                #here we call ealsticSearch and calculate score, forexample imagine score is 9
                #w1.score = f(l1[0], l1[1], l1[2], l1[3])
                #w1.score = f(l1)

            cal = calculator.cal_map(l1[0], l1[1], l1[2], l1[3])
            s = cal.get("map") * cal.get("ndcg")
            w1 = Weight(l1, s)
            list.append(w1)
            list.sort()
            list.pop()


        print("done")

