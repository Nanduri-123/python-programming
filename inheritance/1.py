class Animal:
    def __init__(self,habitat):
        self.habitat = habitat

    def get_habitat(self):
        return self.habitat
class Dog(Animal):
    def __init__(self,habitat,breed):
        super().__init__(habitat)
        self.breed = breed

    def get_details(self):
        return (f"This dog is a {self.breed} and lives in {self.get_habitat()}")
    
my_dog = Dog('House', 'Labrador')

print(my_dog.get_details)
