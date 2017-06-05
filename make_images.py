OpenDatabase("~/Desktop/meshtal.vtk")
AddPlot("Pseudocolor","TALLY_TAG")

OpenDatabase("~/Desktop/fng_zip.stl")
AddPlot("Mesh","STL_mesh")

m = MeshAttributes()
m.showInternal=1
m.opacity=10
SetPlotOptions(m)

AddOperator("Slice",1)
s = SliceAttributes()
SetOperatorOptions(s)

SaveSession("~/Desktop/example.session")

DrawPlots()

WindowAttributes=SaveWindowAttributes()
WindowAttributes.format = WindowAttributes.BMP
WindowAttributes.fileName="example"
WindowAttributes.width, WindowAttributes.height = 1024,768
WindowAttributes.screenCapture = 0
SetSaveWindowAttributes(WindowAttributes)
SaveWindow()

