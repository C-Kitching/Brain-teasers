# Enter your code here. Read input from STDIN. Print output to STDOUT

def sieve(N):
    primes = [True for i in range(N+1)]
    p = 2
    while(p*p < N):
        if(primes[p]):
            for i in range(p*p, N+1, p):
                primes[i] = False
        p += 1
        
    res = []
    for p in range(2, N+1):
        if(primes[p]): res.append(p)
        
    return res

def num_divisors(N, primes):
    res = 1
    for p in primes:
        count = 0
        while(N % p == 0):
            N /= p
            count += 1
        if(count != 0):
            res *= (count + 1)
    return res
            
def find_triangle_nums(N):
    return [n*(n+1)//2 for n in range(1, N+1)]
    
def find_triangle_divisors(triangles, primes):
    res = {}
    for t in triangles:
        d = num_divisors(t, primes)
        if d not in res.keys(): res[d] = t
    return res
    
    
primes = sieve(1000)
triangles = find_triangle_nums(1000)
triangle_divisors = find_triangle_divisors(triangles, primes)

res = {} 
for i in range(1, 1000):
    if i in triangle_divisors.keys():
        curr = triangle_divisors[i]
    res[i] = curr
    
