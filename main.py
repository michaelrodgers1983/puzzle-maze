tiles.set_tilemap(tilemap("""
    level2
"""))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . 3 3 3 . . . . . . . . . . . . 
            3 3 . 3 3 . . . . . . . . 3 . . 
            3 . . 3 3 3 3 3 3 3 3 3 3 3 . . 
            3 . . 3 . . . . . . . . 3 3 . . 
            3 . . 3 . . . . . . . . 3 3 . . 
            3 . . 3 . . . . 3 3 3 3 3 3 . . 
            3 3 . 3 . . . 3 3 . . 3 3 3 . . 
            . 3 . 3 . 3 3 . . . . 3 . 3 . . 
            . 3 . 3 3 3 . . . . . 3 . 3 . . 
            . 3 3 3 3 . . . . . . 3 3 3 . . 
            . . 3 3 . . . 3 . . 3 3 3 3 . . 
            . . . 3 3 3 . 3 3 3 3 3 3 . . . 
            . . . . . 3 3 3 3 3 3 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)