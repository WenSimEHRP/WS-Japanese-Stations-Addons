from PIL import Image
import os

def process_spritesheets(directory):
    # 获取目录中的所有文件
    files = os.listdir(directory)

    # 遍历每个文件
    for file in files:
        # 只处理图片文件
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.bmp'):
            # 打开图片
            img = Image.open(os.path.join(directory, file))

            # 获取图片的宽度和高度
            width, height = img.size
            if width < 65:
                print(f'Image {file} is too small to process')
                continue

            # 计算sprites的数量
            num_sprites = width // 65  # 每个sprites 64px，间隔1px

            # 创建一个新的spritesheet，宽度为每个sprite的宽度（包括边框）加上1px的白色像素
            new_img = Image.new('RGB', (num_sprites * 74 - 1, 72), color='white')

            # 遍历每个sprites
            for i in range(num_sprites):
                # 提取sprites
                sprite = img.crop((i * 65, 0, i * 65 + 64, 64))

                # 创建一个新的图像，然后将sprite粘贴到中间
                sprite_with_border = Image.new('RGB', (72, 72), color='blue')
                sprite_with_border.paste(sprite, (4, 4))

                # 将带有边框的sprite放到新的spritesheet上，位置向右移动1px
                new_img.paste(sprite_with_border, (i * 74, 0))

            # 保存新的spritesheet
            new_img.save('processed_' + file)

process_spritesheets('src\stations\generated_stations\gfx')