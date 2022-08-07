fhand = open('pride-and-prejudice.txt')
counts = dict()

for line in fhand:
    words = line.lower().split()
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
print('Pride =', counts['pride'])
print('prejudice', counts['prejudice'])
