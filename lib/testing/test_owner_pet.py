class Pet:
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        Pet.all.append(self)

    @classmethod
    def get_all(cls):
        return cls.all

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added.")
        self._pets.append(pet)

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


# 
def test_get_sorted_pets():
    """Test Owner class has method get_sorted_pets, sorting related pets by name"""
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)

    assert owner.get_sorted_pets() == [pet2, pet1, pet4, pet3]
