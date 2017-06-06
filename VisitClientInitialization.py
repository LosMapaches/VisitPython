import subprocess

# Visit needs to be added to PATH for this to work.
with subprocess.Popen(["visit", "-cli", "-nowin"], stdin=subprocess.PIPE, bufsize=1, universal_newlines=True) as shell:

	import PathCreator
	import DataLoading
	import PlotSettings
	import OperatorSettings
	import WindowSettings
	import Saving

	PathCreator.PathCreator()
	DataLoading.DataLoading()
	PlotSettings.PlotSettings()
	OperatorSettings.OperatorSettings()
	WindowSettings.WindowSettings()
	Saving.Saving()