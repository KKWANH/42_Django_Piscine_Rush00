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
					listMovieId=List(),
					dataMovieIMDB=None,
					MenuItem=0				):
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


	def	dump(self, filename="data:pickle"):
		_dic = {
			"positionPlayer"	:	self.getPositionPlayer(),
			"amoutMovieBall"	:	self.getAmoutMovieBall(),
			"listMovieId"		:	self.getListMovieId(),
			"dataMovieIMDB"		:	self.getDataMovieIMDB(),
			"menuItem"			:	self.getMenuItem()
		}
		_fil = open(filename, "wb")
		pickle.dump(_dic, _fil)
		_fil.close()
	
	def	load(self, filename="data:pickle"):
		_fil = open(filename, "rb")
		_dic = pickle.load(_fil)
		return	_dic
	
	def	load_default_setting(self):
		self.positionPlayer = settings.DEFAULT_START_PLAYER_POSITION
		self.amoutMovieBall = settings.DEFAULT_AMOUNT_BALL
		self.listMovieId	= list()
		self.dataMovieIMDB	= self.load_IMDB()
		self.menuItem		= 0
	
	def	load_IMDB(self):
		_dat = Data()
		return	_dat.get()
	
	def	get_random_movie(self):
		_dat = Data()
		return	_dat.get_random_movie()
	
	def	get_movie(self, name):
		_dat = Data()
		_dat.get_movie(name)
		return	_dat
	
	def	get_strength(self):
		return	len(self.listMovieId) + 1
	
	def	coefBattle(self, strengthEnemy):
		strengthPlayer = self.get_strength()
		c = 50 - (strengthEnemy * 10) + (strengthPlayer * 5)
		if (c <= 1):
			return	1
		elif c >= 90:
			return	90
		return	c
	
	def	addListMovieId(self, listMovieId):
		self.listMovieId.append(listMovieId)