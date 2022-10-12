#First exercise
user_input = input("add you username and password all in lower case\n")
while user_input.upper() != "Stop":
    print(user_input.lower())
    user_username_and_password = str(user_input)

#Second exercise
class Salary:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return "{} has {} salary".format(self.name, self.salary)

jake1 = Salary("Jake", "$100k")
print("{}".format(jake1))
anand = Salary("Anand", "$120k")
print("{}".format(anand))

#Exercise 3

list1 = (4, 30, 2017, 2, 27)
class Numbers:

    def __str__(self):
        return "{} {} {} {} {}".format(list1[-2], list1[-1], list1[2], list1[0], list1[1])


list_1 = Numbers()
print("{}".format(list_1))







