import unittest
from app import GameWindow
from scene import Scene
from constants import Signal
from demoscenes import DummyScene

class TestApp(unittest.TestCase):

	def setUp(self):
		self.SCREENWIDTH = 640
		self.SCREENHEIGHT = 480
		self.app = GameWindow('GameWindow Test', (self.SCREENWIDTH, self.SCREENHEIGHT)) 
		class SubScene(Scene):
			def __init__(self):
				super().__init__('Scene subclass')
		self.ss = SubScene()
	

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

			# Test with non-Signal type signal
			self.app.register_scene(Scene(scene_name), scene_name, "NOT A SIGNAL CONSTANT")

		# Test if scene registered properly
		scene = self.ss
		sig = Signal.DUMMY
		self.app.register_scene(scene, scene_name, sig)
		self.assertEqual(self.app.current_scene, scene)
		self.assertEqual(self.app.signalSceneDict[sig], scene)

		# Test if the scene's screen size is set to the GameWindow's own size
		self.assertEqual(scene.SCREENWIDTH, self.app.SCREENWIDTH)
		self.assertEqual(scene.SCREENHEIGHT, self.app.SCREENHEIGHT)

		with self.assertRaises(TypeError):
			# try registering without name (use default name of scene)
			# try re-registering the same scene
			dummy = DummyScene()
			self.assertEqual(dummy.name, 'dummy')
			self.app.register_scene(dummy)
			self.app.register_scene(dummy)
	

	def test_scene_count(self):
		self.app.register_scene(self.ss)
		self.app.register_scene(DummyScene())
		try:
			self.app.register_scene(self.ss)
			self.app.register_scene(self.ss)
			self.app.register_scene(self.ss)
			self.app.register_scene(DummyScene())
			self.app.register_scene(DummyScene())
			self.app.register_scene(DummyScene())
			self.app.register_scene(DummyScene())
		except TypeError:
			pass
		self.assertEqual(self.app.scene_count, 2)
	
	
	@unittest.skip
	def test_set_starting_scene(self):
		dummy = DummyScene()
		self.app.register_scene(dummy, dummy.name)
		self.app.set_starting_scene(dummy.name)
		self.assertEqual(dummy.name, self.app.current_scene.name)


if __name__ == '__main__':
	unittest.main()
