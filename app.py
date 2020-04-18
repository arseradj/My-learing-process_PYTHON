import math
student_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(student_count)
print(rating)
print(is_published)
print(course_name)
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])
# \"
# \'
# \\
# \n
course_name1 = "Python \'Programming"
course_name2 = "Python \"Programming"
course_name3 = "Python \\Programming"
course_name4 = "Python \nProgramming"
print(course_name1)
print(course_name2)
print(course_name3)
print(course_name4)
first_name = "Ahmad Reza"
last_name = "Seradj"
full_name1 = first_name + " " + last_name
full_name2 = f"{first_name} {last_name}"
print(full_name1)
print(full_name2)
full_name3 = f"{len(first_name)} {last_name[0]}"
print(full_name3)
print(full_name2.upper())
print(full_name2)
print(full_name1.title())
print(full_name1.find("ez"))
print(full_name2.replace("ez", "EZ"))
print("Reza" in full_name1)
print("gooz" not in full_name1)
x = 10+3
y = 10-3
z = 10*3
k1 = 10/3
k2 = 10//3
print(x)
print(y)
print(z)
print(k1)
print(k2)
print(round(k1))
print(math.sqrt(k1))
a = input("a: ")
b = int(a)+1
print(f"a: {a} and b: {b}")
