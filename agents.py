import random

def getAgent():
    agents = ['chrome','opera','firefox']
    return agents[random.randint(0,2)]
