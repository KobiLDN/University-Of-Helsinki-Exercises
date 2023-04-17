# Write your solution here
person = str(input("Whom should I sign this to: "))
file_location = str(input("Where shall I save it: "))


with open(file_location, "w") as my_file:
    my_file.write(f"Hi {person}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")