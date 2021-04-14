
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
    
    def print_t(self):
        print (f'\tq{self.start} -> q{self.end} when {self.regex} comes.')


class formal_nfa:
    def __init__(self, regex):
        self.Q = 2
        self.transitions = []
        self.start = 0
        self.accept = 1
        self.must_change_states = {}
        self.find_transitions(0,1,regex.replace(" ", ""))
        self.deleteStartofStar()
        self.print_nfa()


    def print_nfa(self):
        print("\n\n\nStates: ", end=" ")

        for i in range(self.Q):
            print(f'q{i}', end=" ")
        
        print("\nLanguage: All ASCII Chracters except \"+\", \"*\", \"(\", \")\"\n")
        
        print("Transitions: ")
        for a in self.transitions:
            a.print_t()

        print(f"\nStart state is q{self.start}")

        print(f"Accept state is q{self.accept}\n\n")


    def optimizeChangables(self):
        def getKey(val):
            for key, value in self.must_change_states.items():
                 if val == value:
                     return key

        somethingChanged = True
        while(somethingChanged):
            somethingChanged = False
            for value in self.must_change_states.values():
                for key in self.must_change_states.keys():
                    if value == key:
                        tempValue = self.must_change_states.get(key)
                        tempKey = getKey(value)
                        self.must_change_states[tempKey] = tempValue
                        somethingChanged = True
        




    def deleteStartofStar(self):
        self.optimizeChangables()

        for key, value in self.must_change_states.items():
            if key == self.start:
                self.start = value
            if key == self.accept:
                self.accept = value
            for t in self.transitions:
                if t.end == key:
                    print(f"{t.start} -> {t.end}   ---   {t.start} -> {value}")
                    t.end = value
                if t.start == key:
                    t.start = value



    def readyForConcanetion(self, regex):
        p = 0

        for element in regex:
            if(element == "("):
                p = p + 1
            elif(element == ")"):
                p = p - 1

            if (p == 0 and (element == "|")):
                return False

        return True


    def findBracketsStartPoint(self, regex, bracket):
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

    def find_transitions(self, start, end, regex):
        t = transition(start, end, regex)

        #self.transitions.append(t)

        #t.print_t()

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
                
                #t.print_t()

                

                if(element == "("):
                    p = p + 1
                elif(element == ")"):
                    p = p - 1
                
                if(element == "|" and p == 0):
                    self.find_transitions(t.start, t.end, t.regex[0:i])
                    self.find_transitions(t.start, t.end, t.regex[i+1:])
                    break

                elif(i < len(regex) - 1 and self.readyForConcanetion(t.regex)  and p == 0):
                    if(t.regex[i+1] not in ["|", "*"]):
                        b = self.Q
                        self.Q = self.Q + 1
                        self.find_transitions(t.start, b , t.regex[0:i+1])
                        self.find_transitions(b , t.end, t.regex[i+1:])
                        
                        break


                elif(element == "*" and p == 0):
                    print("in star")
                    point = i

                    if(t.regex[i-1] == ")"):
                        point = self.findBracketsStartPoint(t.regex, i-1)

                    self.must_change_states[t.start] = t.end
                    self.find_transitions(t.end, t.end, t.regex[point - 1: i])
                    
                    
                    if i != len(t.regex) - 1:
                        self.find_transitions(t.start, t.end, t.regex[0:point-1] + t.regex[i+1:])
                    '''else:
                        if t.end == self.accept:
                            self.accept = t.start'''

                    break






#nfa = formal_nfa("1(1*01*01*)*")  #formal nfa 


"""
Düzeltilmesi gerekli:
--- Değişkenler anlamdırılmalı
--- Comment eklenmeli
--- Stateler estetik olarak düzeltilmeli



Testi geçti:

(aa | ab | ba | bb)*
10|(0|11)0*1
(a|b)*aba
ab
a|b
a*
(ab|a)*
1(1*01*01*)*

Testi geçemedi:

---

"""


#print()
#for a in nfa.transitions:
    #a.print_t()

#print(nfa.readyForConcanetion("1 (1* 01* 01*)*".replace(" ", "")))

#nfa.print_nfa()