n = int(input())

a = input().split()

v = input()

count = 0

for elem in a:
    if elem == v:
        count += 1

print(count)
