# ndvi_demo.py
# 功能：用一组"模拟多光谱影像"数据计算并可视化 NDVI（归一化植被指数）
# NDVI = (NIR - Red) / (NIR + Red)，植被区接近 +1，水体/裸地接近 0 或负值
import numpy as np
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生成 50x50 的模拟红光、近红外波段（值域 0~1）
np.random.seed(0)
red = np.random.rand(50, 50) * 0.6          # 红光反射率偏低
nir = red + np.random.rand(50, 50) * 0.4    # 近红外略高于红光，模拟有植被

# 计算 NDVI，注意分母可能为 0，用 np.where 防止除零
denom = nir + red
ndvi = np.where(denom > 0, (nir - red) / denom, 0.0)

print("NDVI 均值：", round(float(ndvi.mean()), 3))
print("NDVI 最大值：", round(float(ndvi.max()), 3))

# 可视化：红黄绿配色，植被越茂密越偏绿
plt.imshow(ndvi, cmap="RdYlGn", vmin=-0.2, vmax=1.0)
plt.colorbar(label="NDVI")
plt.title("模拟影像 NDVI 分布")
plt.show()