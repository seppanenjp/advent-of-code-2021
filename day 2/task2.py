from functools import reduce
from task1 import Position, Movement, str_to_movement


def position():
    with open('input.txt') as input_file:
        final_position = reduce(
            lambda a, b: update_position(a, str_to_movement(b)), input_file.readlines(), Position)
        print(final_position.x * final_position.y)


def update_position(current_position: Position, movement: Movement):
    match movement.direction:
        case "up":
            current_position.aim -= movement.amount
        case "down":
            current_position.aim += movement.amount
        case "forward":
            current_position.x += movement.amount
            current_position.y += current_position.aim * movement.amount
    return current_position


if __name__ == "__main__":
    position()
