from mesa import Agent


class TreeCell(Agent):
    """
    A tree cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Unelectrified", "Transition", or "Electrified"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """
    def __init__(self, pos, model):
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Unelectrified"

    def step(self):
        """
        If a member is has excess energy, sell it to unelectrified neighbors.
        """
        if self.condition == "Transition":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if neighbor.condition == "Unelectrified":
                    neighbor.condition = "Transition"
            self.condition = "Electrified"

    def get_pos(self):
        return self.pos
