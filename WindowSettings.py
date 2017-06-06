def WindowSettings():
	WindowAttributes = SaveWindowAttributes()
	WindowAttributes.format = WindowAttributes.BMP
	WindowAttributes.fileName = "./Images/example"
	WindowAttributes.width, WindowAttributes.height = 1024, 768
	WindowAttributes.screenCapture = 0
	SetSaveWindowAttributes(WindowAttributes)
	