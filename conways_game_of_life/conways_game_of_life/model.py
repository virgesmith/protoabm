from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector

from .cell import Cell


def get_num_gen1(model):
    #print(len(model.schedule.agents), len([a.age for a in model.schedule.agents if a.age==1]))
    return len([a.age for a in model.schedule.agents if a.age==1])

def get_num_gen2(model):
    return len([a.age for a in model.schedule.agents if a.age==2])

def get_num_gen3(model):
    return len([a.age for a in model.schedule.agents if a.age==3])

def get_num_gen4(model):
    return len([a.age for a in model.schedule.agents if a.age==4])

def get_num_gen5(model):
    return len([a.age for a in model.schedule.agents if a.age==5])

def get_num_gen6(model):
    return len([a.age for a in model.schedule.agents if a.age==6])

def get_num_gen7plus(model):
    return len([a.age for a in model.schedule.agents if a.age>=7])


class ConwaysGameOfLife(Model):
    # this ends up in the "About" menu
    """
    Represents the 2-dimensional array of cells in Conway's Game of Life, colour-coded according to age. 
    Source code at https://github.com/virgesmith/protoabm
    """

    def __init__(self, height, width, initial_proportion, min_survival_neighbours, max_survival_neighbours, min_birth_neighbours, max_birth_neighbours):
        """
        Create a new playing area of (height, width) cells.
        """
        self.initial_proportion = initial_proportion

        self.min_survival_neighbours = min_survival_neighbours
        self.max_survival_neighbours = max_survival_neighbours
        self.min_birth_neighbours = min_birth_neighbours
        self.max_birth_neighbours = max_birth_neighbours

        self.log = [] 
        if self.min_survival_neighbours > self.max_survival_neighbours:
          self.log.append("ERROR: Survival neighbours min/max values (%d/%d) are invalid" % (self.min_survival_neighbours, self.max_survival_neighbours))
        if self.min_birth_neighbours > self.max_birth_neighbours:
          self.log.append("ERROR: Birth neighbours min/max values (%d/%d) are invalid" % (min_birth_neighbours, max_birth_neighbours ))
        
        self.datacollector = DataCollector(
            model_reporters={
                "1st Gen": get_num_gen1,
                "2nd Gen": get_num_gen2,
                "3rd Gen": get_num_gen3,
                "4th Gen": get_num_gen4,
                "5th Gen": get_num_gen5,
                "6th Gen": get_num_gen6,
                "7th+ Gen": get_num_gen7plus,
            }
        )


        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        self.schedule = SimultaneousActivation(self)

        # Use a simple grid, where edges wrap around.
        self.grid = Grid(height, width, torus=True)

        # Place a cell at each location, with some initialized to
        # ALIVE and some to DEAD.
        for (contents, x, y) in self.grid.coord_iter():
            cell = Cell((x, y), self)
            if self.random.random() < self.initial_proportion:
                cell.age = cell.BORN
            self.grid.place_agent(cell, (x, y))
            self.schedule.add(cell)

        self.running = True

    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        self.schedule.step()
        self.datacollector.collect(self)