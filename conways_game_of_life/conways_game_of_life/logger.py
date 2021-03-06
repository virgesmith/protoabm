from mesa.visualization.modules.TextVisualization import TextElement

class LoggerElement(TextElement):
  def __init__(self):
    '''
    Create a new text logger element.
    '''
      
  def render(self, model):
    """ log must be a string list """
    return "<pre>" + "\n".join(model.log) + "</pre>"