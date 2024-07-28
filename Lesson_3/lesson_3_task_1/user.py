class User:
    def __init__(self, first_name, second_name):

       self.first_name = first_name
       self.second_name = second_name

    def my_first_name(self):
        print("First_name:", self.first_name)

    def my_second_name(self):
        print("Second_name:", self.second_name)

    def my_full_name(self):
        print("Full_name:", self.first_name, self.second_name)

