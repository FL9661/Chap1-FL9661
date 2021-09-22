### 3.2.1.14 - building pyramid blocks  - HELP NEEDED HERE ###
blocks = int(input("Enter the number of blocks: "))
height = 0
in_layer = 1
while in_layer <= blocks: # while layer is less than or equal to blocks
    height += 1 # hieght = height + 1
    blocks -= in_layer # blocks = blocks - in layer
    in_layer += 1 # in_layer = inlayer + 1
print("The height of the pyramid:", height)
print("The length of the pyramid:", in_layer)
#YouTube help used but I still did not understand
#height works out correct but the length is incorrect