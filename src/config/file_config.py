# Time:2022/3/16 3:45 PM
# Author:NYL
# Describe:
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root_path)
from src.config import environment_type

if environment_type.get_env_type() == environment_type.EnvType.DEV:
    FILE_DIR_PATH = os.path.join(root_path, 'statics')
else:
    FILE_DIR_PATH = '/home/ubuntu/homework_dir'


def get_file_dir_path():
    return FILE_DIR_PATH
