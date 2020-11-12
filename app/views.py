"""
This file contains all the view classes for this game.
"""
import arcade


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Main View", self.width/2, self.height/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = GameView(self.width, self.height)
        game_view.setup()
        self.window.show_view(game_view)


class GameView(arcade.View):
    """ Manage the 'game' view for our program. """

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_text("Game - press SPACE to advance", self.width/2, self.height/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, symbol, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if symbol == arcade.key.SPACE:
            game_over_view = GameOverView(self.width, self.height)
            self.window.show_view(game_over_view)


class GameOverView(arcade.View):
    """ Class to manage the game over view """

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over - press ESCAPE to advance", self.width/2, self.height/2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, symbol, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if symbol == arcade.key.ESCAPE:
            menu_view = MenuView(self.width, self.height)
            self.window.show_view(menu_view)
