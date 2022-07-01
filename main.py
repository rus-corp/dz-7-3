from csv import list_dialects
import os
from unittest.util import sorted_list_difference 

file_name = '4.txt'

list_of_files = os.listdir('files')
list_dict = {}
for file in list_of_files:
    # print(file)
    with open(f'files\{file}', encoding='utf8') as f:
        content = f.readlines()
        list_dict[file] = content


# new_file = str(sorted_dict)
with open(file_name, 'w', encoding='utf8') as file:
    for key, value in sorted(list_dict.items(), key = lambda item: len(item[1])):
        file.write(key+ '\n')
        file.write("Строк: "+ str(len(value))+ '\n')
        for v in value:
            file.write(v)
        file.write('\n\n')



            



        

        

        
        


