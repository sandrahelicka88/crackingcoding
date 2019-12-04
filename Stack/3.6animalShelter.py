import datetime
import unittest
class Animal:
    def __init__(self,name):
        self.name = name
    

class Dog(Animal):
    pass
class Cat(Animal):
    pass
    

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self,pet):
        pet.enter = datetime.datetime.now()
        if isinstance(pet,Dog):
            self.dogs.append(pet)
        else:
            self.cats.append(pet)
    def dequeueCat(self):
        if self.cats == []:
            print('No cats left')
        else:
            return self.cats.pop(0)
    def dequeueDog(self):
        if self.dogs == []:
            print('No dogs left') 
        else:
            return self.dogs.pop(0)
    def dequeueAny(self):
        if self.cats == [] and self.dogs!=[]:
            return self.dogs.pop(0)
        elif self.dogs == [] and self.cats!=[]:
            return self.cats.pop(0)
        elif self.dogs == [] and self.cats == []:
            print('No animals in the shelter')
        else:
            firstCat = self.cats[0]
            firstDog = self.dogs[0]
            if firstCat.enter<firstDog.enter:
                return self.cats.pop(0)
            else:
                return self.dogs.pop(0)

class Test(unittest.TestCase):
    def test_shelter(self):
        shelter = AnimalShelter()
        cat1 = Cat('Fryzia')
        dog1 = Dog('Benio')
        shelter.enqueue(cat1)
        shelter.enqueue(dog1)
        self.assertEqual(shelter.cats[0].name,'Fryzia')
        self.assertEqual(shelter.dogs[0].name, 'Benio')
        cat2 = Cat('Cukierek')
        dog2= Dog('Reksio')
        cat3 = Cat('Bat')
        shelter.enqueue(cat2)
        shelter.enqueue(dog2)
        shelter.enqueue(cat3)
        self.assertEqual(shelter.dequeueDog().name, 'Benio' )
        self.assertEqual(shelter.dequeueCat().name, 'Fryzia')
        dog3 = Dog('Bush')
        shelter.enqueue(dog3)
        self.assertEqual(shelter.dequeueAny().name, 'Cukierek' )
        self.assertEqual(shelter.dequeueAny().name, 'Reksio')


if __name__ == '__main__':
    unittest.main()



        




