from csoport import *

beni: Tanulo = Tanulo("Krisztin", "Benedek", "2004.11.29.")
gergo: Tanulo = Tanulo("Krisztin", "Gergő", "2004.03.17.")
vicus: Tanulo = Tanulo("Krisztin", "Viktória", "2005.12.23.")
encsi: Tanulo = Tanulo("Krisztin", "Enikő", "2006.08.10.")
csoport: Csoport = Csoport("Krisztinek", [beni, gergo, vicus, encsi])

print(csoport)