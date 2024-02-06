class Prime():
    def __init__(self,mylist):
        self.mylist=mylist
    def filter_prime(self):
        primes=[]
        for i in self.mylist:
            cnt=0
            for j in range(1,i):
                if i%j==0:
                    cnt+=1
            if cnt==1:
                primes.append(i)
        size=lambda a:a+len(primes)
        print("Primes: ",primes,)
        print("The size of primes: ",size(0))
nums=Prime([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
nums.filter_prime()
