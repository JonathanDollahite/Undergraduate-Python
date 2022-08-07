def make_dict_from_line(keys, line):

    flu_dict = {}

    x = line.split(',')
    y = 0
    for key in keys:
        flu_dict[key] = x[y]
        y += 1
    print(flu_dict)
    return flu_dict

keys = [ 'REGION TYPE', 'REGION', 'YEAR', 'WEEK', 'TOTAL SPECIMENS', 'TOTAL A', 'TOTAL B', 'PERCENT POSITIVE', 'PERCENT A', 'PERCENT B' ]

'''week = input('Week: ')
year = input('Year: ')'''

fh = open('WHO_NREVSS_Clinical_Labs.csv')
flu = fh.readlines()
print(flu)
'''for f in flu:
    d = make_dict_from_line(keys, f)
    d[YEAR] =
'''
