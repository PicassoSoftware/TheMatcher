import reg2nfa


class transition:
    def __init__(self, start, end, regex):
        self.start = start
        self.end = end
        self.regex = regex


    # Print transition prettier.
    def print_t(self):
        print(f'\tq{self.start} -> q{self.end} when {self.regex} comes.')


class state:         #state object created
    def __init__(self, q, name):
        self.name = name
        if type(q) == int:
            self.q = [q]
        else:
            self.q = q



class formal_dfa:
    def __init__(self, regex):
        self.regex = regex
        self.nfa = reg2nfa.formal_nfa(regex)
        self.accept = self.nfa.accept
        self.start = self.nfa.start
        self.empty = 61 
        self.used_language = []
        self.states = []
        self.table = []
        self.transitions = []
        self.number_of_states = self.nfa.Q
        self.create_table()
        self.find_transitions()
        self.optimize()

    def optimize(self):

        for t in self.transitions:
            t.print_t()
        print()
        ends = [t.end for t in self.transitions]

        for q in range(self.number_of_states):
            if q not in ends and q != self.start:
                print(q, ' bulundu')
                if q in self.accept:
                    self.accept.remove(q)
                    
                for t in self.transitions:
                    if t.start == q:
                        self.transitions.remove(t)
                        break

                for t in self.transitions:
                    if t.start > q:
                        t.start = t.start - 1
                    if t.end > q:
                        t.end = t.end - 1

                self.number_of_states -= 1
                
                if self.start > q:
                    self.start = self.start - 1

                for i, a in enumerate(self.accept):    
                    if a > q:
                        self.accept[i] -= 1

                self.optimize()   
                break
            
              

    def find_transitions(self):
        for start, row in enumerate(self.table):
            for regexnum,end in enumerate(row):

                t = transition(start,end,self.used_language[regexnum])
                if end != self.empty:
                    self.transitions.append(t)


    def add_empty_row_to_table(self):
        row = []
        for i in range(len(self.used_language)):
            row.append(self.empty)

        self.table.append(row)

    def print_table(self):
        print('  |', end=' ')
        for char in self.used_language:
            print(char, end=' ')
        print('')
        for i, row in enumerate(self.table):
            print(chr(i + 65), end=' | ')

            for unnamed_states in row:
                print(chr(unnamed_states + 65), end=' ')
            print('')


    def find_used_language(self):
        for c in self.regex:
            if (c not in self.used_language) and (c not in ['(', '|', ')', '*']):
                self.used_language.append(c)


    def create_table(self):

        self.find_used_language()


        for i in range(self.nfa.Q):
            s = state(i, i)
            self.states.append(s)
            self.add_empty_row_to_table()

        for current_state in self.states:
            for i, char in enumerate(self.used_language):
                for transition in self.nfa.transitions:
                    if transition.start in current_state.q and char == transition.regex:
                        if self.table[current_state.name][i] == 61:
                            thirdD = []
                            thirdD.append(transition.end)
                            self.table[current_state.name][i] = thirdD
                        else:
                            self.table[current_state.name][i].append(transition.end)

            for i, thirdD in enumerate(self.table[current_state.name]):
                find = 0
                for control_state in self.states:
                    if thirdD == control_state.q:
                        self.table[current_state.name][i] = control_state.name
                        find = 1
                        break
                    elif thirdD == 61:
                        find = 1
                        break

                if find == 0:
                    if any([x in self.accept for x in thirdD]):
                        self.accept.append(self.number_of_states)
                    new_state = state(thirdD, self.number_of_states)
                    self.states.append(new_state)
                    self.add_empty_row_to_table()
                    self.table[current_state.name][i] = self.number_of_states
                    self.number_of_states = self.number_of_states + 1




