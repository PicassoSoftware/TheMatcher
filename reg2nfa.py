# Transitions class hold transitions 
class transition:
    def __init__(self, start, end, regex): 
        self.start = start
        self.end = end
        self.regex = regex
    
    # This function checks transition done or not.
    def isDone(self):
        if(len(self.regex) == 1):
            return True
        else:
            return False
    
    # Print transition prettier.
    def print_t(self):
        print (f'\tq{self.start} -> q{self.end} when {self.regex} comes.')


# NFA class
class formal_nfa:
    def __init__(self, regex):
        self.Q = 2
        self.transitions = []
        self.start = 0
        self.accept = [1]
        self.must_change_states = {}
        self.__find_transitions(0,1,regex)
        self.__deleteStartofStar()

    # Print NFA. 
    def print_nfa(self):

        print("\n\n\nStates: ", end=" ")

        for i in range(self.Q):
            print(f'q{i}', end=" ")
        
        print("\nLanguage: All ASCII Chracters except \"+\", \"*\", \"(\", \")\"\n")
        
        print("Transitions: ")
        for a in self.transitions:
            a.print_t()

        print(f"\nStart state is q{self.start}")

        print(f"Accept state is q{self.accept[0]}\n\n")


    '''
    This function optimize changable states

    For Example:
        q2 must change to q1
        q1 must change to q3
        q4 must change to q5
        q6 must change to q1
    
    As you can see we must change "q1"s to "q3" on right side, because of row 2.

    __optimizeChangables function do this operation.
    ''' 

    def __optimizeChangables(self):
        # Find key by given value.
        def getKey(val):
            for key, value in self.must_change_states.items():
                 if val == value:
                     return key

        somethingChanged = True  

        while(somethingChanged): # We must check all situations.

            somethingChanged = False

            for value in self.must_change_states.values():
                for key in self.must_change_states.keys():
                    if value == key:
                        tempValue = self.must_change_states.get(key)
                        tempKey = getKey(value)
                        self.must_change_states[tempKey] = tempValue
                        somethingChanged = True
        



    # This Function delete unnecessary states. (For better understanding check out Readme)
    def __deleteStartofStar(self):
        self.__optimizeChangables()

        for key, value in self.must_change_states.items():
            if key == self.start:
                self.start = value
            if key == self.accept[0]:
                self.accept[0] = value
            for t in self.transitions:
                if t.end == key:
                    t.end = value
                if t.start == key:
                    t.start = value
        
        self.__cleanStates()

    
    # This function takes n as input and decrease 1 states which greater than n
    # For example:
    # before  -  0 1 2 3 4 5 6
    #       minus_1_all_states_after(3)
    # after   -  0 1 2 3 4 5
    
    def __minus_1_all_states_after(self, n):
        for t in self.transitions:
            if t.start > n:
                t.start = t.start - 1
            if t.end > n:
                t.end = t.end - 1

        for key, value in self.must_change_states.items():
            if key > n:
                key = key - 1
            if value > n:
                value = value - 1
        
        if self.start > n:
            self.start = self.start - 1
        if self.accept[0] > n:
            self.accept[0] = self.accept[0] - 1
            
            
    def __cleanStates(self):
        self.Q = self.Q - len(self.must_change_states)

        for key in self.must_change_states:
            self.__minus_1_all_states_after(key)

            
        


    # This function check regex if there is "Union" operation it returns false else return true 
    # and this meaning we can parse other operations.

    def __IsThereAnyUnion(self, regex):
        p = 0

        for element in regex:
            if(element == "("):
                p = p + 1
            elif(element == ")"):
                p = p - 1

            if (p == 0 and (element == "|")):
                return False

        return True


    # This function find "(" in regex if position of ")" is given.
    def __findBracketsStartPoint(self, regex, bracket):
        regex = regex[0:bracket]
        p = -1

        for i, element in enumerate(reversed(regex)):
            if(element == "("):
                p = p + 1
            elif(element == ")"):
                p = p - 1
            
            if (p == 0):
                return len(regex) - i 

        return -1

    # This is recursive function which find next transition.
    
    def __find_transitions(self, start, end, regex):

        t = transition(start, end, regex)

        # Checking transition. If True we our t to add transitions 
        if(t.isDone()):
            self.transitions.append(t)
        else:
            p = 0
            
            stack = []

            if(t.regex[0] == "(" and t.regex[-1] == ")"):
                for i, c in enumerate(t.regex):
                    if(c == "("):
                        stack.append(i)
                    elif(c == ")"):
                        if(i == len(t.regex)-1 and stack[-1] == 0):
                            t.regex = t.regex[1:-1]
                            break
                        stack.pop()
                    else:
                        continue


            for i, element in enumerate(t.regex):

                if(element == "("):
                    p = p + 1
                elif(element == ")"):
                    p = p - 1
                
                if(element == "|" and p == 0):
                    self.__find_transitions(t.start, t.end, t.regex[0:i])
                    self.__find_transitions(t.start, t.end, t.regex[i+1:])
                    break

                elif(i < len(regex) - 1 and self.__IsThereAnyUnion(t.regex)  and p == 0):
                    if(t.regex[i+1] not in ["|", "*"]):
                        b = self.Q
                        self.Q = self.Q + 1
                        self.__find_transitions(t.start, b , t.regex[0:i+1])
                        self.__find_transitions(b , t.end, t.regex[i+1:])
                        
                        break


                elif(element == "*" and self.__IsThereAnyUnion(t.regex) and p == 0):

                    point = i

                    if(t.regex[i-1] == ")"):
                        point = self.__findBracketsStartPoint(t.regex, i-1)

                    if (t.start != t.end):
                        self.must_change_states[t.start] = t.end
                    self.__find_transitions(t.end, t.end, t.regex[point - 1: i])
                    
                    
                    if i != len(t.regex) - 1:
                        self.__find_transitions(t.start, t.end, t.regex[0:point-1] + t.regex[i+1:])

                    break
