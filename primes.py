import math
import time
import sys
def nprimes(start = 1000000,num=100000,freq=1000):
    total = 0
    file = open("primes.txt","r")
    primes = file.readlines()
    file.close()
    for i in range(len(primes)):
        primes[i] = int(primes[i])
    count = start
    lc = 0
    maximum = start+num
    while count < maximum:
        val = True
        for prime in primes:
            if(count < 1000):
                if prime < math.ceil(count/2) and count%prime == 0:
                    val = False;
                    break;
                
            else:
                if prime < math.ceil(math.sqrt(count)) and count%prime == 0:
                    val = False;
                    break;
        if val:
            primes.append(count)
            total+=1

        if freq != -1 and len(primes)%freq == 0 and lc != len(primes):
            lc = len(primes)
            print(primes[-1])
        count += 1
    string = ""
    for prime in primes:
        string += str(prime)+"\n"
    file = open("primes.txt","w+")
    file.write(string)
    file.close()
    return total
    
