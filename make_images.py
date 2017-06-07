Files={"meshtal.vtk" : ["Pseudocolor"]+["TALLY_TAG"],
	"fng_zip.stl" : ["Mesh"]+["STL_mesh"],
	}


def PathCreator():
	"""Form folders to contain Data, Sessions, and Images.


	Folders created:
	./Data -- data used for visualization
	./Images -- windows images saved
	./Sessions/Python -- python session files
	./Sessions/XML -- XML session files
	"""

	import os

	if not os.path.exists("./Images"):
		os.makedirs("./Images")

	if not os.path.exists("./Sessions/Python"):
		os.makedirs("./Sessions/Python")

	if not os.path.exists("./Sessions/XML"):
		os.makedirs("./Sessions/XML")


def DataLoading(File):
	"""Load data to VisIt and add plot.


	Data used:
	*.vtk -- results
	*.stl -- geometry
	"""
	for key in File:
		OpenDatabase("./Data/"+key)
		AddPlot(File[key][0], File[key][1])


def PlotSettings():
	"""Visual settings for plots."""

	# Mesh plot attributes.
	MeshAttributes().legendFlag = 1
	#MeshAttributes().lineStyle = "SOLID"
	MeshAttributes().lineWidth = 0
	MeshAttributes().meshColor = (0, 0, 0, 255)
	#MeshAttributes().meshColorSource = "Foreground"
	#MeshAttributes().opaqueColorSource = "Background"
	#MeshAttributes().opaqueMode = "Auto"
	MeshAttributes().pointSize = 0.05
	#MeshAttributes().opaqueColorSourcesmoothingLevel = (255, 255, 255, 255)
	MeshAttributes().pointSizeVarEnabled = 0
	MeshAttributes().pointSizeVar = "default"
	#MeshAttributes().pointType = "Point"
	MeshAttributes().showInternal = 0
	MeshAttributes().pointSizePixels = 2
	MeshAttributes().opacity = 1

	SetPlotOptions(MeshAttributes())

	# Pseudocolor plot attributes.
	#PseudocolorAttributes().scaling = "Linear"
	PseudocolorAttributes().lineType = PseudocolorAttributes().Tube

	SetPlotOptions(PseudocolorAttributes())


def OperatorSettings():
	"""Add operator and it's settings."""

	AddOperator("Slice", 1)

	SetOperatorOptions(SliceAttributes())


def WindowSettings():
	"""Modify window settings."""

	WindowAttributes = SaveWindowAttributes()
	WindowAttributes.format = WindowAttributes.BMP
	WindowAttributes.fileName = "./Images/example"
	WindowAttributes.width, WindowAttributes.height = 2000, 2000
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

DataLoading(Files)

PlotSettings()
OperatorSettings()
WindowSettings()
Saving()
