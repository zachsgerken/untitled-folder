import dog

dog1 = dog.Dog('Fido', 3)

dog2 = dog.Dog('Lassie', 5, 'Collie')

dog3 = dog.Dog('Ginger', 5, 'Weiner Dog')

dog4 = dog.Dog("Sienna", 7, "Visla")

dogs = []

dogs.append(dog1)
dogs.append(dog2)
dogs.append(dog3)
dogs.append(dog4)

for dog in dogs:
    print(dog.bark())
