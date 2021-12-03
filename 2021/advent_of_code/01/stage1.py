
def question_1_part_1():
    with  open("depth.txt", "r") as text_file:
        depths = text_file.read().splitlines()
        depth_increase=0
        depth_decrease=0

        for depth_value in range(len(depths) - 1):
            if int(depths[depth_value]) < int(depths[depth_value + 1]):
                depth_increase += 1
            else:
                depth_decrease += 1
    print("Part 1")
    print("Total Times Depth Increased ", depth_increase)
    print("Total Times Depth Decreased ", depth_decrease)

def question_1_part_2():
    with  open("depth.txt", "r") as text_file:
        depths = text_file.read().splitlines()
        depth_increase=0
        depth_decrease=0

        for depth_value in range(len(depths) - 3):
            if int(depths[depth_value]) < int(depths[depth_value + 3]):
                depth_increase += 1
            else:
                depth_decrease += 1
    print("Part 2")
    print("Total Times Depth Increased ", depth_increase)
    print("Total Times Depth Decreased ", depth_decrease)


def question_1_simple():
    data = [int(x) for x in open("depth.txt", "r")]
    print("Part 1:", sum([data[i] > data[i-1] for i in range(1, len(data))]))
    print("Part 2:", sum([data[i] > data[i-3] for i in range(3, len(data))]))



question_1_part_1()
question_1_part_2()
question_1_simple()
