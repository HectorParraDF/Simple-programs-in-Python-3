#This simple script uses the sieve of Eratosthenes to compute all the primes
#numbers up to the value rg.
primes = [2]
sieve = []
rg = 1000

#Append all the prime numbers to the list "primes"
for i in range(2, rg):
    if (i in sieve) == 0:
        primes.append(i)
        for j in range(0, int(rg/i) + 1):
            sieve.append(i*j)
        (j)  
    (i)

#Print all the primes
for k in range(1, len(primes)):
    print(primes[k])
    (k)


