
def gcd(m, n):
    if m == n:
        return m

    if m > n:
        return gcd(m-n, n)
    elif m < n:
        return gcd(m, n-m)

    return -1

def cut(m, n):

    old_m = m
    old_n = n
    while True:
#        print(m, n)
        if m == n:
            divisor = m
            break
        if m == 0:
            divisor = n
            break
        if n == 0:
            divisor = m
            break
        if m == 1 or n == 1:
            divisor = 1
            break

        if m > n:
            m = m % n
        elif n > m:
            n = n % m

    if divisor == 1:
        if old_m % 2 == 1 and old_n % 2 == 1:
            return 1
        else:
            return 0
    else:
        sub_m = old_m // divisor
        sub_n = old_n // divisor
        if sub_m % 2 == 1 and sub_n % 2 == 1:
            return divisor
        else:
            return 0

if __name__ == "__main__":
    nums = list(input().split(' ')) # size of matrix
    m = int(nums[0])
    n = int(nums[1])
    print(cut(m,n))

