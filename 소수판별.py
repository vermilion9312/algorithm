# 소수: 약수가 1과 자기 자신 밖에 없는 수
# N이 소수가 되려면, 2보다 크거나 같고, N-1보다 작거나 같은 자연수로 나누어 떨어지면 안 된다.




# 1. 어떤 수 N이 소수인지 아닌지 판별하는 방법
import random
N = random.randint(1, 100)
print("N =", N)

# 1-1. 소수 정의의 활용: 구간 [2, N-1]에서 나누어 떨어지는 수가 없으면 소수이다.
# 구간 [2, N-1]
# 시간복잡도: O(N)
print("===[1-1]===")
check = True
for i in range(2, N):
    if N % i == 0:
        check = False

if check:
    print("소수이다")
else:
    print("소수가 아니다")

# 1-2. 약수의 특징 활용: 어떤 수 N이 소수가 아니라고 하자,
# 1을 제외한 가장 작은 약수를 x라 하면, N을 제외한 가장 큰 약수는 N/x이다
# N/x 과 N 사이에는 약수가 없으므로, 즉 구간 [(N/x)+1, N-1]에서 약수가 없으므로
# 구간 [x, (N/x)]에서 나누어 떨어지는 수가 없으면 소수이다.
# 가장 작은 약수를 2라고 하면 구간 [2, N/2] 에서 나누어 떨어지는 수가 없으면 소수이다.

# 구간 [2, N/2]
# 시간복잡도: O(N/2) = O(N)
print("===[1-2]===")
check = True
for i in range(2, N//2 + 1):
    if N % i == 0:
        check = False

if check:
    print("소수이다")
else:
    print("소수가 아니다")

# 1-2. 약수의 대칭성 활용: 어떤 수 N의 약수들은 √N을 기준으로 대칭이다.
# 따라서, √N 기준으로 작은 쪽에 약수가 존재한다면 √N 기준으로 큰 쪽에 약수가 반드시 존재한다.
# 약수 a가 존재하면 약수 N/a 도 반드시 존재하기 때문이다.
# for문에서는 실수계산을 피하기위한 식(i * i)를 쓸 수 없으므로 while문으로 판별한다.

# 구간 [2, √N]
# 시간복잡도: O(√N)
print("===[1-3]===")
i = 2
check = True
while i * i <= N:
    if N % i == 0:
        check = False
    i += 1

if check:
    print("소수이다")
else:
    print("소수가 아니다")

# 2. N보다 작거나 같은 모든 자연수 중에서 소수를 찾아내는 방법
# 에라토스테네스의 체
# 1부터 N까지 범위 아넹 들어가는 모든 소수를 구하려면 에라토스테네스의 체를 사용한다.
# 1. 2부터 N까지 모든 수를 써놓는다.
# 2. 아직 지워지지 않은 수 중에서 가장 작은 수를 찾는다.
# 3. 그 수는 소수이다.
# 이제 그 수의 배수를 모두 지운다.