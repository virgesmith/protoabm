from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules.TextVisualization import TextElement

from .portrayal import portrayCell
from .model import ConwaysGameOfLife

# no of cells, and display size in pixels
NX = 100
NY = 100
SIZE = 5


model_params = {
    "height": NX, 
    "width": NY,
    "initial_proportion": UserSettableParameter(
        "slider",
        "Probability of initial alive state",
        0.1,
        0.0,
        1.0,
        0.01,
        description="The probability of a cell starting in an alive state."
    ),
    "min_survival_neighbours": UserSettableParameter("slider", "Minimum neighbours for survival", 2, 0, 8, 1),
    "max_survival_neighbours": UserSettableParameter("slider", "Maximum neighbours for survival", 3, 0, 8, 1),
    "min_birth_neighbours": UserSettableParameter("slider", "Minimum neighbours for cell birth", 3, 0, 8, 1),
    "max_birth_neighbours": UserSettableParameter("slider", "Maximum neighbours for cell birth", 3, 0, 8, 1),
    "logger": TextElement()
}   


# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, NX, NY, SIZE * NX, SIZE * NY)

server = ModularServer(
    ConwaysGameOfLife, [canvas_element], "Game of Life", model_params
)
