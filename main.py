from pet import Pet

# Create your pet
my_pet = Pet("Max")
print(f"Creating pet: {my_pet.name} 🐕\n")

# Simulate actions
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.train("play dead")

# Display status
my_pet.get_status()
my_pet.show_tricks()

