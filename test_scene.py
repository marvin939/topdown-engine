import unittest
from scene import Scene, SceneManager
from constants import Signal
from copy import copy

class TestScene(unittest.TestCase):

	def setUp(self):
		self.scene = Scene('blank')


	def test_status(self):
		with self.assertRaises(NotImplementedError):
			print(self.scene.status)
	

	def test_subclass(self):
		class SceneA(Scene):
			def __init__(self):
				super().__init__('SceneA')
				self.quit = False

			@property
			def status(self):
				for i in range(0, 10):
					yield Signal.CONTINUE

				self.quit = True
				if self.quit:
					yield Signal.STOP

		scene = SceneA()
		self.assertTrue(issubclass(type(scene), Scene))

		# check if status ever gives the STOP signal
		self.assertTrue(any(signal == Signal.STOP for signal in scene.status)
)



class TestSceneManager(unittest.TestCase):

	def setUp(self):
		self.scenedude = SceneManager()
		class SubScene(Scene):
			def __init__(self):
				super().__init__('Scene subclass')
		self.ss = SubScene()


	def test_add(self):
		
		# test that the scene being added subclasses Scene
		with self.assertRaises(TypeError):
			self.scenedude['123'] = Scene('blanko')

		# test string-<incompatible_type> pair adding
		with self.assertRaises(TypeError):
			self.scenedude['123'] = 123

		# test <incompatible_type>-Scene pair adding
		with self.assertRaises(TypeError):
			self.scenedude[123] = self.ss

		# test screendude's current screen. This should be set when its
		# __currentscreen attribute is written by adding a new screen.
		self.scenedude['blank'] = self.ss
		self.assertEqual(self.scenedude.current, self.ss)
		
		
		
		
		
	

	def test_get(self):
		blankScene = self.ss
		self.scenedude['blank'] = blankScene
		self.assertEqual(self.scenedude['blank'], blankScene)

		# test incompatible key type retrieving a Scene item
		with self.assertRaises(TypeError):
			self.scenedude[123456]
	
	
	def test_currentStatus(self):
		blankScene = self.ss
		self.scenedude['blank'] = blankScene

		with self.assertRaises(NotImplementedError):
			print(self.scenedude.current.status)
	
	
	def test_change_scene(self):
		scene1 = self.ss
		scene2 = copy(self.ss)
		self.scenedude['scene1'] = scene1
		self.scenedude['scene2'] = scene2 

		self.assertEqual(self.scenedude.current, scene1)

		# change the scene
		current_scene = self.scenedude.change_scene('scene2')
		self.assertEqual(current_scene, scene2)

		# Try changing to an invalid/non-existant scene
		with self.assertRaises(KeyError):
			self.scenedude.change_scene('invalid-scene')
			self.scenedude.change_scene(None)
	



if __name__ == '__main__':
	unittest.main()
