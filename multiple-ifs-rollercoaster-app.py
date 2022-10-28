#multiple if statements (conditions)
#  in a single if statement block of code, we are only checking the first "if" as true/false, and then only performing the "elif" and/or "else" when the "if" is false
#  with multiple "if" "if" "if" statements, we evaluate each "if" as true or false and perform each subsequent operation independently (such as if y: print("xxxxx") for each "if")
#  example block of multiple "if" code:
#    if condition1:
#        do A
#    if condition2:
#        do B 
#    if condition3:
#        do C 
# example code below --->

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  # line 30 needs to be on the SAME INDENT as the "if" code block starting on line 20, because in this program, the rider cannot have a photo taken if they are too short to ride the rollercoaster, AND because photos cost an extra $3, we FIRST need to figure out how much their initial ticket costs based on their AGE, and only IF they want a photo, add $3 to the cost of the base ticket. that is why the "wants_photo" variable and input statement need to be on the indentation as "if age < 12:".
  if wants_photo == "Y":
    bill += 3 #adds $3 to the bill if wants_photo = Y
    # "bill +=3" is the same thing as "bill = bill + 3"
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
