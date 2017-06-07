def PathCreator():
	"""Form folders to contain Data, Sessions, and Images.


	Folders created:
	./Data -- data used for visualization
	./Images -- windows images saved
	./Sessions/Python -- python session files
	./Sessions/XML -- XML session files
	"""

	import os

	if not os.path.exists("./Data"):
		os.makedirs("./Data")

	if not os.path.exists("./Images"):
		os.makedirs("./Images")

	if not os.path.exists("./Sessions/Python"):
		os.makedirs("./Sessions/Python")

	if not os.path.exists("./Sessions/XML"):
		os.makedirs("./Sessions/XML")


def DataLoading():
	"""Load data to VisIt and add plot.


	Data used:
	*.vtk -- results
	*.stl -- geometry
	"""

	visit.OpenDatabase("./Data/meshtal.vtk")
	visit.AddPlot("Pseudocolor", "TALLY_TAG")

	visit.OpenDatabase("./Data/fng_zip.stl")
	visit.AddPlot("Mesh", "STL_mesh")


def PlotSettings():
	"""Visual settings for plots."""

	MeshAttributes().showInternal = 1
	MeshAttributes().opacity = 10
	SetPlotOptions(MeshAttributes())


def OperatorSettings():
	"""Add operator and it's settings."""

	AddOperator("Slice", 1)
	SetOperatorOptions(SliceAttributes())


def WindowSettings():
	"""Modify window settings."""

	WindowAttributes = SaveWindowAttributes()
	WindowAttributes.format = WindowAttributes.BMP
	WindowAttributes.fileName = "./Images/example"
	WindowAttributes.width, WindowAttributes.height = 1024, 768
	WindowAttributes.screenCapture = 0
	SetSaveWindowAttributes(WindowAttributes)


def Saving():
	"""Displays plots on windows and saves sessions and images."""

	DrawPlots()
	SaveSession("./Sessions/XML/example.session")
	WriteScript(open("./Sessions/Python/example.py", "wt"))
	SaveWindow()
	exit()


PathCreator()
DataLoading()
PlotSettings()
OperatorSettings()
WindowSettings()
Saving()
