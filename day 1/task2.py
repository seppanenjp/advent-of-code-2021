def depth_increase():
    with open('input.txt') as input_file:
        depths = [int(i) for i in input_file.readlines()]
        current_depth = None
        depth_increased = 0
        for index in range(len(depths) - 2):
            if (current_depth and summary(depths, index) > current_depth):
                depth_increased += 1
            current_depth = summary(depths, index)
        print(depth_increased)


def summary(depths, index):
    return depths[index] + depths[index + 1] + depths[index + 2]


if __name__ == "__main__":
    depth_increase()
