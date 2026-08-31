import pygame as pg
import settings as st
def main():
    pg.init()
    screen = pg.display.set_mode((st.WIDTH, st.HEIGHT))
    pg.display.set_caption(st.TITLE)
    clock = pg.time.Clock()

    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:

                running = False

        screen.fill(st.COLORS["red"])

        pg.display.flip()
        clock.tick(st.FPS)
    pg.quit()
if __name__ == "__main__":
    main()
