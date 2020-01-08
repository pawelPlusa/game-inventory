
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.


def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    for i in inventory:
        print(f"{i}: {inventory[i]}")
    pass


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    for i in added_items:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory[i]=1
    

def check_lenght_of_key_in_inv(inventory):
    left_intend = 9
    for i in inventory:
        if len(i) > left_intend:
            left_intend = len(i)
    #print(f"final key intend is: {left_intend}")
    return left_intend

def check_lenght_of_value_in_inv(inventory):
    right_intend = 5
    values = inventory.values()
    # [(right_intend = len(str(i))) if len(str(i)) > right_intend else right_intend for i in values]
    for i in values:
        if len(str(i)) > right_intend:
            right_intend = len(str(i))
    #print(right_intend)
    return right_intend

def check_overall_lenght(inventory):
    central_space = 3
    overall_len = check_lenght_of_key_in_inv(inventory) + check_lenght_of_value_in_inv(inventory) + central_space
    #print(overall_len)
    return overall_len

def print_dashes(inventory):
    dash_len = check_overall_lenght(inventory)
    dash = ("-" * dash_len)
    return dash

def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''
    key_just_val = check_lenght_of_key_in_inv(inventory)
    val_just_val = check_lenght_of_value_in_inv(inventory) 
    printable_inventory=[]
    nl = "\n"
    if order == "count,desc":
        sorted_dict=sorted(inventory.items(), key=lambda value: value[1], reverse=True)
    elif order == "count,asc":
        sorted_dict=sorted(inventory.items(), key=lambda value: value[1])
    else:
        sorted_dict = inventory.items()
    for i in sorted_dict:
        #print(i)
        inv_line = (f"{i[0].rjust(key_just_val)} | {str(i[1]).rjust(val_just_val)}")
        #print(aaa)
        printable_inventory.append(inv_line)
        #printable_inventory.append(nl)
    line = print_dashes(inventory)
    header = "item name".rjust(key_just_val) + " | " + "count".rjust(val_just_val)
    # print(header)
    print(f"{line}{nl}{header}{nl}{line}{nl}{nl.join(printable_inventory)}{nl}{line}")
    

def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def write_table_to_file(file_name, table):
    """
    Writes list of lists into a csv file.

    Args:
        file_name (str): name of file to write to
        table (list): list of lists to write to a file

    Returns:
         None
    """
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''
    # file = open(filename, "r")
    with open(filename, "r") as file:
        imported_items=[]
        line = (file.read().split(","))
        s = ", "
        print(f"New items in inventory: {s.join(line)}")
        add_to_inventory(inventory,line)



def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''
    item_list=[]
    for key_inv in inventory:
        n = inventory[key_inv]
        #print(f"n is {n}")
        for i in range(n):
            item_list.append(key_inv)
    #print(item_list)
    file = open(filename, "w")
    file.write(",".join(item_list))
    file.close()

def print_table2(inventory, order = 0):
    key_just_val = check_lenght_of_key_in_inv(inventory)
    val_just_val = check_lenght_of_value_in_inv(inventory) 
    just_len = len(inventory)
    headers = f"item name |  count"
    temp = []
    if just_len < len("item name"):
        just_len = len("item name")
    for i in inventory:
        #print(f"{i.rjust(just_len)} | {str(inventory[i]).rjust(5)}")
        aaaa = (f"{i.rjust(key_just_val)} | {str(inventory[i]).rjust(val_just_val)}")
        temp.append(aaaa)
    print(temp)
    #overall_lenght = check_max_str_len_in_list(temp)
    line = "-----------"
    new_line = "\n"
    print(f"{line}\n{headers}\n{line}\n{new_line.join(temp)}")
    print(line)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(inv)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, dragon_loot)

# check_lenght_of_value_in_inv(inv)
# check_overall_lenght(inv)
print_dashes(inv)
print_table(inv, "count,desc")
#print_table2(inv)
import_inventory(inv, "test_inventory.csv")
print_table(inv, "count,desc")
#print(inv)
export_inventory(inv)