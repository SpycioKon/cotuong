import pygame

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 1000, 850
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Di chuyển quân cờ bằng click chuột")

# Số hàng và cột
ROWS, COLS = 9,9
CELL_SIZE = 600 // 9  # Kích thước mỗi ô

# Load ảnh quân cờ
piece_img = pygame.image.load("./images/pieces/blue-car.png")  # Thay bằng ảnh quân cờ của bạn
piece_img = pygame.transform.scale(piece_img, (CELL_SIZE, CELL_SIZE))

# Vị trí quân cờ ban đầu (ô 3,3)
piece_pos = (3, 3)
selected = False  # Trạng thái chọn quân cờ

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Xử lý sự kiện click chuột
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col, row = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE

            if not selected:
                # Nếu click vào quân cờ, chọn quân cờ
                if (col, row) == piece_pos:
                    selected = True
            else:
                # Nếu đã chọn quân cờ, click vào ô khác để di chuyển
                piece_pos = (col, row)
                selected = False  # Hủy chọn

    # Tô nền
    screen.fill((255, 255, 255))

    # Vẽ lưới 8x8
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    # Hiển thị quân cờ
    piece_rect = pygame.Rect(piece_pos[0] * CELL_SIZE, piece_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    screen.blit(piece_img, piece_rect.topleft)

    pygame.display.flip()

pygame.quit()
