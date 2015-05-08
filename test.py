Opinions = dict([('strong buy', 1), ('buy', 2), ('hold', 3), ('sell', 4), ('strong sell', 5)])

# 1
def compare(opinion1, opinion2):
    if Opinions[opinion1] < Opinions[opinion2]:     # check if the first element is worth less
        return -1                                       # if so, return -1
    elif Opinions[opinion1] == Opinions[opinion2]:  # check if both elements are the same
        return 0                                        # if so, return 0
    else:                                           # the second element must be worth more
        return 1                                        # if so, return 1


# 2
def changes(opinions):
    changes = []                                        # this will be the result set
    for i in range(len(opinions) - 1):                  # do this for each element except the last one
        if compare(opinions[i], opinions[i+1]) == -1:   # check if this is a downgrade
            changes.append('downgrade')                     # if so, add this to the result list
        elif compare(opinions[i], opinions[i+1]) == 0:  # check if this is the same
            changes.append('same')                          # if so, add this to the result list
        elif compare(opinions[i], opinions[i+1]) == 1:  # check if this is an upgrade
            changes.append('upgrade')                       # if so, add this to the result list
    return changes                                      # return result


#3 
def currentOpinions(opinionList):
    current = []                           # this will be the result set
    for item in range(len(opinionList)):   # do this for each analyst's list
        temp = opinionList[item]           # momentarily store the current list
        current.append(temp[len(temp)-1])  # add the last item in this list
    return current                         # return result


#4
def removeEmpties(seq):
    result = []                            # this will be the result set
    for item in range(len(seq)):           # do this for each list element in the list
        temp = seq[item]                   # momentarily store the current list
        if len(temp) > 0:                  # if this list contains elements
            result.append(temp)                 # add this to the result set
    return result                          # return result
            

#5
def averageRating(opinions):
    average = 0.0                          # let average begin at 0
    if len(opinions) == 0:                 # if the list is empty
        return 0                                # return 0
    for i in range(len(opinions)):         # for each item in opinions list
        average += Opinions[opinions[i]]        # add up each numerical value
    return average/len(opinions)           # return the average

# 1
print compare('buy', 'hold')
print compare('hold', 'hold')
print compare('sell', 'hold')

# 2
op = ['sell', 'buy', 'hold', 'buy', 'strong sell', 'strong buy']
print changes(op)
#op = ['sell']
#print changes(op)

# 3
print currentOpinions([['hold','sell','strong sell'],['sell', 'sell']])

# 4
print removeEmpties([[1,2],[],['a'],[],[],[],['a','b']])

# 5
print averageRating(['strong sell', 'sell'])