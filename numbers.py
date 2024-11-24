def is_prime(n):
    p = 0
    if n<=1:
        return 0
    else:
        for i in range(n-1,1,-1):
            if n%i == 0:
                return 0
    return 1
list = []
for i in range(1,100):
    if is_prime(i)==1:
        list.append(i)
with open("primes.txt",'w') as f:
    f.write(str(list))

    
