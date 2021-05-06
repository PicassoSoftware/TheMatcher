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

        """endsleri tutuyor"""


class formal_dfa:
    def __init__(self, regex):
        self.regex = regex
        self.nfa = reg2nfa.formal_nfa(regex)
        self.empty = 61
        self.used_language = []
        self.states = []
        self.table = []
        self.transitions_for_sm = []
        self.transitions_for_search = []
        self.number_of_states = self.nfa.Q
        self.create_table()

    def find_transitions(self):
        for start, row in enumerate(self.table):
            for regexnum,end in enumerate(row):

                t = transition(start,end,self.used_language[regexnum])
                self.transitions_for_sm.append(t)
                if end != self.empty:
                    self.transitions_for_search.append(t)


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
                    new_state = state(thirdD, number_of_states)
                    self.states.append(new_state)
                    self.add_empty_row_to_table()
                    self.table[current_state.name][i] = number_of_states
                    number_of_states = number_of_states + 1

