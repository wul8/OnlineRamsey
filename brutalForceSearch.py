from state import state
import initial_graph
import copy
import pickle
import time

print_index = 0
stateList = []
start_time = time.time()


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


def plot(currentState):
    global print_index
    print(print_index)
    print_index = print_index + 1
    currentState.plot(print_index)


def brutalForceSearchWithLimit(currentState, step, limit, minNumber):
    """
    :param currentState:currentNode
    :param step:
    :return:
    """
    if step >= minNumber:
        return minNumber

    global stateList
    stateList.append(currentState)
    plot(currentState)

    # Connect Two existing node.
    for nodeI in range(currentState.len()):
        for nodeJ in range(nodeI + 1,currentState.len()):
            if currentState.has_edge(nodeI,nodeJ): break
            maxNumber1 = float("-inf")
            ### The painter now paints color on new edge
            for color in currentState.colorList():
                nextState = copy.deepcopy(currentState)
                if nextState.connect_node(nodeI,nodeJ,color):
                    nextState.update_max_path()
                    if nextState.maxLength < limit:
                        isomorphic_state = nextState.hasIsomorphic(stateList)
                        if isomorphic_state == None:
                            maxNumber1 = max(maxNumber1,brutalForceSearchWithLimit(nextState, step+1, limit, minNumber))
                    else:
                        isomorphic_state = nextState.hasIsomorphic(stateList)
                        if isomorphic_state == None:
                            maxNumber1 = max(maxNumber1,step+1)
                            plot(nextState)
                            print("max Number:", maxNumber1)
                            stateList.append(nextState)

            if maxNumber1 != float("-inf"):
                minNumber = min(maxNumber1,minNumber)
                print("min Number", minNumber)


    # Draw a new node and connect it with the existing node
    for nodeI in range(currentState.len()):
        maxNumber2 = float("-inf")
        for color in currentState.colorList():
            nextState = copy.deepcopy(currentState)
            nextState.add_node(nodeI, color)
            nextState.update_max_path()
            if nextState.maxLength < limit:
                isomorphic_state = nextState.hasIsomorphic(stateList)
                if isomorphic_state == None:
                    maxNumber2 = max(maxNumber2,brutalForceSearchWithLimit(nextState, step+1, limit, minNumber))
            else:
                isomorphic_state = nextState.hasIsomorphic(stateList)
                if isomorphic_state == None:
                    maxNumber2 = max(maxNumber2, step+1)
                    print("max Number:",maxNumber2)
                    plot(nextState)
                    stateList.append(nextState)

        if maxNumber2 != float("-inf"):
            minNumber = min(maxNumber2, minNumber)
            print("minNumber",minNumber)

    return minNumber





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


