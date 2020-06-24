from state import state
import initial_graph
import copy
import pickle
import time

print_index = 0
stateList = []
start_time = time.time()

def plot(currentState):
    global print_index
    print(print_index)
    print_index = print_index + 1
#    currentState.plot(print_index)

def brutalForceSearch(currentState,step):
    """
    :param currentState:currentNode
    :param step:
    :return:
    """
    global stateList
    stateList.append(currentState)
    plot(currentState)

    if currentState.get_step_number() >= step:
        return currentState


    for nodeI in range(currentState.len()):
        for nodeJ in range(nodeI + 1,currentState.len()):
            lst = []
            for color in currentState.colorList():
                nextState = copy.deepcopy(currentState)
                if nextState.connect_node(nodeI,nodeJ,color):
                    isomorphic_state = nextState.hasIsomorphic(stateList)
                    if isomorphic_state == None:
                        lst.append(nextState)
                        brutalForceSearch(nextState, step)
                    else:
                        lst.append(isomorphic_state)
            currentState.add_successor_states(lst)

    for nodeI in range(currentState.len()):
        lst = []
        for color in currentState.colorList():
            nextState = copy.deepcopy(currentState)
            nextState.add_node(nodeI, color)
            isomorphic_state = nextState.hasIsomorphic(stateList)
            if isomorphic_state == None:
                lst.append(nextState)
                brutalForceSearch(nextState, step)
            else:
                lst.append(isomorphic_state)
        currentState.add_successor_states(lst)

    lst = []
    for color in currentState.colorList():
        nextState = copy.deepcopy(currentState)
        nextState.add_twoNodes(color)
        isomorphic_state = nextState.hasIsomorphic(stateList)
        if isomorphic_state == None:
            lst.append(nextState)
            brutalForceSearch(nextState,step)
        else:
            lst.append(isomorphic_state)
    currentState.add_successor_states(lst)

    return currentState

colors = ["red","blue"]
initialState = state(initial_graph.startGraph(),colors,1)
currentState = brutalForceSearch(initialState,10)

for oneState in stateList:
    oneState.update_max_path()
    print(oneState.maxLength)

with open("pickle1.dat", "wb") as f:
    pickle.dump(currentState, f)

print(time.time()-start_time)
