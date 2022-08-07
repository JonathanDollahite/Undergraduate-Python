import matplotlib.pyplot as plt
import seaborn as sns

#ask for filename and read in info
filename = input('Type in a filename: ')
country = input('Type in a country: ')
with open(filename, errors='replace') as f:
    lines = f.readlines()
#print(lines[9])

#access all the lines with somalia and feed + seed
list = []
for line in lines:
    if (country in line) and ('Feed + Seed' in line):
        list.append(line)
        #print(line)

#print ou each line with the year and amount
#print(somalia)
#print(somalia[1])
years = []
counts = []
for line in list:
    if 'Total Grains/Cereals' in line:
        yr_amt = line.split(',')
        print(yr_amt)
        years.append(int(yr_amt[4]))
        counts.append(float(yr_amt[5]))
#print(years)
#print(counts)

#regression plot
sns.regplot(years, counts, label="years/counts")

#final code to generate details
plt.legend()
plt.title('years/counts')
plt.show()
