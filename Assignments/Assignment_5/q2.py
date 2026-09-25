def rectangle_stats(length,width):
    area = length * width
    perimeter = 2 * (length + width)
   # not where int is needed  return int(area, perimeter)
    

user_length = input("Enter the length of the rectangle: ")
user_width = input("Enter the width of the rectangle: ")

#area = rectangle_stats(area)
#5perimeter = rectangle_stats(length)

rect_area, rect_perimeter = rectangle_stats(user_length, user_width)

print(f"The area of the rectangle is: {area:.2f}")
print(f"The perimeter of the rectangle is: {perimeter:.2f}")



