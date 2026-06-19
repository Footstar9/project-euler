
m=11*13*17*19*20*7*3*4*3
print(m)

divisible= False
n=40
while divisible == False:
    for i in range (1,21):
        if  n % i != 0:
            n+=1
            break
    else:
        divisible= True
        print(n)
