	SplitObjects = SplitLines[1].split('\n')
	for Line in SplitObjects:
		if len(Line) > 0:
			params = Line.split(',')
			posx = int(params[0])
			posy = int(params[1])
			time = int(params[2])
			ntype = int(params[3])
			IgnoreFirstLine = True
			if ntype == 1 or ntype == 5:
				nota = Nota(posx, posy, time, sprites[random.randint(0,3)], screen_width, screen_height, 1)
				NoteList.append(nota)
			elif ntype == 2 or ntype == 6:
				## THE GOD LINE
				## this.sliderTime = game.getBeatLength() * (hitObject.getPixelLength() / sliderMultiplier) / 100f;
				curva = params[5]
				repeat = int(params[6])
				pixellength = float(params[7])
				
				sliderEndTime = (bpm * (pixellength/1.4) / 100.0)