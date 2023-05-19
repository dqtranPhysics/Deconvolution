import uproot
import types
import uproot_methods.classes.TH1

file = uproot.recreate("tmp.root", compression=uproot.ZLIB(4))

class MyTH1(uproot_methods.classes.TH1.Methods, list):
    def __init__(self, low, high, values, title=""):
        self._fXaxis = types.SimpleNamespace()
        self._fXaxis._fNbins = len(values)
        self._fXaxis._fXmin = low
        self._fXaxis._fXmax = high
        for x in values:
            self.append(float(x))
        self._fTitle = title
        self._classname = "TH1F"

histogram = MyTH1(-5, 5, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])

file["synthetic"] = histogram

file["synthetic"].show()
