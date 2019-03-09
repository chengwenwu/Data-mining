# this file is exercise 3 of Data Mining homework1
import math
import numpy as np
import random as rd
import matplotlib.pyplot as mpl

points = (10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500, 10000)
loop_times = 100
a = -1
b = 1
c = 2
d = 4
matrix = [[0 for col in range(len(points))] for row in range(2)]  # 建立一个8列2行的矩阵，用来存放实验结果数据

temp_result = [0 for i in range(loop_times)]
for n in range(len(points)):
    for m in range(loop_times):
        sum_t = 0
        for k in range(points[n]):
            x = c + rd.random()*(d - c)
            y = a + rd.random()*(b - a)
            up = pow(y, 2) * math.exp(- pow(y, 2)) + pow(x, 4) * math.exp(- pow(x, 2))
            down = x * math.exp(- pow(x, 2))
            sum_t += (up / down)
        temp_result[m] = sum_t * (b - a) * (d - c) / points[n]
    matrix[0][n] = np.mean(temp_result)  # 均值
    matrix[1][n] = np.var(temp_result)  # 方差
    print("采样 ", points[n], " 个点:  均值： ", matrix[0][n], "  方差： ", matrix[1][n])

mpl.figure(1)
mpl.plot(points, matrix[0], label="means")
mpl.xlabel("number of sample points")
mpl.ylabel("means")
mpl.legend()
mpl.show()
mpl.figure(2)
mpl.plot(points, matrix[1], label="variances")
mpl.xlabel("number of sample points")
mpl.ylabel("variances")
mpl.legend()
mpl.show()
