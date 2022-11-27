import myversion as my
from singleton import Singleton

singleton = Singleton.getInstance()
singleton.obj1 = my.Game()
singleton.obj1.run()
