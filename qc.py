import math

class district:
    def __init__(self, num):
        self.num = num
        self.A = 0
        self.B = 0

def efficiency(p,d):
    districts = [district(i+1) for i in range(d)]
    # aggregate district votes
    for i in range(p):
        line = list(input().split(' '))
        districts[int(line[0])-1].A += int(line[1])
        districts[int(line[0])-1].B += int(line[2])

    wasteA = 0
    wasteB = 0
    totalWasteA = 0
    totalWasteB = 0
    total = 0
    for dist in districts:
        total += dist.A + dist.B
        #print("DEBUG dist # {} A {} B {}".format(dist.num, dist.A, dist.B))
        if dist.A > dist.B:
            wasteA = dist.A - (math.floor((dist.A + dist.B) / 2) + 1)
            wasteB = dist.B
            print("A {} {}".format(wasteA, wasteB))
            totalWasteA += wasteA
            totalWasteB += wasteB
        else:
            wasteA = dist.A
            wasteB = dist.B - (math.floor((dist.A + dist.B) / 2) + 1)
            print("B {} {}".format(wasteA, wasteB))
            totalWasteA += wasteA
            totalWasteB += wasteB
    
    return abs(totalWasteA - totalWasteB) / total

if __name__ == "__main__":
    p_d = list(input().split(' ')) # number of lines
    p = int(p_d[0])
    d = int(p_d[1])
    print(efficiency(p, d))

