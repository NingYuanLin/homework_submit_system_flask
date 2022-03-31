# Time:2022/3/16 8:00 PM
# Author:NYL
# Describe:
import csv
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)

student_list_file_path = os.path.join(root_path, 'statics/student_list.csv')

if not os.path.exists(student_list_file_path):
    raise FileExistsError("""
        请检查statics/student_lit.csv文件是否存在，
        在开源版本中，为了隐私，此文件不会被上传到git
        文件的格式如下：
        序号,学号,姓名,院系,专业,备注
        1,xxxxxxx,xxxxxx,信息与电气工程学院,电气工程,
    """)

with open(student_list_file_path, 'r', encoding='utf8') as reader:
    csv_reader = csv.DictReader(reader)
    student_id_to_info_dict = {}
    for line in csv_reader:
        student_id = line.pop('学号').lower()
        student_id_to_info_dict[student_id] = line


def username_and_student_id_is_right(username, student_id:str):
    """
    检查用户名和学号是否合法，合法返回True
    :param username:
    :param student_id:
    :return:
    """
    if student_id not in student_id_to_info_dict:
        return False
    else:
        real_name = student_id_to_info_dict[student_id]['姓名']
        if username == real_name:
            return True
        else:
            return False
