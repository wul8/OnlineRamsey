from state import state
import copy
import pickle
import time

startTime = time.time()
with open("pickle1.dat", "rb") as f:
    currentState = pickle.load(f)


currentState.plot(1)
currentState.successorStates[1][0].plot(1)
#print(currentState.get_online_ramsey_number(3))

