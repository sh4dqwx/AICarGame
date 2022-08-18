from pygame import Vector2

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
PLAYER_START = Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT * 5 / 6)
PLAYER_SIZE = Vector2(120, 120)
PLAYER_VELOCITY = 10
ENEMY_START_SIZE = Vector2(100, 100)
ENEMY_MAX_SIZE = Vector2(120, 120)
ENEMY_SPEED = 5
ENEMY_INTERVAL = 1
SECOND_LANE_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.25)
FIRST_LANE_START = Vector2(WINDOW_WIDTH * 0.44, WINDOW_HEIGHT * 0.25)
THIRD_LANE_START = Vector2(WINDOW_WIDTH * 0.56, WINDOW_HEIGHT * 0.25)
SECOND_LANE_VECTOR = Vector2(0, 1)
FIRST_LANE_VECTOR = Vector2(WINDOW_WIDTH * -0.36, WINDOW_HEIGHT * 0.75).normalize()
THIRD_LANE_VECTOR = Vector2(WINDOW_WIDTH * 0.36, WINDOW_HEIGHT * 0.75).normalize()