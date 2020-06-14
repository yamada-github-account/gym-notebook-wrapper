import os

from gym import Wrapper
from IPython import display
import matplotlib.pyplot as plt
from pyvirtualdisplay import Display


class NotebookWrapper(Wrapper):
    """
    Wrapper for running/rendering OpenAI gym environment on Notebook
    """
    def __init__(self,env,size=(1024, 768)):
        """
        Wrapping environment for Notebook

        env : gym.Env
            Environment to be wrapped
        size : array-like, optional
            Virtual display size, whose default is (1024,768)
        """
        super().__init__(env)

        self._img = None

        self._display = None
        # To avoid starting multiple virtual display
        if not os.getenv("DISPLAY",None):
            self._display = Display(visible=0, size=size)
            self._display.start()

    def render(self,mode=None):
        """
        Render environment on Notebook
        """
        display.clear_output(wait=True)
        if self._img is None:
            self._img = plt.imshow(self.env.render(mode='rgb_array'))
        else:
            self._img.set_data(self.env.render(mode='rgb_array'))

        plt.axis('off')
        display.display(plt.gcf())
