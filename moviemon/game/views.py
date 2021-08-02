import	os
import	random
from	django.shortcuts	import get_object_or_404, render, redirect
from	.models				import Movie
from	django.http			import HttpResponse, HttpResponseRedirect
from	django.conf			import settings
from	.view_util			import *


_dts	= DataStorage()

def	ft_index(request):
	settings.INDEX = 0
	if request.method == "GET":
		button = request.GET.get('button')
		if button:
			if (button == "A"):
				stor = DataStorage()
				stor.load_default_settings()
				stor.dump()
				return HttpResponseRedirect("worldmap/")
			elif (button == "B"):
				return HttpResponseRedirect("/options/load_game/")
	return render(request, "title.html", {
		"buttons": {
			"a": {"text": "New Game"},
			"b": {"text": "Load"}
		}
	})

def	ft_worldMap(request):
	_dts.load()
	_pos = _dts.getPositionPlayer()
	_po2 = {}
	_btn = request.GET.get('button', '')
	if _btn:
		if _btn == "up"		 and _pos[1] > 0:
			_pos[1] -= 1
		elif _btn == "down"	 and _pos[1] + 1 < settings.DEFAULT_GAME_SIZE:
			_pos[1] += 1
		elif _btn == "left"	 and _pos[0] > 0:
			_pos[0] -= 1
		elif _btn == "right" and _pos[0] + 1 < settings.DEFAULT_GAME_SIZE:
			_pos[0] += 1
		elif _btn == "select":
			return redirect("../moviedex")
		elif _btn == "start":
			return redirect("../options")
		elif _btn == "b":
			settings.TOKEN = ''
	settings.TOKEN = ''
	if _pos[0] and settings.DEFAULT_GAME_SIZE > 0:
		_po2["x"] = _pos[0] * (100 / settings.DEFAULT_GAME_SIZE)
	else:
		_po2["x"] = 0
	if _pos[1] and settings.DEFAULT_GAME_SIZE > 0:
		_po2["y"] = _pos[1] * (100 / settings.DEFAULT_GAME_SIZE)
	else:
		_po2["y"] = 0
	_obj = {"position": _po2}
	_mov = {}
	if random.randrange(100) < 30:
		_mov = _dts.get_random_movie()
	if _mov:
		_tok = "tokenid123"
		settings.TOKEN = _tok
		_obj["moviemon"] = _mov
		_btl = "../battle/" + _mov["imdbID"] + "?tokenid=" + _tok
		_obj["buttons"] = {"a": {"link": _btl}}
	_bal = False
	if not _mov and random.randrange(100) < 25:
		_bal = True
	if _mov: 
		_obj["movieball"] = True
		_dts.addAmoutMovieBall()
	_scr = {}
	_scr["movieballs"] = settings.BALLS
	_scr["moviemons_left"] = len(settings.MOVIES)
	_scr["moviemons_totla"] = settings.SIZE_MOVIE
	_obj["screen_data"] = _scr
	return	render(request, "worldMap.html", _obj)