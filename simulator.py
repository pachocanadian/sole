import SOLE

b = SOLE.Elevator.SimpleElevator()
print("SimpleElevator uuid=" + str(b.uuid()))

floors = []
for floorLabel in range(3):
    f = SOLE.Floor.SimpleFloor(floorLabel)
    floors.append(f)

for x in floors:
    print("Floor label {} with uuid={}".format(x.label, x.uuid()))

d = SOLE.Person.SimplePerson()
print("SimplePerson uuid=" + str(d.uuid()))

a = SOLE.Building.SimpleBuilding()
print("SimpleBuilding uuid=" + str(a.uuid()))
