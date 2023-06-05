import numpy as np
import os
from PIL import Image

# データセットの保存先ディレクトリ
dataset_dir = 'dataset'

# データの生成
num_images = 100

for i in range(num_images):
    r, g, b = np.random.randint(0, 256, size=3)
    image = np.ones((100, 100, 3), dtype=np.uint8) * np.array([r, g, b], dtype=np.uint8)
    label = (r, g, b)

    # 画像をPIL Imageに変換
    pil_image = Image.fromarray(image)

    # 画像の保存
    image_filename = f'image_{i}.jpg'
    image_path = os.path.join(dataset_dir, image_filename)
    pil_image.save(image_path)

    # ラベルの保存
    label_filename = f'label_{i}.txt'
    label_path = os.path.join(dataset_dir, label_filename)
    with open(label_path, 'w') as file:
        file.write(f'{r} {g} {b}')

    print(f'Saved image {image_filename} and label {label_filename}')

print('Dataset creation completed.')
