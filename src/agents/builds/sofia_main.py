from langgraph.graph import END, START, StateGraph, MessagesState
from src.utils.llms.openAI import gpt4_mini
from src.utils.misc.draw_graph import save_graph_as_jpeg

def call_gpt(state: MessagesState):
    messages = state['messages']
    response = gpt4_mini.invoke(messages[-1].content)
    return {"messages": [response]}
    

def sofia_main_graph():
    graph = StateGraph(MessagesState)
    graph.add_node("gpt", call_gpt)
    graph.add_edge(START, "gpt")
    graph.add_edge("gpt", END)
    compiled = graph.compile()
    save_graph_as_jpeg(compiled, "graphs_images")

    return compiled
