from reg2nfa import formal_nfa,transition
from graphviz import Digraph
import time
class FsmDrawer:
#statemanager içinde kullanmak için regex parametresi eklenmeli. 
# self.nfa = regex açılmalı

    def __init__(self): 
        # self.nfa = regex
        self.nfa = formal_nfa("(a|b)*aba")
        self.createRef()
        

    def createRef(self):
        self.f = Digraph("FSM","FSMtext.txt")
        self.f.attr("node" , shape = "doublecircle")
        self.f.attr(rankdir = "LR", size = "12")
        self.f.node(str(self.nfa.accept))

    def drawFsm(self,fsmStart,fsmNext,fsmLabel):
        self.f.attr("node" ,shape = "circle")
        self.f.edge(fsmStart,fsmNext,label = fsmLabel)

    def drawFsmColored(self,fsmStart,fsmNext,fsmLabel):
        self.f.attr("node",shape = "circle")
        self.f.edge(fsmStart,fsmNext,fontcolor = "blue",label = fsmLabel)
  

    def click(self,char,first):
        for a in self.nfa.transitions:
            if((str(a.regex) == char) & (str(a.start) == first) ):
                self.drawFsmColored(str(a.start),str(a.end),str(a.regex))
            else:
                self.drawFsm(str(a.start),str(a.end),str(a.regex))  
        self.f.view()
        self.clearRef()
    
    def clearRef(self):
        time.sleep(1)
        self.f.clear()
        self.createRef()

# Aşağıdaki liste içinde olanlar dinamik olarak gelmeli
listText = ["a","b","a","a","b","a"]
listFirst = ["1","2","3","1","2","3"]
z = FsmDrawer()
for a in range(6):
    char = listText[a]
    first = listFirst[a]
    z.click(char, first)
      
      
        







    

