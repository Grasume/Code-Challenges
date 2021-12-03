def question_2_part_1():
    with  open("movement.txt", "r") as text_file:
        position = text_file.read().splitlines()

        horizontal_position = 0
        depth_position = 0

        for location in position:
            if "forward" in location:
                horizontal_position += int(''.join(filter(str.isdigit, location)))

            elif "down" in location:
                depth_position += int(''.join(filter(str.isdigit, location)))

            elif "up":
                depth_position -= int(''.join(filter(str.isdigit, location)))

    print("Part 1")
    print("Horizontal Ending Position ", horizontal_position)
    print("Depth Ending Position ", depth_position)
    print("Final Depth Ending Position ", horizontal_position * depth_position)

def question_2_part_2():
    with open("movement.txt", "r") as text_file:
        position = text_file.read().splitlines()

        aim_position = 0
        horizontal_position = 0
        depth_position = 0

        for location in position:
            if "forward" in location:
                horizontal_position += int(''.join(filter(str.isdigit, location)))
                depth_position += int(''.join(filter(str.isdigit, location))) * aim_position
            elif "down" in location:
                aim_position += int(''.join(filter(str.isdigit, location)))

            elif "up":
                aim_position -= int(''.join(filter(str.isdigit, location)))

    print("Part 2")
    print("Horizontal Ending Position ", horizontal_position)
    print("Depth Ending Position ", depth_position)
    print("Aim Ending Position ", aim_position)
    print("Final Depth Ending Position ", horizontal_position * depth_position)





question_2_part_1()
question_2_part_2()
