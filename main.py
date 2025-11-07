# 1
for i in range(1, 51):
    if i % 7 == 0 :
        print(i)
        break


# 2
for i in range(100, 150):
    if i == 137:
        print(i)
        break

# 3
sum = 0

for i in range(1, 20):
    sum += i
    if sum >= 20:
        break

print(sum)


# 4
kop = 1

for i in range(1, 20):
    kop *= i
    if kop >= 10000:
        break

print(kop)
