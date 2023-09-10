# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-03-28 19:32 
# ide： PyCharm
import numpy as np

arr = np.array([1, 2, 3, 4, 5])  # 示例数组，你可以替换成自己的数组
pre_mu = 1

# 创建权重数组
weights = np.full(len(arr), 0.95)

# 计算累积乘积
cumulative_weights = np.multiply.accumulate(weights)

# 计算新的数组
new_arr = np.zeros(len(arr))
new_arr[0] = pre_mu
new_arr[1:] = (1 - cumulative_weights[:-1]) * arr[1:] + cumulative_weights[:-1] * pre_mu

# 打印每一步的 pre_mu 值
print(new_arr)

pre_mu=1
for i in range(len(arr)):
    pre_mu=pre_mu*0.95+0.05*arr[i]
    print(pre_mu)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])  # 示例数组，你可以替换成自己的数组
pre_mu = 1

# 计算累积和
cumulative_sum = np.zeros(len(arr) + 1)
cumulative_sum[1:] = np.cumsum(np.log(1 + 0.05 * arr))

# 计算每一步的 pre_mu 值
pre_mu_values = pre_mu * np.exp(cumulative_sum * 0.95)

print(pre_mu_values[1:])
