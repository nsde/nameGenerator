import random

# Words included in the name
words = [
    "Shadow", "Neo", "Vision", "Sound", "Delta", "Alpha", "Byte", "Spider", "Wolf", "Ninja", "Samurai", ""
    ]


def generate(max_length=7, names_to_generate=20):
    names = []
    for _ in range(names_to_generate):
        # Generate name
        name = ""
        while len(name) <= max_length:
            name += random.choice(words)

        names.append(name)
    return names


for name in generate():
    print(name)