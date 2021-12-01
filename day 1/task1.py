def list_depths():
    with open('depths.txt') as rows:
        current_depth = None
        depth_increased = 0
        for depth in [int(i) for i in rows.readlines()]:
            if (current_depth and depth > current_depth):
                depth_increased += 1
            current_depth = depth
        print(depth_increased)

if __name__ == "__main__":
    list_depths()