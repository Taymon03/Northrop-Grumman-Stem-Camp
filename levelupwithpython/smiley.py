import arcade

# Drawing a smiley face

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions, (width, height, title)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Smiley")
#open window set title
arcade.set_background_color(arcade.color.BLUE)
arcade.start_render()
x=300
y=300
radius=200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)
#Make left eye

arcade.finish_render()
arcade.run()
