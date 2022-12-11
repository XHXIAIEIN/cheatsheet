from zipfile import ZipFile
import os,shutil

root_path = r"D:\XHXIAIEIN\Downloads"
zip_filename = 'file.zip'
zip_filepath = os.path.join(root_path,zip_filename)

# 如果文件夹不存在，先创建
def create_directory(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

with ZipFile(zip_filepath, 'r') as zip:
    # 创建一个临时目录，用来存放解压后的文件
    temp_path = os.path.join(root_path, 'tmp') 
    create_directory(temp_path)

    # 解压压缩包中的文件到临时目录中
    zip.extractall(temp_path, members=[m for m in zip.infolist()])

    # 将压缩包文件名用作文件夹名
    folder_name = os.path.splitext(zip_filename)[0]
    file_path = os.path.join(root_path, folder_name) 
    create_directory(file_path)

    # 移动临时目录中的文件到指定目录中，并在移动时解决文件名中存在的乱码问题
    for file in os.listdir(temp_path):
        temp_file_path = os.path.join(temp_path, file)
        new_file_path = os.path.join(file_path, file.encode('cp437').decode('gbk'))
        shutil.move(temp_file_path, new_file_path)
    
    # 删除临时文件夹
    shutil.rmtree(temp_path)
