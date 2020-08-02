
def _colour(age):
    return 

_lookup = [ "#FFFFFF", "#00FFFF", "#0000FF", "#FF00FF", "#FF0000", "#FFFF00", "#00FF00", "#000000"]

def portrayCell(cell):
    """
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the cell in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    """
    assert cell is not None
    return {
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Filled": "true",
        "Layer": 0,
        "x": cell.x,
        "y": cell.y,
        "Color": _lookup[min(cell.age,7)],
    }
