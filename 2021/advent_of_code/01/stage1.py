

with  open("input.txt", "r") as text_file:
    depths = text_file.read().splitlines()

    depth_increase=0
    depth_decrease=0

    for depth_value in range(len(depths) - 1):
        if int(depths[depth_value]) < int(depths[depth_value + 1]):
            depth_increase += 1
            #print("Increasing")
        else:
            depth_decrease += 1
            #print("Decreasing")

print("Total Times Depth Increased ", depth_increase)
print("Total Times Depth Decreased ", depth_decrease)

with open("input.txt", "r") as f:
    depths = f.read().splitlines()

count = 0
for i in range(len(depths) - 1):
    if int(depths[i]) < int(depths[i + 1]):
        count += 1
print(count)

with open("input.txt", "r") as f:
    depths = f.readlines()

count = 0
for i, num in enumerate(depths[:-1]):
    if int(num) < int(depths[i + 1]):
        count += 1

print(count)


text_file = open("input.txt", "r")
depth = text_file.readlines()
#depth = map(lambda s: int(s.strip()), depth)
text_file.close()
depthlength=len(depth)
increase=0
decrease=0
for index in range(1,depthlength):
    if depth[index]>depth[index-1]:
        increase=increase+1
    elif depth[index]<depth[index-1]:
        decrease=decrease+1
print("Increases: {}\nDecreases: {}".format(increase,decrease))
