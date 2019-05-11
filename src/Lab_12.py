#Purpose:

#Порахувати сумарний розмвр файлів зображень кожного типу (в кінці стрічки запиту має бути закінчення 
#png,jpeg,jpg,gif),які були успішно повернуті клієнтам (тип запиту - GET)
#в проміжку 
#17/May/2015:21:10:44 до 19/May/2015:15:21:28

#@author Serhii Senyk , 07.05.2019
import re

def log_file_scanner(log_file_path):
   
    regex_data = '(\[1(7\/May\/2015:(21:((10:(4[4-9]|5[0-9])'+\
            '|1[1-9]:[0-5][0-9])|[2-5][0-9]:[0-5][0-9])|2[2-3](:[0-5][0-9]){2})'+\
            '|8\/May\/2015:[0-2][0-9](:[0-5][0-9]){2}|9\/May\/2015:(0[0-9](:[0-5]'+\
            '[0-9]){2}|1([0-4](:[0-5][0-9]){2}|5:([0-1][0-9]:[0-5][0-9]|2(0:[0-5]'+\
            '[0-9]|1:([0-1][0-9]|2[0-8]))))))\s\+[0-9]{4}\])'

    regex = re.compile(r'[0-9.]*[\s-]*' + regex_data + '\s\"GET\s\/\/*.+\.'+\
            '(png|jpeg|jpg|gif)\s[A-Z]{4}\/\d\.\d\"\s200\s([0-9]*)')

    total_size_of_all_files_images = 0
    count_of_all_files_images = 0
    total_size_png = 0
    total_size_jpeg = 0
    total_size_jpg = 0
    total_size_gif = 0

    try:
        with open(log_file_path, 'r') as log_file: 
            for line in log_file:
                result = re.search(regex, line)
                if result is not None:
                   group_image_type = 16
                   group_size = 17
                   current_size_image = int(result.group(group_size))
                   total_size_of_all_files_images += current_size_image
                   count_of_all_files_images += 1

                   if result.group(group_image_type) == 'png' :
                        total_size_png += current_size_image
                   elif result.group(group_image_type) == 'jpeg':
                        total_size_jpeg += current_size_image
                   elif result.group(group_image_type) == 'jpg':
                        total_size_jpg += current_size_image
                   elif result.group(group_image_type) == 'gif':
                        total_size_gif += current_size_image
                   
    except Exception as exception:
        print("Error : ", exception)
    else:
        print("Total size of all images files : ", total_size_of_all_files_images," bytes ",
              total_size_of_all_files_images/2**20," Mb")
        print("Total size of png files: ", total_size_png , " bytes ,", total_size_png/2**20," Mb")
        print("Total size of jpeg files: ", total_size_jpeg , " bytes ,", total_size_jpeg/2**20," Mb")
        print("Total size of jpg files: ", total_size_jpg , " bytes ,", total_size_jpg/2**20," Mb")
        print("Total size of gif files: ", total_size_gif , " bytes ,", total_size_gif/2**20," Mb")
        print("Count all files png ,jpeg ,jpg, gif: ", count_of_all_files_images)
    finally:
        print("Done")

log_file_scanner("apache_logs")