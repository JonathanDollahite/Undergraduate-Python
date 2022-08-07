

def create_state_dict(filename):
    fh = open(filename)
    states = fh.readlines()
    states_dict = dict()

    for state in states:
        x = state.strip('\n')
        key,value = x.split('\t')
        states_dict[key] = value

    x = input('State: ')
    if x == 'exit':
        print('Goodbye!')

    while x != 'exit':
        if x in states_dict.keys():
            print(states_dict[x])
            x = input('State: ')
        else:
            x = input('State: ')

    return states_dict

stateIDs = create_state_dict('states.tsv')
