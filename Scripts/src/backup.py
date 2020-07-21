
# def brutalForceSearch(currentState,step):
#     """
#     Search all the possible successor state given the currentState
#     :param currentState
#     :param step: The number of steps required to reach currentState
#     :return: currentState
#     """
#
#     global stateList
#     stateList.append(currentState)
#     plot(currentState)
#
#     if currentState.step >= step:
#         return currentState
#
#
#     for nodeI in range(currentState.len()):
#         for nodeJ in range(nodeI + 1,currentState.len()):
#             lst = []
#             for color in currentState.colorList():
#                 nextState = copy.deepcopy(currentState)
#                 if nextState.connect_node(nodeI,nodeJ,color):
#                     isomorphic_state = nextState.hasIsomorphic(stateList)
#                     if isomorphic_state == None:
#                         lst.append(nextState)
#                         brutalForceSearch(nextState, step)
#                     else:
#                         lst.append(isomorphic_state)
#             if lst:
#                 currentState.add_successor_states(lst)
#
#     for nodeI in range(currentState.len()):
#         lst = []
#         for color in currentState.colorList():
#             nextState = copy.deepcopy(currentState)
#             nextState.add_node(nodeI, color)
#             isomorphic_state = nextState.hasIsomorphic(stateList)
#             if isomorphic_state == None:
#                 lst.append(nextState)
#                 brutalForceSearch(nextState, step)
#             else:
#                 lst.append(isomorphic_state)
#         if lst:
#             currentState.add_successor_states(lst)
#
#     lst = []
#     for color in currentState.colorList():
#         nextState = copy.deepcopy(currentState)
#         nextState.add_twoNodes(color)
#         isomorphic_state = nextState.hasIsomorphic(stateList)
#         if isomorphic_state == None:
#             lst.append(nextState)
#             brutalForceSearch(nextState,step)
#         else:
#             lst.append(isomorphic_state)
#     if lst:
#         currentState.add_successor_states(lst)
#
#     return currentState
