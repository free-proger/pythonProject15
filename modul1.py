import sys

if __name__ == '__main__':
    k=0
    s=0
    A = [ int(input()) for i in range(10) ]
    for i in range(len(A)):
        if A[i]<0 and A[i]%7==0:
            s+=A[i]
            k+=1
    print(s,k)