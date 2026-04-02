class Person:
    # Class attribute to store all instances by name
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # Automatically add the instance to the class dictionary
        Person.people[name] = self

def create_person_list(people_data: list) -> list:
    # Clear the class attribute to ensure a fresh start for each function call
    Person.people = {}

    # Phase 1: Create all Person instances
    # This populates Person.people so we can look up spouses later
    for p_dict in people_data:
        Person(p_dict["name"], p_dict["age"])

    # Phase 2: Assign spouse attributes and build the return list
    result = []
    for p_dict in people_data:
        person_instance = Person.people[p_dict["name"]]

        # Check for 'wife' or 'husband' keys
        for spouse_key in ["wife", "husband"]:
            if spouse_key in p_dict:
                spouse_name = p_dict[spouse_key]
                if spouse_name is not None:
                    # Set the attribute as a reference to the existing Person object
                    setattr(person_instance, spouse_key, Person.people[spouse_name])

        result.append(person_instance)

    return result
