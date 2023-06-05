import numpy as np
import pandas as pd

# データの生成
data = {
    '年齢': np.random.randint(18, 65, size=100),
    '性別': np.random.choice(['男性', '女性'], size=100),
    '収入': np.random.randint(20000, 100000, size=100)
}

# データフレームの作成
df = pd.DataFrame(data)

# データセットをCSVファイルとして保存
df.to_csv('dataset1.csv', index=False)