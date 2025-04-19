class Pet:
    def __init__(self, name, hunger=5, energy=5, happiness=5):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []  # Bonus: a list to store learned tricks

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(self.hunger - 3, 0)
            self.happiness = min(self.happiness + 1, 10)
            print(f"{self.name} ate and feels energized! ")
        else:
            print(f"{self.name} is already full!")

    def sleep(self):
        if self.energy < 10:
            self.energy = min(self.energy + 5, 10)
            print(f"{self.name} slept well. ")
        else:
            print(f"{self.name} is already fully rested!")

    def play(self):
        if self.energy > 0:
            self.energy = max(self.energy - 2, 0)
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} had fun playing! ")
        else:
            print(f"{self.name} had a blast running around!")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} learned a new trick: {trick}! ")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"\n {self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10\n")