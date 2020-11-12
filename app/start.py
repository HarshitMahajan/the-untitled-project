"""
This file is the starting point of The Untitled Project.
"""
import arcade
import views

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snakes and Ladders"


class SnakesAndLadders(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """ Initilizes the underlying arcade window with given width, height and titile. """
        super().__init__(width, height, title)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Sprites and sprite lists go here.

    def run(self):
        """ Start the game loop. """
        # Create the menu view and show it.
        menu_view = views.MenuView(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.show_view(menu_view)
        arcade.run()


def main():
    """ Startup """
    window = SnakesAndLadders(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.run()


if __name__ == "__main__":
    main()
