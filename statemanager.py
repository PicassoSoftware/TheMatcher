from state import State, StateControl
from drawFsm import FsmDrawer

class CheckStateManager:
    def __init__(self, automataController, label):
        self.label = label
        self.automataController = automataController
        self.stateList = []
        self.expectedValueList = []
        self.nextStateList = []
        self.fsmDrawer = FsmDrawer(self.automataController, label)
        self.transitionDict = {}


        self.tempState = -1
        self.tempChar = ""
        

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


    def isItAcceptable(self,string,stateValue,index=0):
        possibleStates = []

        try:
            for item in self.statesControl.allStates:
                if string[index] in item.get('char') and stateValue == item.get('state'):
                    for i in range(len(item.get('next'))):
                        if(item.get('char')[i] == string[index]):
                            if(stateValue != self.tempState or (stateValue == self.tempState and string[index] != self.tempChar)):
                                # Connection to drawFsm
                                currentState = str(item.get('state'))
                                self.fsmDrawer.click(string[index],currentState)
                                self.tempState = item.get('state')
                                self.tempChar = string[index]

                            possibleStates.append(item.get('next')[i])


            # Wrong value or wrong state.
            if not possibleStates:
                return False

        except IndexError:
            # End of the process. That means out of the index range.
            try:
                if stateValue in self.automataController.accept:
                    return True
            except:
                if stateValue == self.automataController.accept:
                    return True
            else:
                return False

        for stateValue in possibleStates:
            # When the process is over, if True returns, that string is right.
            if(self.isItAcceptable(string,stateValue,index+1)):
                return True
        # if it's not.
        return False


