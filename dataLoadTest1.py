import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ast

# CSVファイルからデータを読み込む
df = pd.read_csv('dataset2.csv')

# 画像データとラベルを取得
images = df['画像']
labels = df['ラベル']

# 画像を表示
for i in range(len(images)):
    image = np.array(ast.literal_eval(images[i]))
    image = image.reshape((100, 100, 3))
    label = ast.literal_eval(labels[i])
    
    plt.imshow(image)
    plt.title(f'Label: {label}')
    plt.axis('off')
    plt.show()
