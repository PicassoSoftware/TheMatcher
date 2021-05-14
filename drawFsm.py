from graphviz import Digraph
import time
from showFsm import Window

class FsmDrawer():
    def __init__(self,formalDefinition): 
        self.formalDefinition = formalDefinition
        self.createReference()
       
    
    def createReference(self):
        self.fsm = Digraph("FSM","FSMtext.txt",format="svg")
        self.fsm.attr("node" , shape = "doublecircle") #fontsize can be resize
        self.fsm.attr(rankdir = "LR")
        self.fsm.node(str(self.formalDefinition.accept))
        self.img = Window()
        print(str(self.formalDefinition.accept))

    def drawFsm(self,fsmStart,fsmNext,fsmLabel):
        self.fsm.attr("node" ,shape = "circle")
        self.fsm.edge(fsmStart,fsmNext,label = fsmLabel)

    def drawFsmColored(self,fsmStart,fsmNext,fsmLabel):
        self.fsm.attr("node",shape = "circle")
        self.fsm.edge(fsmStart,fsmNext,fontcolor = "red",label = fsmLabel)
  

    def click(self,char,first):        
        for a in self.formalDefinition.transitions:
            if((str(a.regex) == char) & (str(a.start) == first) ):
                self.drawFsmColored(str(a.start),str(a.end),str(a.regex))
            else:
                self.drawFsm(str(a.start),str(a.end),str(a.regex))  

        self.fsm.render(view=False)


        
        self.clearReference()
        
    def clearReference(self):
        time.sleep(1)
        self.fsm.clear()
        self.createReference()
        

      








    

