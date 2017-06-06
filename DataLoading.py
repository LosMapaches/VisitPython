def DataLoading():
	OpenDatabase("./Data/meshtal.vtk")
	AddPlot("Pseudocolor", "TALLY_TAG")

	OpenDatabase("./Data/fng_zip.stl")
	AddPlot("Mesh", "STL_mesh")
