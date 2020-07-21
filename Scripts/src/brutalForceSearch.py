from state import state
import copy

print_index = 0
# The state that has been visited. Used for check isomorphism
stateList = []

def plot(currentState):
    """used for debug. plot currentState image and print
    on the console the number of unisomorphic graph has searched """

    global print_index
    print(print_index)
    print_index = print_index + 1
    #currentState.plot(print_index)


def brutalForceSearchWithLimit(currentState, step, limit, minNumber):
    """
    Search all the possible successor state given the currentState
    :param currentState
    :param step: The number of steps required to reach currentState
    :return: currentState
    """
    global stateList         # Store
    if step >= minNumber:
        return minNumber
    stateList.append(currentState)

    # Connect Two existing node.
    for nodeI in range(currentState.len()):
        for nodeJ in range(nodeI + 1,currentState.len()):

            # Check if two node is connected. If so, go next.
            if currentState.has_edge(nodeI,nodeJ): break
            maxNumber1 = float("-inf")

            # The painter now paints color on new edge
            for color in currentState.colorList():
                nextState = copy.deepcopy(currentState)
                if nextState.connect_node(nodeI,nodeJ,color):
                    nextState.update_max_path()
                    if nextState.maxLength < limit:
                        isomorphic_state = nextState.hasIsomorphic(stateList)
                        if isomorphic_state == None:
                            maxNumber1 = max(maxNumber1,brutalForceSearchWithLimit(nextState, step+1, limit, minNumber))
                        # if the new state is not isomoprhic, return corresponding minStep
                        else:
                            maxNumber1 = max(maxNumber1,isomorphic_state.minStep)

                    else:
                        isomorphic_state = nextState.hasIsomorphic(stateList)
                        if isomorphic_state == None:
                            #plot(nextState)
                            #print("max Number:", maxNumber1)
                            stateList.append(nextState)
                        maxNumber1 = max(maxNumber1, step + 1)

            if maxNumber1 != float("-inf"):
                minNumber = min(maxNumber1,minNumber)
                #print("min Number", minNumber)


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
                ### if the new state is not isomoprhic, return corresponding minStep
                else:
                    maxNumber2 = max(maxNumber2, isomorphic_state.minStep)
            else:
                isomorphic_state = nextState.hasIsomorphic(stateList)
                if isomorphic_state == None:
                    #print("max Number:",maxNumber2)
                    #plot(nextState)
                    stateList.append(nextState)
                maxNumber2 = max(maxNumber2, step + 1)

        if maxNumber2 != float("-inf"):
            minNumber = min(maxNumber2, minNumber)
            #print("minNumber",minNumber)

    currentState.updateSuccessorMin(minNumber)
    return minNumber






