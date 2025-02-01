class Animal:
    alive = []

    def __str__() -> str:
        return [{"Name": animal.name, "Health": animal.health, "Hidden": animal.hidden} for animal in Animal.alive]

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)
        print(f"{self.name}, total animals: {len(Animal.alive)}")

        pass

    def getbitten(self) -> None:
        pass

    def __iter__(self):
        yield self.strings
        yield "something else"



class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        animal.getbitten()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
    
    def getbitten(self) -> None:
        if not self.hidden:
            self.health -= 50
            if self.health <= 0:
                Animal.alive.remove(self)

    def getbitten(self) -> None:
        if not self.hidden:
            self.health -= 50
            if self.health <= 0:
                Animal.alive.remove(self)


wolf = Carnivore("Azor")
sheep = Carnivore("Beza")

print(Animal.alive)
print(Animal.__str__())