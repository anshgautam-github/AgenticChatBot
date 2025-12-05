from langgraph.graph import StateGraph

class GraphBuilder:
    def __init__(self,model):    #This graphBuilder is being triggered when the frontedn and llm is loaded
        self.llm=model
        self.graph_builder=StateGraph(State)
         