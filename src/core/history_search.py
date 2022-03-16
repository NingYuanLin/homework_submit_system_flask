# Time:2022/3/16 8:00 PM
# Author:NYL
# Describe:
import datetime
import os

from src.helper import check_format_helper
from src.config import file_config


def get_filenames_in_dir_no_recursive(dir_path):
    filenames = []
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            filenames.append(filename)
    return filenames


def get_ori_filename_and_timestamp(filename: str):
    """
    获取源文件名
    :param filename: 学号_姓名_时间戳---源文件名.pdf
    :return:源文件名.pdf
    """
    filename_prefix, filename_postfix = os.path.splitext(filename)
    filename_prefix_split = filename_prefix.split('---')
    ori_filename_prefix = filename_prefix_split[1]
    timestamp = filename_prefix_split[0].split('_')[2]
    ori_filename = ori_filename_prefix + filename_postfix
    return ori_filename, timestamp


def timestamp_to_datetime_str(timestamp: [int, float]):
    datetime_str = datetime.datetime.fromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    return datetime_str


def history_search(username, student_id):
    if not check_format_helper.username_and_student_id_is_right(username, student_id):
        return {
            'status': 400,
            'msg': '请检查用户名和学号是否输入正确'
        }

    file_dir_path = file_config.get_file_dir_path()

    file_dir_path = os.path.join(file_dir_path, student_id)

    filenames = get_filenames_in_dir_no_recursive(file_dir_path)

    result = []

    for filename in filenames:
        ori_filename, timestamp = get_ori_filename_and_timestamp(filename)
        # 对时间戳=>日期
        datetime_str = timestamp_to_datetime_str(float(timestamp))
        result.append({
            'date': datetime_str,
            'filename': ori_filename
        })

    return {
        'status': 200,
        'result': result
    }
