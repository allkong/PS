total = 0
for i in range(5):
    s = int(input())
    if s < 40:
        s = 40
    total += s
print(total // 5)