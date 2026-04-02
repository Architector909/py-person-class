from typing import List, Dict, Optional


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(
    people_dicts: List[Dict[str, Optional[str]]]
) -> List[Person]:
    person_list: List[Person] = [
        Person(p["name"], p["age"]) for p in people_dicts
    ]

    for idx, p in enumerate(people_dicts):
        person_instance = person_list[idx]

        wife_name = p.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        husband_name = p.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return person_list
