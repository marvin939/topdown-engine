from demoscenes import DummyScene
from app import GameWindow

if __name__ == '__main__':
	game = GameWindow()
	game.register_scene(DummyScene(), 'dummy')
	game.start()
