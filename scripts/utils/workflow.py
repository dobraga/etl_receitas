from multiprocessing import Semaphore
from multiprocessing.pool import Pool

class Workflow():
    def __init__(self, steps, runs):
        self.steps = steps
        self.runs = runs
        
        