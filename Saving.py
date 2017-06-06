def Saving():
	DrawPlots()
	SaveSession("./Sessions/XML/example.session")
	WriteScript(open("./Sessions/Python/example.py", "wt"))
	SaveWindow()
	exit()
