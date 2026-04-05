#from python_OOP_classes import *
#import python_OOP_classes
#from python_OOP_classes import bluebrint_auto
from python_OOP_classes import mini



#mini1 = mini

mini1 = mini("D", "blau", 10000, 4)
mini2 = mini("A15", "gelb")

print(mini.__module__, mini1.model, mini1.alter, mini1.farbe, mini1.kmstand)
print(mini.__module__, mini2.model, mini2.alter, mini2.farbe, mini2.kmstand)
mini1.auto_fahren(200)

mini1.mini_sachen("Tanken")