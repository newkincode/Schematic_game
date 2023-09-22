import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((960, 640))

# 변수

# 화면 타이틀 설정
pygame.display.set_caption(f"SG {ver_text}")

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 로직 업데이트

    # 화면 업데이트
    screen.fill((0, 0, 0))  # 화면을 검은색으로 채웁니다.

    # 여기에 게임 객체 그리기 또는 화면 업데이트 코드를 추가할 수 있습니다.

    pygame.display.update()

# Pygame 종료
pygame.quit()
sys.exit()
