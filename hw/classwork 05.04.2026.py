class Animal:
    def __init__(self,name , type, sound)-> None:
        self.name = name
        self.type = type
        self.sound =sound
    def make_sound(self):
        print(f'Animal named {self.name} makes sound {self.sound}')
        def __str__(self) -> str:
            return f'Animal(name={self.name}, type={self.type}, sound={self.sound})'
animal1 =Animal('Buddy', 'dog', 'WOOF')
animal1.make_sound()
print(animal1.type)
animal2 = Animal('Marcel', 'cat', 'MEOW')
print(animal2.type)
print(type(animal1))
print (animal1,animal2,sep='\n')
animal2.make_sound()
