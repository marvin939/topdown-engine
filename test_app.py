import unittest
from app import GameWindow
from scene import Scene
from constants import Signal

class TestApp(unittest.TestCase):

	def setUp(self):
		self.SCREENWIDTH = 640
		self.SCREENHEIGHT = 480
		self.app = GameWindow('GameWindow Test', (self.SCREENWIDTH, self.SCREENHEIGHT)) 
	

	def tearDown(self):
		pass


	def test_getscreen(self):
		screen = self.app.screen
		self.assertEqual(self.app.title, 'GameWindow Test')
		self.assertEqual(self.app.SCREENWIDTH, self.SCREENWIDTH)
		self.assertEqual(self.app.SCREENHEIGHT, self.SCREENHEIGHT)
	

	def test_register_scene(self):
		scene_name = 'random'

		# Test nulls
		with self.assertRaises(TypeError):
			# Test null scene, and name
			self.app.register_scene(None, scene_name)

			# Test null name
			self.app.register_scene(Scene(scene_name), None)

			#	Test with non-Signal type signal
			self.app.register_scene(Scene(scene_name), scene_name, "NOT A SIGNAL CONSTANT")

		# Test if scene registered properly
		scene = Scene(scene_name)
		sig = Signal.DUMMY
		self.app.register_scene(scene, scene_name, sig)
		self.assertEqual(self.app.scenedude[scene_name], scene)
		self.assertEqual(self.app.signalSceneDict[sig], scene)


if __name__ == '__main__':
	unittest.main()
