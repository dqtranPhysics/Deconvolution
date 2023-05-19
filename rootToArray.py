import uproot
import numpy as np

def rootToArray(rootName,histName):

	file = uproot.open("./" + rootName)
	tree = file["fiberHarpOffline"]
	time = tree[histName].edges
	intensity = tree[histName].values

	return intensity
