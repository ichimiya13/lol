import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# データの生成
num_images = 100

data = {
    '画像': [],
    'ラベル': []
}

for _ in range(num_images):
    r, g, b = np.random.randint(0, 256, size=3)
    image = np.ones((100, 100, 3)) * np.array([r, g, b]) / 255.0
    label = (r, g, b)
    
    data['画像'].append(np.array2string(image, separator=', '))
    data['ラベル'].append(label)

# データフレームの作成
df = pd.DataFrame(data)

# データセットをCSVファイルとして保存
df.to_csv('dataset2.csv', index=False)
