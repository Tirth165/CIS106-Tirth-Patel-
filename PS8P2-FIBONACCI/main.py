# InputPhase
a, b = 1, 1

# ProcessPhase 
print(a)
print(b)

# OutputPhase
for _ in range(18):
    c = a + b


    print(c)


    a, b = b, c
