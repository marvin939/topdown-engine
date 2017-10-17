from enum import IntEnum

class Signal(IntEnum):
	CONTINUE = 0
	MAIN_MENU = 1
	START_GAME = 2
	PAUSE = 3
	STOP = 4
	QUIT = 200
	INTRO = 500
	NONE = 10000
	DUMMY = 10001

