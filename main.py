from pdf2image import convert_from_path, convert_from_bytes

import tempfile
import os

# PDF文件夹目录
dirPath = "C:\\Users\\SHAT\\PhpstormProjects\\tarot\\gb"

# 截取首张图片保存路径
picOutputPath = 'C:\\Users\\SHAT\\PhpstormProjects\\tarot\\img'

for root, dirs, files in os.walk(dirPath):

    for file in files:

        # 获取文件名
        filename = os.path.basename(os.path.join(root, file)).split('.')
        if filename[1] == 'pdf':
            with tempfile.TemporaryDirectory() as path:
                images_from_path = convert_from_path(os.path.join(root, file), output_folder=picOutputPath, first_page=0, dpi=50,thread_count=10,
                                                     last_page=1, fmt="png", output_file=filename[0], single_file=True)
