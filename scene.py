import pygame
from pygame.locals import *

"""
Screen or Scene?
eg. ScreenManager vs SceneManager
"""

class SceneManager():

	def __init__(self):
		self.scenedict = {}
		self.__currentscene = None
	

	def __setitem__(self, key, value):
		if not issubclass(type(value), Scene) or type(value) is Scene:
			raise TypeError('{}({}) does not subclass/inherit Scene!'.format(value, type(value)))
		if type(key) is not str:
			raise TypeError('{}({}) is not type str!'.format(key, type(key)))

		self.scenedict[key] = value

		if self.__currentscene == None:
			self.__currentscene = self.scenedict[key]
	

	def __getitem__(self, key):
		if type(key) is not str:
			raise TypeError('{}({}) is not type str!'.format(key, type(key)))
		return self.scenedict[key]
	
	
	@property
	def current(self):
		if self.__currentscene is None:
			raise AttributeError('There are no screens in SceneManager.')
		return self.__currentscene
	

	@property
	def count(self):
		return len(self.scenedict.items())
	

	def change_scene(self, scene_name):
		self.__currentscene = self.scenedict[scene_name]
		return self.current
	
	

class Scene():

	def __init__(self, name):
		self.name = name
		self.SCREENHEIGHT = 0
		self.SCREENWIDTH = 0
	

	def handle_event(self, event):
		pass
	

	def draw_scene(self, screen):
		pass
	
	def set_screen_size(self, size):
		if not isinstance(size, tuple) or len(size) != 2 or not all((type(n) is int for n in size)):
			raise TypeError('size argument must be a tuple containing two integers!')
		self.SCREENWIDTH, self.SCREENHEIGHT = size
	

	@property
	def status(self):
		"""
		Returns an integer enum constant as a signal for GameWindow to
		keep running current Scene, or move to another one.
		"""
		raise NotImplementedError()
	
