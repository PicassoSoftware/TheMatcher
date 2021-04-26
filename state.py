class State():
    def __init__(self):
        self.values = []
        self.next = []
        self.stateValue = 0


class StateControl():
    def __init__(self):
        self.allStatesForNfa = []
        self.allStatesForDfa = []

    def addState(self, obj: State):
        stateDictForNfa, stateDictForDfa = self.ready2Add(obj)
        self.allStatesForDfa.append(stateDictForDfa)
        self.allStatesForNfa.append(stateDictForNfa)


    def ready2Add(self, obj: State):

        #                       FOR NFA                         #
        #########################################################
        stateDictForNfa = {}
        stateDictForNfa.update(
            {
                'state': obj.stateValue,
                'next': obj.next,
                'char': obj.values
            }
        )
        ##########################################################


        #                        FOR DFA                         #
        ##########################################################
        stateDictForDfa = {}
        stateProperties = dict(zip(obj.values, obj.next))
        stateMood = obj.stateValue
        stateDictForDfa.setdefault('state', stateMood)
        stateDictForDfa.setdefault('properties', stateProperties)
        '''
            e.g.:
                {'state': 0, 'properties': {'a': 0, 'b': 2}}
                {'state': 1, 'properties': {'b': 2}}
                {'state': 2, 'properties': {'c': 3}}
                {'state': 3, 'properties': {'d': 0}}
        '''
        ###########################################################

        return stateDictForNfa,stateDictForDfa
