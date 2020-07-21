import olRamseyNumber
import initial_graph
import state
import brutalForceSearch

colors = ["red","blue"]
initialState = state.state(initial_graph.startGraph(),colors,1)
limit = 2
bound = 4 * (limit + 1) - 6
a = brutalForceSearch.brutalForceSearchWithLimit(initialState, 0, limit, bound)
print("result",a)