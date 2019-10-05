
def skipped(num):
    counter = 1
    is_skip = False
    for i in range(num):
        n = int(input())
        #print("input {}".format(n))
        while counter < n:
            is_skip = True
            print(counter)
            counter += 1
        counter += 1

    if not is_skip:
        print("good job")

if __name__ == "__main__":
    num = int(input()) # number of lines
    skipped(num)

