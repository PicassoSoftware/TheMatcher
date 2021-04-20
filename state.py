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
        stateDict = {}
        stateProperties = dict(zip(obj.values, obj.next))
        stateMood = obj.stateValue
        stateDict.setdefault('state', stateMood)
        stateDict.setdefault('properties', stateProperties)
        '''
            e.g.:
                {'state': 0, 'properties': {'a': 0, 'b': 2}}
                {'state': 1, 'properties': {'b': 2}}
                {'state': 2, 'properties': {'c': 3}}
                {'state': 3, 'properties': {'d': 0}}                       
        '''
        return stateDict