x = ['a', 'b', 'c']
y = [1, 2, 3, 4]

z = [i for i in zip(x,y) if i[1] % 2 == 0]

z = []
for i in zip(x, y):
    if i[1] % 2 == 0:
        z.append(i)

print(z)
