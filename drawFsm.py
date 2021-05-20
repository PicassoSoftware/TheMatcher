from typing import Sized
from graphviz import Digraph
import time
from showFsm import Window

class FsmDrawer():
    def __init__(self,formalDefinition, label): 
        self.label = label
        self.formalDefinition = formalDefinition
        self.createReference()
       
    
    def createReference(self):
        self.fsm = Digraph("FSM","FSMtext.txt",format="svg")
        self.fsm.attr("node" , shape = "doublecircle",color="black",fontsize="10") #fontsize can be resize 
        self.fsm.attr(rankdir = "LR",bgcolor="transparent",size="9,9!")

        try:
            for item in self.formalDefinition.accept:
                self.fsm.node(str(item))
        except:
            self.fsm.node(str(self.formalDefinition.accept))
        self.img = Window(self.label)
        print(str(self.formalDefinition.accept))

    def drawFsm(self,fsmStart,fsmNext,fsmLabel):
        self.fsm.attr("node" ,shape = "circle",color="black",fontcolor = "black")
        self.fsm.edge(fsmStart,fsmNext,label = fsmLabel,color="blue",fontcolor = "blue")


    def drawFsmColored(self,fsmStart,fsmNext,fsmLabel):
        self.fsm.attr("node",shape = "circle",color="black",fontcolor = "black")
        self.fsm.edge(fsmStart,fsmNext,fontcolor = "red",label = fsmLabel,color="red")
  

    def click(self,char,first):       
        for a in self.formalDefinition.transitions:
            if((str(a.regex) == char) & (str(a.start) == first) ):
                self.drawFsmColored(str(a.start),str(a.end),str(a.regex))
            else:
                self.drawFsm(str(a.start),str(a.end),str(a.regex))  

        self.fsm.attr("node",shape="plaintext")      
        self.fsm.edge("",str(self.formalDefinition.start))
        
        self.fsm.render(view=False)
  
        self.clearReference()
        
    def clearReference(self):
        time.sleep(1)
        self.fsm.clear()
        self.createReference()
        

      








    

