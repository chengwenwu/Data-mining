# this file is exercise 2 of Data Mining homework1
import numpy as np
import random as rd
import matplotlib.pyplot as mpl

points = (5, 10, 20, 30, 40, 50, 60, 70, 80, 100, 1000)
loop_times = 100
a = 0
b = 1
matrix = [[0 for col in range(len(points))] for row in range(2)]  # 建立一个8列2行的矩阵，用来存放实验结果数据

temp_result = [0 for col in range(loop_times)]
for m in range(len(points)):
    sum_t = 0
    for k in range(loop_times):
        sum_t = 0
        for n in range(points[m]):
            sum_t += pow(rd.random(), 3)
        temp_result[k] = sum_t * (b - a) / points[m]
    matrix[0][m] = np.mean(temp_result)  # 均值
    matrix[1][m] = np.var(temp_result)  # 方差
    print("采样 ", points[m], " 个点:  均值： ", matrix[0][m], "  方差： ", matrix[1][m])

mpl.figure(1)
mpl.plot(points, matrix[0], label="means")
mpl.plot(points, matrix[1], label="variances")
mpl.plot(points, [0.25 for i in range(len(points))], label="true value")
mpl.legend()
mpl.show()