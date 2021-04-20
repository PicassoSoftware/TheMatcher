from state import State,StateControl

# Check for is it acceptable
def isItAcceptable(ch,dfa):
    for item in statesControl.allStates:
        # Checking for is the 'ch' that expected in right 'state'.
        if(ch in item.get('properties').keys() and dfa == item.get('state')):
            # If it's all correct until here, return 'next' state value.
            return item.get('properties').get(ch)
    # If not, return error state value.
    return -1

# That function uses other functions respectively for provides to know that string is acceptable.
def checkPoint(string):
    dfa = 0
    for i in string:
        dfa = isItAcceptable(i, dfa)
        print(dfa)
    # Return 'True' or 'False' checking by dfa value.
        if dfa == -1:
            return False
    return True

states = {
    0: {
        'char': ['a','b'],
        'next': [0,2]
    },
    1: {
        'char': ['b'],
        'next': [2]
    },
    2: {
        'char': ['c'],
        'next': [3]
    },
    3: {
        'char': ['d'],
        'next': [0]
    }
}

# Create a stateControl object.
statesControl = StateControl()

# Adding all states into statesControl.
for i in states.keys():
    # creating a state.
    newState = State()
    for item in states.get(i).get('char'):
        newState.values.append(item)
    for item in states.get(i).get('next'):
        newState.next.append(item)
    newState.stateValue = i
    statesControl.addState(newState)


strings = ['abcd','aabcd','dabcd','abbcd']


for string in strings:
    if checkPoint(string):
        print('{} acceptable!'.format(string))
