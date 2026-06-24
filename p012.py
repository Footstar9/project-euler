# D=0
# n=1
# while D <= 500:
    # S=sum(i for i in range (1, n+1))
    # d=0
    # for j in range (1, S+1):
        # if S % j ==0:
            # d+=1
    # if d>D:
       # D=d
    # n+=1
# print(S)
import math
# def divisors(n):
#     M=1
  #   multiplicity= [[c, 0] for c in range(n+1)]
    # sieve= [True] * (n+1)
    # sieve[0]=sieve[1]= False
    # for i in range (2, math.isqrt(n)+1):
      #   sieve[i*i::i]=[False] * len(sieve[i*i::i])
    # for j in range (2, n+1):
        
      #   if sieve[j]==True and n % j == 0:
        #     m=1
          #   for q in range(1,n):
            #     if n % (j**q)==0 and q>m:
              #       m=q
          #   multiplicity[j][1]+=m
    # for g in range (1, n+1):
      #   if multiplicity[g][1]>=1:
        #     M=M*(multiplicity[g][1]+1)
    # return M
# n=1
# d=0
# while d<=500:
  #   print(n)
    # S=n*(n+1)//2
    # D=divisors(S)
    # if D>d:
      #   d=D
   #  n=n+1
# print(S)
    

    

# import math
# def prime(n):
  #   sieve= [True] * (n+1)
    # sieve[0]=sieve[1]= False
   #  for i in range (2, math.isqrt(n)+1):
     #    sieve[i*i::i]=[False] * len(sieve[i*i::i])
    # return [j for j, prime in enumerate(sieve) if prime]

# D=0
# n=1
# S=1
# while D<=500:
  #   d=1
    ## S=n*(n+1)//2
    #  p=prime(S)# # 
    # for k in range(len(p)):
     #    for c in range(1, math.isqrt(S)+1):
       #      if S % (c*p[k]) == 0:
         #        d+=1
    # if d>D:
      #   D=d
    # n+=1
# print(S)
    
def divisor_count(n):
    count=1
    d=2
    while d * d <= n:
        exp=0
        while n % d ==0:
            n //= d

            exp+=1
        count *= (exp+1)
        d+=1
    if n>1:
        count*=2
    return count
D=0
n=1
while D<=500:
    S=n*(n+1)//2
    d=divisor_count(S)
    if d>D:
        D=d
    n+=1
print(S)
