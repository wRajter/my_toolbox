from random import choice

def dino_name():
    dino_names = ['Tyrannosaurus Rex', 'Stegosaurus', 'Triceratops', 'Velociraptor', 'Spinosaurus', 'Allosaurus', 'Archaeopteryx', 'Megalosaurus']
    print(f'Hi! If you were a dinosaurus, you would be {choice(dino_names)}. RAWRRR')


def dino_type():
    types = ['theropods', 'sauropods', 'stegosaurs', 'ankylosaurs', 'ornithopods', 'ceratopsians', 'pachycephalosaurs']
    return choice(types)
