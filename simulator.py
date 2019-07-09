import SOLE

b = SOLE.Elevator.SimpleElevator()
print("SimpleElevator uuid=" + str(b.uuid()))

floors = []
for floorLabel in range(3):
    f = SOLE.Floor.SimpleFloor({"label": floorLabel})
    floors.append(f)

for x in floors:
    print("Floor label {} with uuid={}".format(x.get("label"), x.uuid()))

d = SOLE.Person.SimplePerson({"name": "Foo"})
print(
    "SimplePerson uuid="
    + str(d.uuid())
    + " with name="
    + d.get("name")
    + " and badkey="
    + d.get("badkey")
)

e = SOLE.Person.SimplePerson()
print(
    "SimplePerson uuid="
    + str(e.uuid())
    + " with name="
    + e.get("name")
    + " and badkey="
    + e.get("badkey")
)

a = SOLE.Building.SimpleBuilding()
print("SimpleBuilding uuid=" + str(a.uuid()))
