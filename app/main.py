from typing import List, Dict, Optional

class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:  # тип повернення доданий
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_dicts: List[Dict[str, Optional[str]]]) -> List[Person]:
    person_list: List[Person] = []
    for p in people_dicts:
        person = Person(p["name"], p["age"])
        person_list.append(person)

    for i, p in enumerate(people_dicts):
        person = person_list[i]
        if "wife" in p and p["wife"] is not None:
            setattr(person, "wife", Person.people[p["wife"]])
        if "husband" in p and p["husband"] is not None:
            setattr(person, "husband", Person.people[p["husband"]])

    return person_list
