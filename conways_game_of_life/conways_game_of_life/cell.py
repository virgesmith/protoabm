from mesa import Agent


class Cell(Agent):
    """Represents a single cell in the simulation."""

    DEAD = 0
    BORN = 1

    def __init__(self, pos, model, init_state=DEAD):
        """
        Create a cell, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        self.age = init_state
        # self.state = init_state
        self._nextAge = None

    @property
    def isAlive(self):
        return self.age != self.DEAD

    @property
    def neighbors(self):
        return self.model.grid.neighbor_iter((self.x, self.y), True)

    def step(self):
        """
        Compute if the cell will be dead or alive at the next tick.  This is
        based on the number of alive or dead neighbors.  The state is not
        changed here, but is just computed and stored in self._nextAge,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        """

        # Get the neighbors and apply the rules on whether to be alive or dead
        # at the next tick.
        live_neighbors = sum(neighbor.isAlive for neighbor in self.neighbors)

        # Assume nextState is unchanged, unless changed below.
        self._nextAge = self.age + 1
        if self.isAlive:
            # alive -> dead
            if live_neighbors < self.model.min_survival_neighbours or live_neighbors > self.model.max_survival_neighbours:
                self._nextAge = self.DEAD
            # alive -> alive
            else:
                self._nextAge = self.age + 1
        else:
            # dead -> alive
            if live_neighbors >= self.model.min_birth_neighbours and live_neighbors <= self.model.max_birth_neighbours:
                self._nextAge = self.BORN
            # dead -> dead
            else:
                self._nextAge = self.DEAD

    def __str__(self):
        return "%d,%d: %d" % (self.x, self.y, self.age)

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.age = self._nextAge
