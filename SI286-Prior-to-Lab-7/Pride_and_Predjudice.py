fhand = open('pride-and-prejudice.txt')
counts = dict()

for line in fhand:
    words = line.lower().split()
    for word in words:
        print(word)
        if word in count:
            counts[word] = counts[word] + 1
        else:
            counts[word]
print('Pride =', counts['pride'])
print('prejudice', counts['prejudice'])
