import math

def knapsack(values):
    max_chance = 0
    num_papers = 0
    cum_odds = [1]
    values.sort()

    while values:
        v = values.pop()
        v_fail = (100-v) / 100
        v_success = v / 100
        #print(v, v_fail, v_success)

        chance = 0
        for i in range(1, len(cum_odds)):
            chance += math.pow(i, i/(num_papers+1)) * cum_odds[i] * v_fail
            chance += math.pow(i, i/(num_papers+1)) * cum_odds[i] * v_success
            print("Chance w/ fail {}: {}".format(i, math.pow(i, i/(num_papers+1)) * cum_odds[i] * v_fail))
            print("Chance w/ success {}: {}".format(i, math.pow(i, i/(num_papers+1)) * cum_odds[i] * v_success))

        chance += (num_papers+1) * cum_odds[len(cum_odds)-1] * v_fail
        chance += (num_papers+1) * cum_odds[len(cum_odds)-1] * v_success
        print("Chance w/ fail {}: {}".format(num_papers+1, (num_papers+1) * cum_odds[len(cum_odds)-1] * v_fail))
        print("Chance w/ success {}: {}".format(num_papers+1, (num_papers+1) * cum_odds[len(cum_odds)-1] * v_success))
        print("Breakdown {} {} {}".format(num_papers+1, cum_odds[len(cum_odds)-1], v_success))

        print(chance)

        num_papers += 1
        
        new_cum_odds = []
        for c in cum_odds:
            new_cum_odds.append(c * v_fail)
            new_cum_odds.append(c * v_success)

        cum_odds = new_cum_odds

        if chance > max_chance:
            max_chance = chance

        print("cum_odds: {} {}".format(len(cum_odds), cum_odds))

    return max_chance

if __name__ == "__main__":
    num = int(input()) # number of papers
    line = list(input().split(' '))
    values = [int(num) for num in line]
    print(knapsack(values))

