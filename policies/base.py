from random import randint

class PolicyBase:
    def __init__(self, action_space):
        self.action_space = action_space
    
    def step(self, observation, frame = None):
        raise NotImplementedError

class RandomPolicy(PolicyBase):
    def step(self, observation, frame=None):
        return self.action_space.sample()
