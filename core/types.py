from typing import TypedDict 

class Rule(TypedDict):
    identifier: int
    normal_value: float
    current_value: float


class Rules(TypedDict):
    rules: list[Rule]
