import	pickle
import	random
import	sys
import	os
from	django.conf			import settings
from	game.api			import Data


class	DataStorage:

	def	__init__(	self,
					positionPlayer=list(),
					amountMovieBall=150,
					listMovieId=list(),
					dataMovieIMDB=None,
					menuItem=0				):
		self.positionPlayer = positionPlayer
		if len(self.positionPlayer) == 0:
			self.positionPlayer = settings.DEFAULT_START_PLAYER_POSITION
		self.amout_MvBall = amountMovieBall
		self.listMovieId = listMovieId
		self.dataMovieIMDB = dataMovieIMDB
		self.menuItem = menuItem
		settings.BALLS = amountMovieBall


	def	setPositionPlayer(self, positionPlayer):
		self.positionPlayer = positionPlayer
	def	getPositionPlayer(self):
		return	(self.positionPlayer)

	def	setAmountMovieBall(self, amountMovieBall):
		self.amountMovieBall = amountMovieBall
		settings.BALLS = amoutMovieBall
	def	getAmountMovieBall(self):
		return	self.amountMovieBall
	
	def	setListMovieName(self, listMovieId):
		self.listMovieId = listMovieId
	def	getListMovieName(self):
		return	self.listMovieId

	def	getMoviesById(self):
		_dat = Data()
		_arr = self.getListMovieName()
		return	_dat.getMovieById(_arr)
	
	def	setDataMovieIMDB(self, dataMovieIMDB):
		self.dataMovieIMDB = dataMovieIMDB
	def	getDataMovieIMDB(self):
		return	self.dataMovieIMDB

	def	setMenuItem(self, menuItem):
		self.menuItem = menuItem
	def	getMenuItem(self):
		return	self.menuItem
	
	def	addAmoutMovieBall(self):
		self.amoutMovieBall = self.amoutMovieBall + 1
		settings.BALLS = settings.BALLS + 1
	def	removeAmoutMovieBall(self):
		self.amoutMovieBall = self.amoutMovieBall - 1
		settings.BALLS = settings.BALLS - 1

