import os  
import shutil  
import glob  
import re  
ClassMap={1: 'airplane', 2: 'ship', 3: 'storage tank', 4: 'baseball diamond', 5: 'tennis court', 6: 'basketball court', 7: 'ground track field', 8: 'harbor', 9: 'bridge', 10: 'vehicle'}
def extract_numbers_from_line(line):  
    numbers = re.findall(r'\d+', line)  
    return numbers  

def modify_and_save_text_files(source_directory, target_directory):  
    # 如果目标文件夹不存在，则创建  
    if not os.path.exists(target_directory):  
        os.makedirs(target_directory)  
  
    # 遍历指定文件夹下的所有txt文件  
    for filename in glob.glob(os.path.join(source_directory, '*.txt')):  
        # 获取文件名和扩展名  
        base_filename = os.path.basename(filename)  
        # 在目标文件夹下创建新的文件并写入修改后的内容  
        new_filename = os.path.join(target_directory, base_filename)  
        with open(filename, 'r') as file:  
            lines = file.readlines()  
            # 修改文件内容  

            for line in lines:
                if len(line)<5:
                    continue
                # 定义要提取的数字字符串  
                numbers = extract_numbers_from_line(line) 
                if len(numbers)<5:
                    continue
                # xmin ymin xmax ymax lable 
                xmin=numbers[0]
                ymin=numbers[1]
                xmax=numbers[2]
                ymax=numbers[3]
                label=numbers[4]
                # 变为OBB格式
                #x1 y1 x2 y2 x3 y3 x4 y4 label difficult
                x1 = xmin
                y1 = ymin
                x2 = xmax
                y2 = ymin
                x3 = xmax
                y3 = ymax
                x4 = xmin
                y4 = ymax
                difficult = '0'
                # 合成一个字符串，分隔符为空格
                line = ' '.join([x1, y1, x2, y2, x3, y3, x4, y4, label, difficult])
                with open(new_filename, 'w') as new_file:  
                    new_file.writelines(line)  
            print(f"Saved modified file to {target_directory} as {base_filename}")  
  
# 调用函数，将指定文件夹下的所有txt文件中的"old_string"替换为"new_string"，并保存到另一个文件夹下 

pth=os.path.abspath(os.path.dirname(__file__))          
source_dir = pth+"\ground truth"  # 源文件夹路径  
target_dir = pth+"\data\lables"  # 目标文件夹路径  
modify_and_save_text_files(source_dir, target_dir)