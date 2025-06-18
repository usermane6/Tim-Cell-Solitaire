import pygame as pg
import sys
pg.init()

deck_image : pg.Surface = pg.image.load("assets/base_deck.png")
card_back  : pg.Surface = pg.image.load("assets/card_back.png")
CARD_WIDTH  : int = 16 * 4
CARD_HEIGHT : int = 16 * 6

def get_card_image( suit : int, value : int ) -> pg.Surface :
    y_pos : int = (suit - 1) * 16 * 6
    x_pos : int = (value - 1) * 16 * 4
    image_sub_rect :  pg.Rect = pg.Rect(x_pos, y_pos, CARD_WIDTH, CARD_HEIGHT)
    return deck_image.subsurface(image_sub_rect)

class Card(pg.sprite.Sprite): 
    group = pg.sprite.Group()

    def __init__(self, suit : int, value : int, *groups):
        self.image : pg.Surface = get_card_image(suit, value)
        self.rect : pg.rect.Rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100
    

        super().__init__(*groups, Card.group)

def main() -> None:
    window : pg.Surface = pg.display.set_mode((800, 650))

    Card(1, 2)

    while True:
        # Process player inputs.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit
        
        Card.group.draw(window)

        pg.display.flip()


if __name__ == "__main__":
    main()