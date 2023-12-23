import os  
from PIL import Image  
  
def convert_images_to_png(directory):  
    # 遍历目录下的所有文件  
    for root, dirs, files in os.walk(directory):  
        for file in files:  
            # 检查文件是否为图片  
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):  
                # 构建完整的文件路径  
                file_path = os.path.join(root, file)  
                # 打开图片文件  
                with Image.open(file_path) as img:  
                    # 保存为PNG格式  
                    img.save(file_path, 'PNG')  
                    print(f"Converted {file_path} to PNG")  
def rename_images_to_png(directory):  
    # 遍历目录下的所有文件  
    for root, dirs, files in os.walk(directory):  
        for file in files:  
            # 检查文件是否为图片  
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):  
                # 构建完整的文件路径  
                file_path = os.path.join(root, file)  
                # 获取不带扩展名的文件名  
                base_name = os.path.splitext(file)[0]  
                # 构建新的文件名，将扩展名更改为.png  
                new_file_name = base_name + '.png'  
                # 构建新的文件路径  
                new_file_path = os.path.join(root, new_file_name)  
                # 重命名文件  
                os.rename(file_path, new_file_path)  
                print(f"Renamed {file_path} to {new_file_path}")    
# 使用示例：将指定目录下的所有图片转换为PNG格式  
directory = r'D:\BaiduNetdiskDownload\vhr-10\NWPU VHR-10 dataset\vhr10\NWPU VHR-10 dataset\data\images' 
# 替换为您的目录路径  
convert_images_to_png(directory)
rename_images_to_png(directory)