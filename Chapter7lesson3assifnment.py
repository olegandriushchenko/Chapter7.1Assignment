
class Zoo:
    def __init__(self):
        self.zoo_employees = ["John"]
        self.zoo_animal = {"squirrel": 3}
        self.animal_count = 3

    def add_animal(self, animal = "squirrel"):
        if self.animal_count / len(self.zoo_employees) > 10:
            print("Not enough employees for all animals! Hire someone new!")
            return

        if animal in self.zoo_animal.keys():
            self.zoo_animal[animal] += 1
            self.animal_count += 1
        else:
            self.zoo_animal[animal] = 1
            self.animal_count += 1

        if self.animal_count / len(self.zoo_employees) > 10:
            print("Not enough employees for all animals! Hire someone new!")
    def remove_animals(self, animal):
        if animal not in self.zoo_animal.keys():
            print("Zoo doesn`t have {}".format(animal))
        else:
            self.zoo_animal[animal] -= 1

    def hire_new_employee(self, new_employee):
        self.zoo_employees.append(new_employee)
        print("{} welcome!".format(new_employee))

    def fire_employee(self, employee = None):
        if employee is None:
            self.zoo_employees.pop()
        else:
            self.zoo_employees.remove(employee)

    def __str__(self):
        output = "Animals\n"
        for animal, quantity in self.zoo_animal.items():
            output = output + animal + ":" + str(quantity) + "\n"
        output = output + "Employees:\n"
        for employee in self.zoo_employees:
            output = output + employee + "\n"
        return ""
zoo = Zoo()
zoo.add_animal("Lion")
zoo.add_animal("Bear")
zoo.add_animal("Lion")

zoo.add_animal()
zoo.add_animal()
zoo.add_animal("fox")
zoo.add_animal("rabbit")
zoo.add_animal("Elephant")

#print(zoo)

zoo.hire_new_employee("Oleg")
zoo.hire_new_employee("Max")
zoo.fire_employee("Alex")
zoo.fire_employee()

print(zoo)



#exercise 2
def compute_patterns(inputs = [], patterns = "new pattern"):
    inputs.append(patterns)
    patterns = ["a list based on "] + inputs
    return patterns