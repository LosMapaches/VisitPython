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
	Attribute=MeshAttributes()

	Attribute.legendFlag = 1
	Attribute.lineStyle = Attribute.DASH  # SOLID DASH DOT DOTDASH
	Attribute.lineWidth = 0
	Attribute.meshColor = (0, 0, 0, 255)
	Attribute.meshColorSource = Attribute.Foreground  # Foreground MeshCustom
	Attribute.opaqueColorSource = Attribute.Background  # Background OpaqueCustom
	Attribute.opaqueMode = Attribute.Auto  # Auto On Off
	Attribute.pointSize = 0.05
	Attribute.opaqueColor = (255, 255, 255, 255)
	Attribute.smoothingLevel = Attribute.None  # None Fast High
	Attribute.pointSizeVarEnabled = 0
	Attribute.pointSizeVar = "default"
	Attribute.pointType = Attribute.Point  # Point Box Axis Icosahedron Octahedron Tetrahedron SphereGeometry Point Sphere
	Attribute.showInternal = 0
	Attribute.pointSizePixels = 2
	Attribute.opacity = 1

	SetPlotOptions(Attribute)

	# Pseudocolor plot attributes.
	Attribute = PseudocolorAttributes()

	Attribute.scaling = Attribute.Linear  # Linear Log Skew
	Attribute.skewFactor = 1
	Attribute.limitsMode = Attribute.OriginalData  # OriginalData CurrentPlot
	Attribute.minFlag = 0
	Attribute.min = 0
	Attribute.maxFlag = 0
	Attribute.max = 1
	Attribute.centering = Attribute.Natural # Natural Nodal Zonal
	Attribute.colorTableName = "hot"  # See options in VisIt
	Attribute.invertColorTable = 0
	Attribute.opacityType = Attribute.FullyOpaque  # FullyOpaque ColorTable Constant Ramp VariableRange
	Attribute.opacityVariable = ""
	Attribute.opacity = 1
	Attribute.opacityVarMin = 0
	Attribute.opacityVarMax = 1
	Attribute.opacityVarMinFlag = 0
	Attribute.opacityVarMaxFlag = 0
	Attribute.pointSize = 0.05
	Attribute.pointType = Attribute.Point  # Point Box Axis Icosahedron Octahedron Tetrahedron SphereGeometry Point Sphere
	Attribute.pointSizeVarEnabled = 0
	Attribute.pointSizeVar = "default"
	Attribute.pointSizePixels = 2
	Attribute.lineType = Attribute.Tube  # Line Tube Ribbon
	Attribute.lineStyle = Attribute.SOLID  # SOLID DASH DOT DOTDASH
	Attribute.lineWidth = 0
	#Attribute.tubeDisplayDensity = 10
	Attribute.tubeRadiusSizeType = Attribute.FractionOfBBox  # FractionOfBBox Absolute
	Attribute.tubeRadiusAbsolute = 0.125
	Attribute.tubeRadiusBBox = 0.005
	#Attribute.varyTubeRadius = 0
	#Attribute.varyTubeRadiusVarible = ""
	#Attribute.varyTubeRadiusFactor = 10
	#Attribute.endPointType = Attribute.None  # None Tails Heads Both
	#Attribute.endPointStyle = Attribute.Spheres  # Spheres Cones
	Attribute.endPointRadiusSizeType = Attribute.FractionOfBBox # FractionOfBBox Absolute
	Attribute.endPointRadiusAbsolute = 1
	Attribute.endPointRadiusBBox = 0.005
	Attribute.endPointRatio = 2
	Attribute.renderSurfaces = 1
	Attribute.renderWireframe = 0
	Attribute.renderPoints = 0
	Attribute.smoothingLevel = 0
	Attribute.legendFlag = 1
	Attribute.lightingFlag = 1

	SetPlotOptions(Attribute)


def OperatorSettings():
	"""Add operator and it's settings."""

	AddOperator("Slice", 1)

	Attribute = SliceAttributes()
	SetOperatorOptions(Attribute)


def WindowSettings():
	"""Modify window settings."""

	Attribute = SaveWindowAttributes()
	Attribute.format = Attribute.BMP
	Attribute.fileName = "./Images/example"
	Attribute.width = 2000
	Attribute.height = 2000
	Attribute.screenCapture = 0

	SetSaveWindowAttributes(Attribute)


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
