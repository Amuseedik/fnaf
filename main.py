
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
    """рисуте объекты офиса виде прямоугольников,нам нужно передать экран на которм будем рисовать """
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
def draw_door(screen,rect_tuple,key_hint,close,mouse_pos):
    """рисует на экране несколько прямоугольников пол и размеры и кординаты,и проверяет наведен ли курсор мыши на дверь
    ,если игрок близок то дверь подсевечивается,если дверь заперта то она отображается серым,если дверь открыта она отображается черным,нам нужно
    передать экран,кортеж из данных прямоуглоьника,key_hint,параментр который хранит закрыта ли дверь ,положения курсора """
    c = st.COLORS
    rect = pg.Rect(rect_tuple)

    hovered = rect.collidepoint(mouse_pos)
    if close:
        pg.draw.rect(screen,c["gray"],rect)
        for y in range(rect.top+20,rect.bottom-10,40):
            pg.draw.line(screen,c["light_gray"],(rect.left+10,y),(rect.right-10,y),3)
        else:
            pg.draw.rect(screen,c["black"],rect)
    if hovered:
        border_color = c["white"]
    else:
        border_color = c["light_gray"]
    pg.draw.rect(screen,border_color,rect,4)
    if close:
        state,color = "Закрыта",c["green"]
    else:
        state,color =  "Открыта",c["light_gray"]
    draw_text(screen,state,rect.centerx,rect.bottom+16,18,color,center=True)
    draw_text(screen,f"[{key_hint}]",rect.centerx,rect.top-16,18,c["light_gray"],center=True)
def draw_hud(screen,hour,energy):
    """отвечает за отображение важной игровой информации на экране,за время за какая ночь и за энергию,мы передаем сюда экрна,часы,энергия"""
    c = st.COLORS
    draw_text(screen,f"{hour}AM",0.083*st.WIDTH,0,34,c["white"])
    draw_text(screen,"NIGHT 1",0.083*st.WIDTH,34,34,c["white"])
    draw_text(screen,f"ENERGY:{energy}%",0.825*st.WIDTH,0,34,c["white"])
    draw_energy_bar(screen,energy)
def draw_energy_bar(screen,energy):
    """рисует полоску энергий,мы предаем сюда экран и энергию. """
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
def make_camera_buttons():
    """показывает расположениий камер и кнопок. """
    step = st.CAM_BTN_GAP + st.CAM_BTN_GAP*st.CAM_BTN_W
    total = step*len(st.CAMERAS)-st.CAM_BTN_GAP
    start_x =( st.WIDTH - total)//2
    return [pg.Rect(start_x + i * step, st.CAM_BTN_Y,st.CAM_BTN_W,st.CAM_BTN_H)for i ,name in enumerate(st.CAMERAS)]
def draw_button(screen,rect,text,active=False,hovered=False):
    """отвечате просто за динамику за отобрадение кнопки их цвета ,мы предаем сюда экран ,прямоугольник ,текст,состояние кнопки,для того что бы
    наведен ли курсор"""
    c = st.COLORS
    if active:
        bg,bordr,fg=c["blue"],c["white"],c["white"]
    elif hovered:
        bg,bordr,fg=c["gray"],c["white"],c["white"]
    else :
        bg,bordr,fg=c["dark"],c["light_gray"],c["light_gray"]
    pg.draw.rect(screen,bg,rect)
    pg.draw.rect(screen,bordr,rect,2)
    draw_text(screen,text,rect.centerx,rect.centery,18,fg,center=True)

def toggle_door(doors,side):
    doors[side] = not doors[side]
def handle_click(pos,doors,buttons,current_cam):
    if pg.Rect(st.LEFT_DOOR_RECT).collidepoint(pos):
        toggle_door(doors,"left")
        return current_cam
    if pg.Rect(st.RIGHT_DOOR_RECT).collidepoint(pos):
        toggle_door(doors,"right")
        return current_cam
    for i,rect in enumerate(buttons):
        if rect.collidepoint(pos):
            return None if current_cam == i else i
    return current_cam

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
