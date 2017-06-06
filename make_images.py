import os

if not os.path.exists("./Data"):
	os.makedirs("./Data")

if not os.path.exists("./Images"):
	os.makedirs("./Images")

if not os.path.exists("./Sessions/Python"):
	os.makedirs("./Sessions/Python")

if not os.path.exists("./Sessions/XML"):
	os.makedirs("./Sessions/XML")

OpenDatabase("./Data/meshtal.vtk")
AddPlot("Pseudocolor", "TALLY_TAG")

OpenDatabase("./Data/fng_zip.stl")
AddPlot("Mesh", "STL_mesh")

m = MeshAttributes()
m.showInternal = 1
m.opacity = 10
SetPlotOptions(m)

AddOperator("Slice", 1)
s = SliceAttributes()
SetOperatorOptions(s)

SaveSession("./Sessions/XML/example.session")
WriteScript(open("./Sessions/Python/example.py", "wt"))

DrawPlots()

WindowAttributes = SaveWindowAttributes()
WindowAttributes.format = WindowAttributes.BMP
WindowAttributes.fileName = "./Images/example"
WindowAttributes.width, WindowAttributes.height = 1024, 768
WindowAttributes.screenCapture = 0
SetSaveWindowAttributes(WindowAttributes)
SaveWindow()

exit()
