def rectangle_stats(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

   # not where int is needed  return int(area, perimeter)
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

    #rect_area = length * width
    #rect_perimeter = 2 * length + width

#area = rectangle_stats(rect_area)
#perimeter = rectangle_stats(rect_perimeter)
   

area, perimeter = rectangle_stats(length, width)

print(f"The area of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")

#area = rectangle_stats(area)
#perimeter = rectangle_stats(length)

#rect_area, rect_perimeter = rectangle_stats(length, width)

#print(f"The area of the rectangle is: {rect_area:.2f}")
#print(f"The perimeter of the rectangle is: {rect_perimeter:.2f}")



