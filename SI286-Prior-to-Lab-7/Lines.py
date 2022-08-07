#ask for filename and read in info
filename = input('Type in a filename: ')
with open(filename, errors='replace') as f:
    lines = f.readlines()
#print(lines[9])

#access all the lines with somalia and feed + seed
somalia = []
for line in lines:
    if ('Somalia' in line) and ('Feed + Seed' in line):
        somalia.append(line)
        #print(line)

#print ou each line with the year and amount
#print(somalia)
#print(somalia[1])
for line in somalia:
    if 'Total Grains' in line:
        yr_amt = line.split(',')
        x = yr_amt[4], yr_amt[5]
        print(yr_amt[4], yr_amt[5])
