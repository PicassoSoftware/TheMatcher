import reg2nfa

regex = "sema"

nfa = reg2nfa.formal_nfa(regex)


empty = 61
used_language = []
states = []
table = []
number_of_states =nfa.Q

for c in regex:
    if (c not in used_language) and (c not in ['(', '|', ')', '*']):
        used_language.append(c)

class state:
    def __init__(self, q, name):
        self.name = name
        if type(q) == int :
            self.q = [q]
        else :
            self.q = q

      
        """endsleri tutuyor"""


def  add_empty_row_to_table():

    row = []
    for i in range (len(used_language)):

        row.append(empty)

    table.append(row)


for i in range(nfa.Q):
    s =state(i,i)
    states.append(s)
    add_empty_row_to_table()

for current_state in states:
    for i, char in enumerate(used_language):
        for transition in nfa.transitions:
            if transition.start in current_state.q and char == transition.regex:
                if table[current_state.name][i] == 61:
                    thirdD = []
                    thirdD.append(transition.end)
                    table[current_state.name][i] = thirdD
                else:
                    table[current_state.name][i].append(transition.end)

    for i, thirdD in enumerate(table[current_state.name]):
        find =0
        for control_state in states :
            if thirdD==control_state.q:
                table[current_state.name][i]=control_state.name
                find=1
                break
            elif thirdD == 61 :
                find = 1
                break

        if find == 0 :
            new_state = state(thirdD,number_of_states)
            states.append(new_state)
            add_empty_row_to_table()
            table[current_state.name][i] = number_of_states
            number_of_states = number_of_states + 1

def print_table():
    print('  |',end=' ')
    for char in used_language:
        print(char,end=' ')
    print('')
    for i, row in enumerate(table) :
        print(chr(i+65),end =' | ')

        for unnamed_states in row:
            print(chr(unnamed_states + 65), end=' ')
        print('')

print_table()
