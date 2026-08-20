# 1 is the sequential workflow
from langgraph.graph import START, END, StateGraph
from typing import TypedDict

# define state

class TemperatureState(TypedDict):
    temp_celsius : float
    temp_fahrenheit : float
    
# define graph

graph = StateGraph(TemperatureState)

# func for conversion
def convert_temp(state: TemperatureState) -> TemperatureState:  
    celsius = state['temp_celsius']
    # convert
    fahrenheit = (celsius*9/5) + 32
    state['temp_fahrenheit'] = round(fahrenheit,2) # 2 means first 2 digit after . decimal
    return state



# add nodes
# start and end are the dummy node no neeed to add seperately langgraph add them by it self
graph.add_node('convert_temp', convert_temp)
# add edges
graph.add_edge(START, "convert_temp")
# 2nd edge
graph.add_edge("convert_temp", END)


#  compile the graph

workflow = graph.compile()


degree =  float(input("enter the degree which you want to convert: "))

# now execution
initial_state= {'temp_celsius': degree}
final_state = workflow.invoke(initial_state)

print(final_state)




#  for to visualize the graph use 

from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())

from IPython.display import display, Image
display(Image(workflow.get_graph().draw_mermaid_png()))