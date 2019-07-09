from pprint import pprint
import SOLE


b = SOLE.Elevator.SimpleElevator()
print(b)

floorLabels = ["Lobby", 1, 2, 3]
floors = []
for floorLabel in floorLabels:
    f = SOLE.Floor.SimpleFloor({"label": floorLabel})
    floors.append(f)

for x in floors:
    print(x)

d = SOLE.Person.SimplePerson({"name": "Foo"})
print(d)

e = SOLE.Person.SimplePerson()
print(e)

a = SOLE.Building.SimpleBuilding({"floors": floors})
print(a)
