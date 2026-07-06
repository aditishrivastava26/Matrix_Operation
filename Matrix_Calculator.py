#This program should be able to perform normal matrix calculations like:
#1.Addition
#2.Sutraction
#3.Multiplication

# region user input
#function for looping the user input until the input given is valid
def user_input(prompt):
    """
    for input of user rows ad columns    
    """
    value = input(prompt).strip().replace(" ", "")
    if not value:   # empty after strip/replace
        print("Input cannot be empty. Please re-enter.")    
        return user_input(prompt)   # recursive call instead of while
    try:
        return int(value)
    except ValueError:
        print("Invalid number. Please enter an integer.")
        return user_input(prompt)  # recursive call instead of while
# region Yes or no 
#function for looping the user input until the user enters yes/no
def yes_no(prompt):
    """
    for input of user for yes/no
    """
    value = input(prompt).strip().lower().replace(" ","")
    if not value: #empty after strip/replace
        print("Input cannot be empty.Please re-enter.")
        return yes_no(prompt) 
    if value in ["yes","no"]:
        return value
    else:
        print("Invalid input. Please enter yes or no.")
        return yes_no(prompt)   # recursive call
    
#=======================values for matrix-1===============================
#region main
print("matrix-1")
for _ in range(2):
    rows= user_input("enter the number of rows:")
    columns = user_input("enter the number of columns:")
    if rows == 0 or columns == 0:#condition for the matrix
        print("matrix is not possible")
        choice = yes_no("would you like to re enter the values? (yes/no): ")
        if choice.lower() == "yes":
                print("re-entering values of matrix-1")
        else:
                print("matrix-1 value = 0")
                break
    else:
        x=[]
        for i in range (rows):
            row=[]
            for j in range (columns):
                value = user_input(f"enter value for [{i}][{j}]: ")
                row.append(value)
            x.append(row)
        for row in x:
            print(row)
        break

choice = yes_no("would you like to add another matrix? (yes/no): ")
# initialize y
y=[]
if choice.lower() == "yes":
#==========================values for matrix-2=====================================
    print("adding another matrix")
    print("matrix-2")
    for _ in range(2):
        rows = user_input("enter the number of rows:") 
        columns = user_input("enter the number of columns:")
        if rows == 0 or columns == 0:#condition for the matrix
            print("matrix is not possible")
            choice = yes_no("would you like to re enter the values? (yes/no): ")
            if choice.lower() == "yes":
                print("re-entering values of matrix-2")
            else:
                print("matrix-2 value = 0")
                break
        else:    
            y=[]
            for i in range (rows):
                row=[]
                for j in range (columns):
                    value = user_input(f"enter value for [{i}][{j}]: ")
                    row.append(value)
                y.append(row)
            for row in y:
                print(row) 
            break
else:
    print("exiting the program") 
    print("thank you for using the program")
    exit()

print("The matrices are:")
print("Matrix-1\t\tMatrix-2")

for i in range(max(len(x), len(y))):
    left = str(x[i]) if i < len(x) else ""
    right = str(y[i]) if i < len(y) else ""
    print(f"{left:<20} {right}")

#===================variables used for the operations========================================
rows_x = len(x)
columns_x = len(x[0])   
rows_y = len(y)
columns_y = len(y[0])  

#===================operation to be performed by the matrix==================================
for _ in range(5):
    choice = yes_no(" would like to perform any operations on the matrices? (yes/no):")
    if choice.lower() == "yes":                    
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. exit")
        operation = user_input("Enter the number corresponding to the operation you want to perform: ")
        #==================1.Addition=====================
        if operation == 1:
            print("addition of matrices")
            if  rows_x != rows_y or columns_x != columns_y:#condition for adddition
                print("Matrix addition is not possible")    
            else:
                addition=[]
                for i in range (rows_x):
                    new_row=[]
                    for j in range (columns_x):
                        value = x[i][j] + y[i][j]
                        new_row.append(value)
                    addition.append(new_row)
                print("addition of two matrix is:")
                for rows in addition:
                    print(rows)     
        #===================2.Subtraction=======================
        elif operation == 2:
            print("subtraction of matrices")
            if  rows_x != rows_y or columns_x != columns_y:#condition for subtraction
                print("Matrix subtraction is not possible")    
            else:
                subtraction=[]
                for i in range (rows_x):
                    new_row=[]
                    for j in range (columns_x):
                        value = x[i][j] - y[i][j]
                        new_row.append(value)
                    subtraction.append(new_row)
                print("subtraction of two matrix is:")
                for rows in subtraction:
                    print(rows)
        #===================3.Multiplication=====================
        elif operation == 3:
            print("multiplication of matrices")
            if columns_x != rows_y:#consition for multiplication
                print("Matrix multiplication is not possible")    
            else:
                multiplication=[]
                for i in range (rows_x):
                    new_row=[]
                    for j in range (columns_y):
                        value = 0
                        for k in range(columns_x):
                            value += x[i][k] * y[k][j]
                        new_row.append(value)
                    multiplication.append(new_row)
                print("multiplication of two matrix is:")
                for rows in multiplication:
                    print(rows)  
        #===================4.Exit================================
        elif operation == 4:
            print("Thank you for using the program") 
            break     
        elif operation >= 5:
            print("please choose from among the options")   
                 
    else:
        print("exiting the program")
        print("thank you for using the program")
        break