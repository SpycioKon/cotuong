import pygame as pg

# kich co man hinh
WIDTH, HEIGHT = 1000,650 #đ
# khoi tao cac o chua quan
COLS, ROWS = 9,9
SAMPLE = 600
CELL = SAMPLE // ROWS

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Cờ Tướng")

#BTL_NHOM12_chinese_chess\images\pieces\blue-car.png
image_car_blue = pg.image.load("./images/pieces/blue-car.png")
image_car_blue = pg.transform.scale(image_car_blue, (CELL, CELL))

image_car_red = pg.image.load("./images/pieces/red-car.png")
image_car_red = pg.transform.scale(image_car_red, (CELL, CELL))

running = True
selected = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = event.pos
            col,row = mouse_x // CELL, mouse_y // CELL
            if not selected:
                if(col,row) == piece_pos:
                    selected = True
            else:
                piece_pos = (col,row)
                selected = False
        else:
            screen.fill("white")
            for row in range(ROWS):
                for col in range(COLS):
                    if (row == 0) and (col == 0 or col == COLS-1):
                        rect = pg.Rect(col * CELL, row * CELL, CELL, CELL)
                        screen.blit(image_car_blue, rect.topleft)  # Hiển thị ảnh tại vị trí ô
                    elif (row == ROWS-1) and (col == 0 or col == COLS-1):
                        rect = pg.Rect(col * CELL, row * CELL, CELL, CELL)
                        screen.blit(image_car_red, rect.topleft)  # Hiển thị ảnh tại vị trí ô
                    else:
                        rect = pg.Rect(col * CELL, row * CELL, CELL, CELL)
                        pg.draw.rect(screen, "red", rect, 1)
        pg.display.flip()
pg.quit()