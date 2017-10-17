'''
Demonstrate how easy it is to use GameWindow, and show contents of
DummyScene.
'''

from demoscenes import DummyScene
from app import GameWindow

if __name__ == '__main__':
	game = GameWindow(title='[Demo] Headcrabs!!!', screen_size=(640, 480))
	game.register_scene(DummyScene(), 'dummy')
	game.start()
