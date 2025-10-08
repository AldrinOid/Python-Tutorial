my_list = [1,2,3]

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl
new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)


def get_area_of_rectangle(length, width):
    area = length * width
    return area

lenghtRectangle = float(input("Input here the lenth of the rectangle: "))
widthRectangle = float(input("Input here the width of the rectangle: "))

print(f"The area of the rectangle is {get_area_of_rectangle(lenghtRectangle, widthRectangle)}. It's amazing!")


