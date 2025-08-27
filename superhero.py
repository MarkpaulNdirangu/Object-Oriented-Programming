# Assignment 1: Design Your Own Class (Superhero)
class Superhero:
    """Base class for a superhero with encapsulated attributes."""
    def __init__(self, name, secret_identity, power_level):
        self._name = name  # Encapsulated attribute
        self._secret_identity = secret_identity
        self._power_level = max(0, min(power_level, 100))  # Ensure power level is 0-100
        self._is_active = True

    # Getter for encapsulated name
    @property
    def name(self):
        return self._name

    # Setter with validation
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Superhero name cannot be empty!")
        self._name = value

    # Method to display superhero info
    def display_info(self):
        return f"Superhero: {self._name}, Secret Identity: {self._secret_identity}, Power Level: {self._power_level}"

    # Polymorphic method for ability (to be overridden)
    def use_ability(self):
        return f"{self._name} uses a generic ability!"

    # Method to toggle active status
    def toggle_active(self):
        self._is_active = not self._is_active
        return f"{self._name} is {'active' if self._is_active else 'retired'}."

# Assignment 2: Polymorphism Challenge with Inherited Classes
class FireHero(Superhero):
    """A superhero with fire-based abilities."""
    def __init__(self, name, secret_identity, power_level, flame_intensity):
        super().__init__(name, secret_identity, power_level)
        self._flame_intensity = flame_intensity  # Additional attribute

    def use_ability(self):
        return f"{self._name} unleashes a fiery blast with intensity {self._flame_intensity}!"

class FlightHero(Superhero):
    """A superhero with flight-based abilities."""
    def __init__(self, name, secret_identity, power_level, max_altitude):
        super().__init__(name, secret_identity, power_level)
        self._max_altitude = max_altitude

    def use_ability(self):
        return f"{self._name} soars to {self._max_altitude} feet in the sky!"

# Demonstration of the classes
def main():
    try:
        # Create superhero instances
        torch = FireHero("Blaze", "John Smith", 85, 10)
        sky = FlightHero("Skywing", "Jane Doe", 90, 30000)

        # Display information
        print(torch.display_info())
        print(sky.display_info())

        # Demonstrate polymorphism with use_ability
        print("\nPolymorphic Abilities:")
        heroes = [torch, sky]
        for hero in heroes:
            print(hero.use_ability())

        # Demonstrate encapsulation
        print("\nTesting Encapsulation:")
        torch.name = "Inferno"  # Using setter
        print(torch.display_info())
        
        # Test invalid name
        try:
            torch.name = ""  # Should raise ValueError
        except ValueError as e:
            print(f"Error: {e}")

        # Demonstrate active status toggle
        print("\nStatus Toggle:")
        print(torch.toggle_active())
        print(sky.toggle_active())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
