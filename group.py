"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"members": [
            {"name": "Jill", "age": 26, "Job": "Biologist",},
            {"name": "Zalika", "age": 28, "Job": "Artist", },
            {"name": "John", "age": 27, "Job": "Writer", },
            {"name": "Nash", "age": 34, "Job": "Chef", }],

            "relationships": [    
                {"type": "partners", "persons": ("Jill", "Zalika")},
                {"type": "friends", "persons": ("Jill", "John")},
                {"type": "cousins", "persons": ("Nash", "John")},
                {"type": "landlord", "landlord": "Nash", "tenant": "Zalika"}]
}

print(my_group["relationships"][3]["tenant"]) # Output: Zalika