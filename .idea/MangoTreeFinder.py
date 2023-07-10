# Creation of function which states whether tree is a Mango Tree or not
def is_mango_tree(rows, columns, tree_number) :
    if tree_number % columns == 1 or tree_number <= columns and tree_number > 0 or tree_number % columns == 0 :
        return True
    return False
try :
    rows = int(input("Enter the number of Rows : "))
    columns = int(input("Enter the number of Columns : "))
    tree_number = int(input("Enter the tree Number : "))

    print(is_mango_tree(rows, columns, tree_number))

except ValueError :                       # Accept only valid inputs else handles exception
    print("Invalid Input!!! Please Enter Integers Only that are greater than 0")


