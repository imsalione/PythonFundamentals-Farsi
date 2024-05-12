class Vehicle:
    def name(self, name):
        return name
    
v = Vehicle()
print(f"\nThe class name is: {v.__class__.__name__}")