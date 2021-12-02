from functools import reduce


class Position:
    x: int = 0
    y: int = 0
    aim: int = 0


class Movement:
    def __init__(self, direction, amount):
        self.direction = direction
        self.amount = amount

    direction: str
    amount: int


def position():
    with open('input.txt') as input_file:
        final_position = reduce(
            lambda a, b: update_position(a, str_to_movement(b)), input_file.readlines(), Position)
        print(final_position.x * final_position.y)


def update_position(current_position: Position, movement: Movement):
    match movement.direction:
        case "up":
            current_position.y -= movement.amount
        case "down":
            current_position.y += movement.amount
        case "forward":
            current_position.x += movement.amount
    return current_position


def str_to_movement(input_value: str):
    split_value = input_value.split(" ")
    return Movement(split_value[0], int(split_value[1]))


if __name__ == "__main__":
    position()
