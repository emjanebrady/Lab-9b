# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:05:59 2024

@author: emjan
"""

#Emma Brady

from numpy import random


class Agent:
    def __init__(self, world):
        self.world = world
        self.location = None

    def move(self):
        vacancies = self.world.find_vacant(return_all=True)
        for patch in vacancies:
            if self.location is None or self.world.grid[self.location] != self:
                continue
            self.world.grid[self.location] = None
            self.location = patch
            self.world.grid[patch] = self
            return

class World:
    def __init__(self, world_size, num_agents):
        assert world_size[0] * world_size[1] > num_agents, 'Grid too small for number of agents.'
        self.grid = self.build_grid(world_size)
        self.agents = [Agent(self) for _ in range(num_agents)]
        self.init_world()

    def build_grid(self, world_size):
        locations = [(i, j) for i in range(world_size[0]) for j in range(world_size[1])]
        return {l: None for l in locations}

    def init_world(self):
        for agent in self.agents:
            loc = self.find_vacant()
            self.grid[loc] = agent
            agent.location = loc

    def find_vacant(self, return_all=False):
        empties = [loc for loc, occupant in self.grid.items() if occupant is None]
        if return_all:
            return empties
        else:
            return random.choice(empties) if empties else None

    def run(self, max_iter):
        for _ in range(max_iter):
            for agent in self.agents:
                agent.move()


# Set parameters
world_size = (5, 5)
num_agents = 5
max_iter = 10

# Initialize and run simulation
world = World(world_size, num_agents)
world.run(max_iter)