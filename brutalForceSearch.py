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
    currentState.plot(print_index)

def brutalForceSearch(currentState,step):
    """
    :param currentState:currentNode
    :param step:
    :return:
    """
    global stateList
    stateList.append(currentState)
    plot(currentState)

    if currentState.step >= step:
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
            if lst:
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
        if lst:
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
    if lst:
        currentState.add_successor_states(lst)

    return currentState


def brutalForceSearchWithLimit(currentState,step,limit):
    """
    :param currentState:currentNode
    :param step:
    :return:
    """
    if step >= 4 * (limit + 1) - 6: return 4 * (limit + 1) - 6

    global stateList
    stateList.append(currentState)
    # plot(currentState)


    minNumber = float("inf")

    for nodeI in range(currentState.len()):
        for nodeJ in range(nodeI + 1,currentState.len()):
            lst = []
            maxNumber1 = float("-inf")
            for color in currentState.colorList():
                nextState = copy.deepcopy(currentState)
                if nextState.connect_node(nodeI,nodeJ,color):
                    nextState.update_max_path()
                    if nextState.maxLength < limit:
                        isomorphic_state = nextState.hasIsomorphic(stateList)
                        if isomorphic_state == None:
                            lst.append(nextState)
                            brutalForceSearchWithLimit(nextState, step+1, limit)
                        else:
                            lst.append(isomorphic_state)
                    else:
                        maxNumber1 = max(maxNumber1,nextState.step)
            if maxNumber1 != float("-inf"):
                minNumber = min(maxNumber1,minNumber)
            if lst:
                currentState.add_successor_states(lst)

    for nodeI in range(currentState.len()):
        lst = []
        maxNumber2 = float("-inf")
        for color in currentState.colorList():
            nextState = copy.deepcopy(currentState)
            nextState.add_node(nodeI, color)
            nextState.update_max_path()
            if nextState.maxLength < limit:
                isomorphic_state = nextState.hasIsomorphic(stateList)
                if isomorphic_state == None:
                    lst.append(nextState)
                    brutalForceSearchWithLimit(nextState, step+1, limit)
                else:
                    lst.append(isomorphic_state)
            else:
                maxNumber2 = max(maxNumber2, nextState.step)
        if maxNumber2 != float("-inf"):
            minNumber = min(maxNumber2, minNumber)
        if lst:
            currentState.add_successor_states(lst)

    # lst = []
    # maxNumber3 = float("-inf")
    # for color in currentState.colorList():
    #     nextState = copy.deepcopy(currentState)
    #     nextState.add_twoNodes(color)
    #     nextState.update_max_path()
    #     if nextState.maxLength < limit:
    #         isomorphic_state = nextState.hasIsomorphic(stateList)
    #         if isomorphic_state == None:
    #             lst.append(nextState)
    #             brutalForceSearchWithLimit(nextState,limit)
    #         else:
    #             lst.append(isomorphic_state)
    #     else:
    #         maxNumber3 = max(maxNumber3,nextState.step)
    #
    # if maxNumber3 != float("-inf"):
    #     minNumber = min(maxNumber3, minNumber)
    #
    # if lst:
    #     currentState.add_successor_states(lst)

    return minNumber

# colors = ["red","blue"]
# initialState = state(initial_graph.startGraph(),colors,1)
# currentState = brutalForceSearch(initialState,4)
#
# for oneState in stateList:
#     oneState.update_max_path()
#     print(oneState.maxLength)
#
# with open("pickle3.dat", "wb") as f:
#     pickle.dump(currentState, f)
#
# print(time.time()-start_time)
