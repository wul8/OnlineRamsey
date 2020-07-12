import olRamseyNumber
import initial_graph
import state
import brutalForceSearch

colors = ["red","blue"]
initialState = state.state(initial_graph.startGraph(),colors,1)
a = brutalForceSearch.brutalForceSearchWithLimit(initialState,0,2)
print(a)