import sys
from main import *

class Fread:
    def __init__(self):
        self.opf = open("main.om", "r", encoding="utf_8")
    def run(self):
        opf2 = self.opf.readlines()
        for inp in opf2:
            m = Main(inp)
            m.run()

if __name__ == "__main__":
    if os.path.exists("sys\\var.oms"):
        os.remove("sys\\var.oms")
    f = open("sys\\var.oms", "x", encoding="utf_8")
    f.close()
    f = Fread()
    f.run()
