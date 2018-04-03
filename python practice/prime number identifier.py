# list primer number below 500

i = 0
while i < 500:
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=' ')
        i += 1
    else:
        i += 1
