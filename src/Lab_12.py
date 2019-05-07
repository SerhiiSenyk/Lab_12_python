#Purpose:

#Порахувати сумарний розмвр файлів зображень кожного типу (в кінці стрічки запиту має бути закінчення 
#png,jpeg,jpg,gif),які були успішно повернуті клієнтам (тип запиту - GET)
#в проміжку 
#17/May/2015:21:10:44 до 19/May/2015:15:21:28

#@author Serhii Senyk , 07.05.2019
import re

def log_file_scanner(log_file_path):
    total_size_of_files_images = 0
    count_of_files_images = 0
    regex_data = '(\[1(7\/May\/2015:(21:((10:(4[4-9]|5[0-9])'+\
            '|1[1-9]:[0-5][0-9])|[2-5][0-9]:[0-5][0-9])|2[2-3](:[0-5][0-9]){2})'+\
            '|8\/May\/2015:[0-2][0-9](:[0-5][0-9]){2}|9\/May\/2015:(0[0-9](:[0-5]'+\
            '[0-9]){2}|1([0-4](:[0-5][0-9]){2}|5:([0-1][0-9]:[0-5][0-9]|2(0:[0-5]'+\
            '[0-9]|1:([0-1][0-9]|2[0-8]))))))\s\+[0-9]{4}\])'
    regex = r'[0-9.]*[\s-]*' + regex_data + '\s\"GET\s\/\/*.+\.'+\
            '(png|jpeq|jpg|gif)\s[A-Z]{4}\/\d\.\d\"\s200\s([0-9]*)'
    try:
        with open(log_file_path,'r') as log_file: 
            for line in log_file:
                result = re.search(regex, line)
                if result is not None:
                   group = 17
                   total_size_of_files_images += int(result.group(group))
                   count_of_files_images += 1
    except Exception as exception:
        print("Error : ", exception)
    else:
        print("Total size of images files : ", total_size_of_files_images,"\tbytes\t",
              total_size_of_files_images/2**20,"\tMb")
        print("Count : ", count_of_files_images)
    finally:
        print("Done")

log_file_scanner("apache_logs")