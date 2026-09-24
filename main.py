
import pygame as pg
import settings as st

_FONTS={

}

def get_font(size):
    """эта функция даёт шрифт из размера """
    if size not in _FONTS:
        _FONTS[size]=pg.font.SysFont(st.FONT_NAME,size,bold=True)
    return _FONTS[size]
def draw_text(screen,text,x,y,size=24, color=st.COLORS["white"],center=False):
    """она возращает прямоугольник в которм текст расположение и размер"""
    surface = get_font(size).render(text,True,color)
    rect = surface.get_rect()
    if center:
        rect.center = (x,y)
    else:
        rect.topleft = (x,y)
    screen.blit(surface,rect)
    return rect
def draw_office(screen):
    c = st.COLORS
    screen.fill(c["wall"])
    #1
    pg.draw.rect(screen,c["floor"], (st.WIDTH*0.075,0.072*st.HEIGHT,0.1*st.WIDTH,st.HEIGHT*0.19))
    #2
    pg.draw.rect(screen,c["floor"],(0.25*st.WIDTH,0,0.5*st.WIDTH,0.42*st.HEIGHT))
    #3
    pg.draw.rect(screen,c["floor"],(0.825*st.WIDTH,0.072*st.HEIGHT,0.1*st.WIDTH,st.HEIGHT*0.19))
    #4
    pg.draw.rect(screen,c["floor"],(0,0.29*st.HEIGHT,0.066*st.WIDTH,0.048*st.HEIGHT))
    #5
    pg.draw.rect(screen,c["floor"],(0,0.33*st.HEIGHT,0.17*st.WIDTH,0.33*st.HEIGHT))
    #6
    pg.draw.rect(screen,c["floor"],(0,0.76*st.HEIGHT,st.WIDTH,0.24*st.HEIGHT))
    #7
    pg.draw.rect(screen,c["floor"],(0.5*st.WIDTH,0.62*st.HEIGHT,0.17*st.WIDTH,0.14*st.HEIGHT))
    #8
    pg.draw.rect(screen,c["floor"],(0.75*st.WIDTH,0.24*st.HEIGHT,0.033*st.WIDTH,0.095*st.HEIGHT))
    #9
    pg.draw.rect(screen,c["floor"],(0.93*st.WIDTH,0.29*st.HEIGHT,0.066*st.WIDTH,0.048*st.HEIGHT))
    #10
    pg.draw.rect(screen,c["floor"],(0.83*st.WIDTH,0.33*st.HEIGHT,0.17*st.WIDTH,0.33*st.HEIGHT))
def draw_hud(screen,hour,energy):
    c = st.COLORS
    draw_text(screen,f"{hour}AM",0.083*st.WIDTH,0,34,c["white"])
    draw_text(screen,"NIGHT 1",0.083*st.WIDTH,34,34,c["white"])
    draw_text(screen,f"ENERGY:{energy}%",0.825*st.WIDTH,0,34,c["white"])
    draw_energy_bar(screen,energy)
def draw_energy_bar(screen,energy):
    c = st.COLORS
    x,y,w,h=st.ENERGY_BAR_RECT
    pg.draw.rect(screen,c["wall"],(x,y,w,h))
    filled=int(w*energy/100)
    if energy <= st.ENERGY_LOW:
        color = c["red"]
    elif energy <= st.ENERGY_PRE_LOW :
        color = c["yellow"]
    else:
        color = c["green"]

    pg.draw.rect(screen,color,(x,y,filled,h))
    pg.draw.rect(screen,c["light_gray"],(x,y,w,h),2)
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
        draw_office(screen)
        draw_hud(screen,12,8)

        pg.display.flip()
        clock.tick(st.FPS)
    pg.quit()
if __name__ == "__main__":
    main()


