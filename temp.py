# def isPrime(x):

#     i = 2
#     while i * i <= x:
#         if x % i == 0:
#             return False
#         i += 1
        
#     return True


# while True:

#     n = int(input())

#     count = 0
#     for i in range(n + 1, 2 * n + 1):
#         if isPrime(i):
#             count += 1
#     print(count)

#     if n == 0:
#         break

a = 1
b = 123456
nRange = list(range(a, 2 * b + 1))
print(nRange)