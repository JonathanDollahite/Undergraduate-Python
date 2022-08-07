def create_state_dict():
    fh = open('states.tsv')
    states = fh.readlines()
    states_dict = dict()

    for state in states:
        x = state.strip('\n')
        key,value = x.split('\t')
        states_dict[key] = value

    '''x = input('State: ')
    if x == 'exit':
        print('Goodbye!')

    while x != 'exit':
        if x in states_dict.keys():
            print(states_dict[x])
            x = input('State: ')
        else:
            x = input('State: ')
    '''
    return states_dict

def make_dict_from_line(keys, line):

    flu_dict = {}

    x = line.split(',')
    y = 0
    for key in keys:
        flu_dict[key] = x[y]
        y += 1
    #print(flu_dict)
    return flu_dict

#>--------------------------------------------------------
#>--------------------------------------------------------

keys = [ 'REGION TYPE', 'REGION', 'YEAR', 'WEEK', 'TOTAL SPECIMENS', 'TOTAL A', 'TOTAL B', 'PERCENT POSITIVE', 'PERCENT A', 'PERCENT B' ]

week = input('Week: ') #index value 3
year = input('Year: ') #index value 2

fh = open('WHO_NREVSS_Clinical_Labs.csv')
flu = fh.readlines()
for f in flu:
    d = make_dict_from_line(keys, f)
    if d['YEAR'] == year and d['WEEK'] == week:
        stateID = create_state_dict()
        state = d['REGION']
        print(stateID[state], d['TOTAL A'])
