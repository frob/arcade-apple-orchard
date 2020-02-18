"""
Apple Orchard Main game file.

This file contains the main file for the apple orchard game.
"""
import arcade
from modules.test_module import test_print

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Apple Orchard Game"


class AppleOrcardGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        print(test_print())
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.text_angle = 0

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear the
        # screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # start_x and start_y make the start point for the text. We draw a dot
        # to make it easy too see the text in relation to its start x and y.
        start_x = 50
        start_y = 450
        arcade.draw_text(
            "Hello World",
            start_x,
            start_y,
            arcade.color.WHITE,
            24
        )



def main():
    AppleOrcardGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
