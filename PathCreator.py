def PathCreator():
	import os

	if not os.path.exists("./Data"):
		os.makedirs("./Data")

	if not os.path.exists("./Images"):
		os.makedirs("./Images")

	if not os.path.exists("./Sessions/Python"):
		os.makedirs("./Sessions/Python")

	if not os.path.exists("./Sessions/XML"):
		os.makedirs("./Sessions/XML")
