#graphviz import edilmediyse pip install graphviz yapılmadır. 
from graphviz import Digraph
import time
from showFsm import Window

class FsmDrawer():
    def __init__(self,formalDefinition, label): 
        self.label = label
        self.formalDefinition = formalDefinition
        self.createReference()
       
    
    def createReference(self):
        self.fsm = Digraph("FSM",format="svg",filename="fsm.txt")
        self.fsm.attr("node" , shape = "doublecircle",color="#fdfaf6",fontsize="10") #fontsize can be resize
        self.fsm.attr(rankdir = "LR",bgcolor="transparent",size="9,9!")

        try:
            for item in self.formalDefinition.accept:
                self.fsm.node(str(item), fontcolor = "#fdfaf6")
        except:
            self.fsm.node(str(self.formalDefinition.accept))
        self.img = Window(self.label)
        print(str(self.formalDefinition.accept))

    def drawFsm(self, fsmStart, fsmNext, fsmLabel):
        self.fsm.attr("node", shape="circle", color="#fdfaf6", fontcolor="#fdfaf6")
        self.fsm.edge(fsmStart, fsmNext, label=fsmLabel, color="#fdfaf6", fontcolor="#fdfaf6")

    def drawFsmColored(self, fsmStart, fsmNext, fsmLabel):
        self.fsm.attr("node", shape="circle", color="#fdfaf6", fontcolor="#fdfaf6")
        self.fsm.edge(fsmStart, fsmNext, fontcolor="#fb743e", label=fsmLabel, color="#fb743e")
  

    def click(self,char,first):       
        for a in self.formalDefinition.transitions:
            if((str(a.regex) == char) & (str(a.start) == first) ):
                self.drawFsmColored(str(a.start),str(a.end),str(a.regex))
            else:
                self.drawFsm(str(a.start),str(a.end),str(a.regex))  

        self.fsm.attr("node",shape="plaintext", color = "#fdfaf6")
        self.fsm.edge("",str(self.formalDefinition.start),color = "#fdfaf6")
        
        self.fsm.render(view=False)
  
        self.clearReference()
        
    def clearReference(self):
        time.sleep(0,8)
        self.fsm.clear()
        self.createReference()
