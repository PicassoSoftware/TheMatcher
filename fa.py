import reg2nfa
import nfa2dfa

class FA:
    def __init__(self, regex):
        self.__dfa = nfa2dfa.formal_dfa(regex)
        self.__nfa = reg2nfa.formal_nfa(regex)
        self.DFA_NumberOfStates = self.__dfa.number_of_states
        self.NFA_NumberOfStates = self.__nfa.Q
        self.DFA_Transitions = self.__dfa.transitions_for_search
        self.NFA_Transitions = self.__nfa.transitions
        self.DFA_Start = self.__nfa.start
        self.NFA_Start = self.__nfa.start
        self.DFA_Accept = self.__nfa.accept
        self.NFA_Accept = self.__nfa.accept
        self.Used_Alphabet = self.__dfa.used_language