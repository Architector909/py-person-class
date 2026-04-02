from typing import List, Dict, Optional


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.wife: Optional["Person"] = None
        self.husband: Optional["Person"] = None
        Person.people[name] = self


def create_person_list(
    people_dicts: List[Dict[str, Optional[str]]]
) -> List[Person]:
    person_list: List[Person] = []

    # First pass: create all Person instances
    for person_data in people_dicts:
        person_instance = Person(person_data["name"], person_data["age"])
        person_list.append(person_instance)

    # Second pass: link spouses
    for idx, person_data in enumerate(people_dicts):
        person_instance = person_list[idx]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return person_list
