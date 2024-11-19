import string 

def combination_code():
    pass 

# to bring all the alphabets, there is an string library. 
first_list = string.ascii_uppercase
second_list = string.ascii_uppercase
third_list = string.ascii_uppercase
 
# Single double and triple for loops without nesting them  

single_letters = [x for x in first_list]
double_letters = [x+y for x in first_list for y in second_list]
triple_letters = [x+y+z for x in first_list for y in second_list for z in third_list]

final_list = single_letters + double_letters + triple_letters

# Very important list hashing. Just keep it here. 
hash_map = {item:index+1 for index, item in enumerate(final_list)}

print(hash_map["ABC"])