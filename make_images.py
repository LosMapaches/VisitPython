#import PathCreator
#import DataLoading
#import PlotSettings
#import OperatorSettings
#import WindowSettings
#import Saving

#PathCreator.PathCreator()
#DataLoading.DataLoading()
#PlotSettings.PlotSettings()
#OperatorSettings.OperatorSettings()
#WindowSettings.WindowSettings()
#Saving.Saving()


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

def DataLoading():
	visit.OpenDatabase("./Data/meshtal.vtk")
	visit.AddPlot("Pseudocolor", "TALLY_TAG")

	visit.OpenDatabase("./Data/fng_zip.stl")
	visit.AddPlot("Mesh", "STL_mesh")

def PlotSettings():
	m = MeshAttributes()
	m.showInternal = 1
	m.opacity = 10
	SetPlotOptions(m)
	
def OperatorSettings():
	AddOperator("Slice", 1)
	s = SliceAttributes()
	SetOperatorOptions(s)
	
def WindowSettings():
	WindowAttributes = SaveWindowAttributes()
	WindowAttributes.format = WindowAttributes.BMP
	WindowAttributes.fileName = "./Images/example"
	WindowAttributes.width, WindowAttributes.height = 1024, 768
	WindowAttributes.screenCapture = 0
	SetSaveWindowAttributes(WindowAttributes)

def Saving():
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
