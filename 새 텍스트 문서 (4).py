# PyGame 모듈을 임포트합니다.
import pygame

# 화면 크기를 설정합니다.
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상을 정의합니다.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 버튼과 레버의 위치와 크기를 정의합니다.
button_x = 100
button_y = 100
button_width = 100
button_height = 50
lever_x = 300
lever_y = 100
lever_width = 50
lever_height = 100

# 전선의 시작점과 끝점을 정의합니다.
wire_start_x = button_x + button_width // 2
wire_start_y = button_y + button_height // 2
wire_end_x = lever_x + lever_width // 2
wire_end_y = lever_y + lever_height // 2

# 버튼과 레버의 상태를 저장하는 변수를 정의합니다.
button_pressed = False
lever_pulled = False

# 게임 루프를 시작합니다.
running = True
while running:
    # 이벤트를 처리합니다.
    for event in pygame.event.get():
        # 창을 닫으면 게임을 종료합니다.
        if event.type == pygame.QUIT:
            running = False
        # 마우스 버튼을 누르면 버튼과 레버의 상태를 변경합니다.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 버튼 위에 마우스가 있으면 버튼을 누릅니다.
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                button_pressed = True
            # 레버 위에 마우스가 있으면 레버를 당깁니다.
            elif lever_x <= mouse_x <= lever_x + lever_width and lever_y <= mouse_y <= lever_y + lever_height:
                lever_pulled = True
        # 마우스 버튼을 뗄 때 버튼과 레버의 상태를 원래대로 돌립니다.
        elif event.type == pygame.MOUSEBUTTONUP:
            button_pressed = False
            lever_pulled = False

    # 화면을 하얀색으로 채웁니다.
    screen.fill(WHITE)

    # 버튼과 레버를 그립니다.
    pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height))
    pygame.draw.rect(screen, BLACK, (lever_x, lever_y, lever_width, lever_height))

    # 버튼이 눌려있거나 레버가 당겨져 있으면 전선을 켜고 아니면 꺼줍니다.
    if button_pressed or lever_pulled:
        pygame.draw.line(screen, GREEN, (wire_start_x, wire_start_y), (wire_end_x, wire_end_y), 5)
    else:
        pygame.draw.line(screen, RED, (wire_start_x, wire_start_y), (wire_end_x, wire_end_y), 5)

    # 화면을 업데이트합니다.
    pygame.display.flip()
