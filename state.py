class State():
    def __init__(self):
        self.values = []
        self.next = []
        self.stateValue = 0


class StateControl():
    def __init__(self):
        self.allStates = []


    def addState(self, obj: State):
        stateDict = self.ready2Add(obj)
        self.allStates.append(stateDict)


    def ready2Add(self, obj: State):
        stateDictForNfa = {}
        stateDictForNfa.update(
            {
                'state': obj.stateValue,
                'next': obj.next,
                'char': obj.values
            }
        )

        return stateDictForNfa
