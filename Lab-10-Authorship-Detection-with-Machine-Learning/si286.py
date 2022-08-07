import math

def cosine_sim(d1, d2):
    """ 
    Given two dictionaries, compute the cosine similarity score between them. 
    The dictionaries must have integer counts as their values. 
    """
    sumprod = 0
    d1squared = 0
    d2squared = 0

    # Sanity checks for Dictionary type ... print error but let function continue
    if not isinstance(d1,dict):
        print('ERROR: cosine_sim first argument is not a Dictionary')
    if not isinstance(d2,dict):
        print('ERROR: cosine_sim second argument is not a Dictionary')
    
    # Compute the similarity score.
    for k1 in d1:
        d1squared += d1[k1]*d1[k1]
        if k1 in d2:
            sumprod += d1[k1]*d2[k1]

    for k in d2:
        d2squared += d2[k]*d2[k]

    return sumprod / (math.sqrt(d1squared)*math.sqrt(d2squared))


def accuracy(L1, L2):
    """
    Given two Lists, compute the accuracy score between their values
    matching.  # matches / length
    """

    # Sanity check for same length
    if len(L1) != len(L2):
        print('ERROR lengths of lists in accuracy() are not the same:', len(L1), len(L2))

    correct = 0
    N = len(L1)
    for i in range(len(L1)):
        if L1[i] == L2[i]:
            correct += 1

    print("Accuracy:", correct/N)
