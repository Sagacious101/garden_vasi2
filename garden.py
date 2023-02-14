import random


garden = ["покрышка", "бутылка", "окурок", "железяка", "череп коровы"]
garden.clear()
order = (
    ("ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис"),
    ("роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза"),
    ("пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион")
)
for package in order:
  for seed in package:
    garden.append(seed)
weeds = ("борщевик", "крапива", "лопух")
for weed in weeds:
  for i in range(random.randint(5, 10)):
    garden.append(weed)
random.shuffle(garden)
print("сад до прополки:", garden)
print("\nидентификатор сада до прополки:", id(garden))

for weed in weeds:
    while weed in garden:
        garden.remove(weed)

print("\nсад после прополки:", garden)
print("\nидентификатор сада после прополки:", id(garden))

flowers_quantity = len(garden)
print(f"\nобщее количество цветов: {flowers_quantity}")

bouquet = random.sample(garden, 5)

print(f"\nбукет: {bouquet}")
    
