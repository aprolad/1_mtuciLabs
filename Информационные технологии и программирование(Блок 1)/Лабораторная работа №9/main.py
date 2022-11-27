

tuple = tuple(float(el) for el in input().split())
pos = 0
neg = 0
for i in range(len(tuple)-1):
    if tuple[i] + tuple[i+1] > 0:
        pos += 1
    elif tuple[i] + tuple[i + 1] < 0:
        neg += 1
print("Количество положительных соседних пар: " + str(pos))
print("Количество отрицательных соседних пар: " + str(neg))