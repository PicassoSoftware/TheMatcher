from state import State, StateControl
from reg2nfa import formal_nfa


# Check for is it acceptable
def isItAcceptableForDfa(ch, dfa):

    for item in statesControl.allStatesForDfa:
        # Checking for is the 'ch' that expected in right 'state'.
        if (ch in item.get('properties').keys() and dfa == item.get('state')):
            # If it's all correct until here, return 'next' state value.
            return item.get('properties').get(ch)
    # If not, return error state value.
    return -1


def isItAcceptableForNfa(string,dfa,index=0):
    possibleStates = []
    try:
        for item in statesControl.allStatesForNfa:
            if string[index] in item.get('char') and dfa == item.get('state'):
                for value in item.get('next'):
                    possibleStates.append(value)
        # Wrong value or wrong state.
        if possibleStates == []:
            return False
    except IndexError:
        # End of the process. That means out of the index range.
        if dfa == nfaCreator.accept:
            return True
        else:
            return False

    for dfaValue in possibleStates:
        # When the process is over, if True returns, that string is right.
        if(isItAcceptableForNfa(string,dfaValue,index+1)):
            return True
    # if it's not.
    return False


# That function uses other functions respectively for provides to know that string is acceptable.
def checkPoint(string):
    dfa = nfaCreator.start  # Start state
    for i in string:
        dfa = isItAcceptableForDfa(i, dfa)
        print(dfa)
        # Return 'True' or 'False' checking by dfa value.
        if dfa == -1:  # Error state
            return False
    if dfa == nfaCreator.accept:  # Accept state
        return True


# Getting all values that desired as a list.
def stateCreator(list, stateList, isItEnd=False):
    for value in stateList:
        tempList = []
        for item in nfaCreator.transitions:
            if item.start == value:
                if isItEnd:
                    tempList.append(item.end)
                else:
                    tempList.append(item.regex)
        list.append(tempList)
        del tempList


nfaCreator = formal_nfa("(a|b)*aba")

stateList = []
for item in nfaCreator.transitions:
    if item.start not in stateList:
        stateList.append(item.start)

expectedValueList = []
nextStateList = []
stateCreator(expectedValueList, stateList)
stateCreator(nextStateList, stateList, True)


# Create a stateControl object.
statesControl = StateControl()

# Creating state then adding into statesControl.
for i in range(len(stateList)):
    newState = State()
    for item in expectedValueList[i]:
        newState.values.append(item)
    for item in nextStateList[i]:
        newState.next.append(item)
    newState.stateValue = stateList[i]
    statesControl.addState(newState)

strings = ['aba', 'ababa', 'aabcd', 'dabcd', 'abbcd']
selection = 0 # Which process to choose (0) -> NFA / (1) -> DFA
if selection:
    for string in strings:
        if checkPoint(string):
            print('{} acceptable!'.format(string))
else:
    print(isItAcceptableForNfa('abababababa', nfaCreator.start))
