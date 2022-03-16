# Time:2022/3/16 3:43 PM
# Author:NYL
# Describe:
import datetime
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
from src.config import file_config
from src.helper import check_format_helper

file_dir_path = file_config.get_file_dir_path()


def upload_file(username, student_id, filename, file_bytes):
    if not check_format_helper.username_and_student_id_is_right(username, student_id):
        return {
            'status': 400,
            'msg': '请检查用户名和学号是否输入正确'
        }

    now_timestamp = str(int(datetime.datetime.now().timestamp()))
    filename = f'{student_id}_{username}_{now_timestamp}---{filename}'
    file_path = os.path.join(file_dir_path, student_id, filename)  # 根目录/student_id/文件名

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, 'wb') as writer:
        writer.write(file_bytes)

    return {
        'status': 200,
        'msg': '文件上传成功'
    }
