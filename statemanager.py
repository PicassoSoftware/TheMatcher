from state import State, StateControl
from reg2nfa import formal_nfa

class CheckStateManager:
    def __init__(self, automataController):
        self.automataController = automataController
        self.stateList = []
        self.expectedValueList = []
        self.nextStateList = []

        # Get all lists values.
        self.getLists()

        # Create a stateControl object.
        self.statesControl = StateControl()
        self.addToStatesControl()


    def getLists(self):
        for item in self.automataController.transitions:
            if item.start not in self.stateList:
                self.stateList.append(item.start)
        self.stateCreator(self.expectedValueList, self.stateList)
        self.stateCreator(self.nextStateList, self.stateList, True)


    # Getting all values that desired as a list.
    def stateCreator(self,list, stateList, isItEnd=False):
        for value in stateList:
            tempList = []
            for item in self.automataController.transitions:
                if item.start == value:
                    if isItEnd:
                        tempList.append(item.end)
                    else:
                        tempList.append(item.regex)
            list.append(tempList)
            del tempList


    def addToStatesControl(self):
        # Creating state then adding into statesControl.
        for i in range(len(self.stateList)):
            newState = State()
            for item in self.expectedValueList[i]:
                newState.values.append(item)
            for item in self.nextStateList[i]:
                newState.next.append(item)
            newState.stateValue = self.stateList[i]
            self.statesControl.addState(newState)
            del newState

    def checkString(self,string):
       return self.isItAcceptable(string,self.automataController.start)


    def isItAcceptable(self,string,dfa,index=0):
        possibleStates = []

        try:
            for item in self.statesControl.allStates:
                if string[index] in item.get('char') and dfa == item.get('state'):
                    for value in item.get('next'):
                        possibleStates.append(value)
            # Wrong value or wrong state.
            if not possibleStates:
                return False
        except IndexError:
            # End of the process. That means out of the index range.
            if dfa == self.automataController.accept:
                return True
            else:
                return False

        for dfaValue in possibleStates:
            # When the process is over, if True returns, that string is right.
            if(self.isItAcceptable(string,dfaValue,index+1)):
                return True
        # if it's not.
        return False




if __name__ == "__main__":
    nfaController = formal_nfa('(ab|a)*')
    controlManager = CheckStateManager(nfaController)

    stringList = ['abab','a','aaa','sırat','ba','ab','baba']
    for string in stringList:
        if controlManager.checkString(string):
            print('{0} accepted.'.format(string))
