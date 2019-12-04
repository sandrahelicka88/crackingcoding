import unittest
class Animal:
    def __init__(self):
        self.timestamp = 0
        

class Dog(Animal):
    pass
class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.animalnumber = 0
    def enqueue(self, pet):
        self.animalnumber+=1
        pet.timestamp = self.animalnumber
        if isinstance(pet, Dog):
            self.dogs.append(pet)
        else:
            self.cats.append(pet)
    def dequeueCat(self):
        if self.cats == []:
            raise IndexError('No cats left')
        else:
            return self.cats.pop(0)
    def dequeueDog(self):
        if self.dogs == []:
            raise IndexError('No dogs left') 
        else:
            return self.dogs.pop(0)
    def dequeueAny(self):
        if self.cats == [] and self.dogs==[]:
            raise IndexError('No animal in the shelter')
        elif self.dogs == []:
            return self.cats.pop(0)
        elif self.cats == []:
            return self.dogs.pop(0)
        else:
            firstcat = self.cats.pop(0)
            firstdog = self.dogs.pop(0)
            if firstdog.timestamp < firstcat.timestamp and self.dogs != []:
                adopted_pet = self.dogs.pop(0)
            else:
                adopted_pet = self.cats.pop(0)
            print(adopted_pet)

class Test(unittest.TestCase):
    def test_shelter(self):
        shelter = AnimalShelter()
        cat1 = Cat()
        dog1 = Dog()
        cat2 = Cat()
        dog2 = Dog()
        shelter.enqueue(cat1)
        shelter.enqueue(dog1)
        shelter.enqueue(cat2)
        shelter.enqueue(dog2)
        self.assertEqual(shelter.dequeueAny(),cat1)
        self.assertEqual(shelter.dequeueDog(),dog1)
        


if __name__ == '__main__':
    unittest.main()




