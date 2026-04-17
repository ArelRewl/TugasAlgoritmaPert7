def fibonacci(N):
    if N<=1:
        return N
    else:
        return fibonacci(N-2)+fibonacci(N-1)
    
N = int(input('masukan N : '))


for i in range(1,N+1):
    print(fibonacci(i))