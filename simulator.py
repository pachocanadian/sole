import SOLE

b = SOLE.Elevator.SimpleElevator()
print("SimpleElevator id=" + str(b.id()))

floors = []
for floorLabel in range(3):
    f = SOLE.Floor.SimpleFloor(floorLabel)
    floors.append(f)

for x in floors:
    print("Floor label {} with id={}".format(x.label, x.id()))

d = SOLE.Person.SimplePerson()
print("SimplePerson id=" + str(d.id()))

a = SOLE.Building.SimpleBuilding()
print("SimpleBuilding id=" + str(a.id()))
