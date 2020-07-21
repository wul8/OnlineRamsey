from state import state
import copy
import pickle
import time

def get_online_ramsey_number(number):
    if number <= 4:
        with open("../../data/pickle2.dat", "rb") as f:
            currentState = pickle.load(f)
        return str(currentState.get_online_ramsey_number(number))
    else:
        return "not in range"

