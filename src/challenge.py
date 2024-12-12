from typing import Literal, List, Union
from langgraph.graph import END, START, StateGraph, MessagesState
from langchain_core.messages import HumanMessage
from pprint import pprint

from utils.misc.draw_graph import save_graph_as_jpeg

def node1(state: MessagesState):
    messages = state['messages']
    result = float(messages[-1].content) + 10
    pprint(state)
    return 

def edge_node1(state: MessagesState) -> Literal["node2", "node3"]:
    if state["messages"][-1] % 2 == 0:
        return "node2"
    else:
        return "node3"
    
def node2(state: MessagesState):
    messages = state['messages']
    messages[-1] *2
    return "node4" 

def node3(state: MessagesState):
    messages = state['messages']
    messages[-1] / 2
    return "node5"

def node4(state: MessagesState):
    messages = state['messages']
    messages[-1] - 2
    return "node5"

def node5(state: MessagesState):
    messages = state['messages']
    messages[-1] + 2
    return messages[-1]

def edge_node5(state: MessagesState) -> Literal["node6", "node7"]:
    if state["messages"][-1] >= 5 and state["messages"][-1] <= 15:
        return "node7"
    else:
        return "node6"

def node6(state: MessagesState):
    return state["messages"][-1]

def node7(state: MessagesState):
    return state["messages"][-1]

def challenge():
    graph = StateGraph(MessagesState)

    graph.add_node("node1", node1)
    graph.add_node("node2", node2)
    graph.add_node("node3", node3)
    graph.add_node("node4", node4)
    graph.add_node("node5", node5)
    graph.add_node("node6", node6)
    graph.add_node("node7", node7)

    graph.add_edge(START, 'node1')
    graph.add_conditional_edges('node1', edge_node1)
    graph.add_edge('node2', 'node4')
    graph.add_edge('node4', 'node5')
    graph.add_edge("node3", "node5")
    graph.add_conditional_edges("node5", edge_node5)
    graph.add_edge("node6", END)
    graph.add_edge("node7", END)


    compiled = graph.compile()
    return compiled

x = challenge()
final = x.invoke(
    {"messages": [HumanMessage(content="10")]}
)
