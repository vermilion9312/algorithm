'''
	[문제]
		a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
		단, 중복없는 숫자로 저장한다.
	
	[예시]
		[1,4,2,3]
'''
import random
a = []

print('===[2023-02-04 (토) # 03]===')

b = set()
while len(a) < 4:
	r = random.randint(1, 4)
	b.add(r)
	a = list(b)
print(a)


print('===[2023-02-04 (토) #02]===')
while len(a) < 4:
	r = random.randint(1, 4)

	check = True
	for i in range(len(a)):
		if r == a[i]:
			check = False
	
	if check:
		a.append(r)
print(a)


print('===[2023-02-04 (토) #01]===')

while len(a) < 4:

	check = True
	r = random.randint(1, 4)
	if r in a:
		check = False

	if check:
		a.append(r)
print(a)

