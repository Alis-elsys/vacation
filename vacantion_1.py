num = int(input())
n = num
prime = False


def check():
    global prime
    for i in range(2,n):
        if (n % i) == 0:
            prime = False
            return prime
        else:
            prime = True
            return prime

check()

while num > 1:
    if prime == True:
        print(n)
        break
    else:
        n += 1
        check()

if num == 1:
    print("3")