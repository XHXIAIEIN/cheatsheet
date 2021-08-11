from PIL import Image
import matplotlib.pyplot as plt
import os

# 原始图像路径
IMAGE_INPUT_PATH = 'D:/Desktop/新建文件夹'

# 裁剪完成，图像输出路径
IMAGE_OUTPUT_PATH = 'D:/Desktop/新建文件夹/output'

# 裁剪区域：上、左、下、右
BOX_UP,BOX_LEFT,BOX_DOWN,BOX_RIGHT = 470, 0, 828, 828

if not os.path.exists(IMAGE_OUTPUT_PATH):
    os.makedirs(IMAGE_OUTPUT_PATH)

# 开始遍历文件夹内的所有文件
for each_image in os.listdir(IMAGE_INPUT_PATH):
    
    # 补全文件的完整路径
    image_input_fullname = IMAGE_INPUT_PATH + '/' + each_image
    
    # 判断文件类型
    image_type = os.path.splitext(each_image)[-1].lower()
    
    # 过滤其他类型的文件
    if image_type not in ['.jpg', '.jpeg', '.png']: 
        continue
    
    # 打开图像
    img = Image.open(image_input_fullname)
    plt.figure("image_input_fullname")
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.axis('off')

    # 裁剪
    roi_area = img.crop(BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN)
    plt.subplot(1, 2, 2)
    plt.imshow(roi_area)
    plt.axis('off')
    
    # 裁剪完成的文件路径
    image_output_fullname = IMAGE_OUTPUT_PATH + "/" + each_image

    # 存储裁剪得到的图像
    roi_area.save(image_output_fullname)
