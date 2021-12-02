def depth_increase():
    with open('input.txt') as input_file:
        current_depth = None
        depth_increased = 0
        for depth in [int(i) for i in input_file.readlines()]:
            if (current_depth and depth > current_depth):
                depth_increased += 1
            current_depth = depth
        print(depth_increased)


if __name__ == "__main__":
    depth_increase()
