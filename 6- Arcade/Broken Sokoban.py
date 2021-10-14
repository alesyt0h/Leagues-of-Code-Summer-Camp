import arcade

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 64
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)


HEIGHT = 9
WIDTH = 18

SCREEN_WIDTH = SPRITE_SIZE * WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * HEIGHT
SCREEN_TITLE = "Sokoban"

FLOOR = " "
WALL = "#"
PLAYER = "@"
BOX = "$"
TARGET = "."
BOX_ON_TARGET = "*"
PLAYER_ON_TARGET = "+"

SPRITES = {
    FLOOR: "ground_03.png",
    WALL: "block_03.png",
    PLAYER: "player_05.png",
    BOX: "crate_23.png",
    TARGET: "environment_04.png",
    BOX_ON_TARGET: "crate_23.png",
    PLAYER_ON_TARGET: "player_05.png",
}

state = [
[" "," "," "," ","#","#","#","#","#"," "," "," "," "," "," "," "," "," "," "], 
[" "," "," "," ","#"," "," "," ","#"," "," "," "," "," "," "," "," "," "," "], 
[" "," "," "," ","#","$"," "," ","#"," "," "," "," "," "," "," "," "," "," "], 
[" "," ","#","#","#"," "," ","$","#","#"," "," "," "," "," "," "," "," "," "], 
[" "," ","#"," "," ","$"," ","$"," ","#"," "," "," "," "," "," "," "," "," "], 
["#","#","#"," ","#"," ","#","#"," ","#"," "," "," ","#","#","#","#","#","#"], 
["#"," "," "," ","#"," ","#","#"," ","#","#","#","#","#"," "," ",".",".","#"], 
["#"," ","$"," "," ","$"," "," "," "," "," "," "," "," "," "," ",".",".","#"], 
["#","#","#","#","#"," ","#","#","#"," ","#","@","#","#"," "," ",".",".","#"], 
[" "," "," "," ","#"," "," "," "," "," ","#","#","#","#","#","#","#","#","#"], 
[" "," "," "," ","#","#","#","#","#","#","#"," "," "," "," "," "," "," "," "],
]


class LevelWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.GRAY)

    def create_sprite(self, cell, i, j):
        filepath = "sprites/" + SPRITES[cell]
        sprite = arcade.Sprite(filepath, SPRITE_SCALING)
        sprite.center_x = (j + i) * SPRITE_SIZE - SPRITE_SIZE // 2
        sprite.center_y = SCREEN_HEIGHT - SPRITE_SIZE // 2 - i * SPRITE_SIZE
        return sprite

    def on_draw(self):
        arcade.start_render()
        sprites = arcade.SpriteList()
        for i in range(HEIGHT):
            for j in range(WIDTH):
                cell = state[i][j]
                sprite = self.create_sprite(cell,i,j)
                sprites.append(sprite)
                # if cell == wall:
                #     filepath = "sprites/" + sprites[wall]
                #     sprite = arcade.Sprite(filepath,sprite_scaling)
                #     sprite.center_x = j * sprite_size - sprite_size // 2
                #     sprite.center_y = screen_height - sprite_size // 2 - i * sprite_size
                    # sprites.append(sprite)
        sprites.draw()

    
window = LevelWindow(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()
