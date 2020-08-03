from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from .logger import LoggerElement
from .portrayal import portrayCell, cellColour
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
    "max_birth_neighbours": UserSettableParameter("slider", "Maximum neighbours for cell birth", 3, 0, 8, 1)
}   


# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, NX, NY, SIZE * NX, SIZE * NY)

chart_element = ChartModule(
  [
    {"Label": "1st Gen", "Color": cellColour(1)},
    {"Label": "2nd Gen", "Color": cellColour(2)},
    {"Label": "3rd Gen", "Color": cellColour(3)},
    {"Label": "4th Gen", "Color": cellColour(4)},
    {"Label": "5th Gen", "Color": cellColour(5)},
    {"Label": "6th Gen", "Color": cellColour(6)},
    {"Label": "7th+ Gen", "Color": cellColour(7)}
  ]
)

console = LoggerElement()

server = ModularServer(
    ConwaysGameOfLife, [canvas_element, chart_element, console], "Conway's Game of Life", model_params
)
