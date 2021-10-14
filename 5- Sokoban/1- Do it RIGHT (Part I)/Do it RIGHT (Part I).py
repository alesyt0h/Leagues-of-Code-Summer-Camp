from typing import List

state1 = [
["#", "#", "#", "#", "#", "#", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", " ", " ", "@", " ", " ", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", "#", "#", "#", "#", "#", "#"],
]

state2 = [
["#", "#", "#", "#", "#", "#", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", " ", " ", "@", "#", " ", "#"],
["#", " ", " ", " ", " ", " ", "#"],
["#", "#", "#", "#", "#", "#", "#"],
]


def go_right(state: List[List[str]]) -> None:
    for value in state:
        for index,char in enumerate(value):
            if char == "@" and value[index + 1] == " ":
                value[index] = " "
                value[index + 1] = char
                break
    
    return state

go_right(state1)
print(state1)

print("-----------------------------")

go_right(state2)
print(state2)