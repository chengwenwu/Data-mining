# this file is homework of Data Mining exercise 1
import random as rd
import matplotlib.pyplot as mpl

matrix = [[0 for col in range(8)] for row in range(2)]  # 建立一个8列2行的矩阵，用来存放实验结果数据
data_input = (20, 50, 100, 200, 300, 500, 1000, 5000)   # 使用元组来存放数据，防止中途被修改
loop_times = 10  # 每个总点数的循环次数
temp_matrix = [0]*loop_times  # 临时数组用来存放每次循环的结果，方便最后计算均值和方差。

for n in range(len(data_input)):  # 不同点数

    sum_t = 0
    for m in range(loop_times):  # 多次循环
        count = 0
        for k in range(data_input[n]):
            x = rd.random()  # 横坐标
            y = rd.random()  # 纵坐标
            dis = pow(pow(x, 2) + pow(y, 2), 0.5)  # 距离
            if dis <= 1:
                count += 1
        temp_matrix[m] = count / data_input[n] * 4  # 保存中间结果
        sum_t += temp_matrix[m]  # 为计算均值做准备

    matrix[0][n] = sum_t / loop_times  # 均值

    sum_t = 0
    for j in range(loop_times):
        sum_t += pow((temp_matrix[j] - matrix[0][n]), 2)

    matrix[1][n] = pow(sum_t / loop_times, 0.5)  # 方差

mpl.figure(1)
mpl.plot(data_input, matrix[0], label="means")
mpl.plot(data_input, matrix[1], label="variances")
mpl.plot(data_input, [3.14159265 for i in range(len(data_input))], label="true value")
mpl.legend()
mpl.show()

for list_t in matrix:
    for ele in list_t:
        print(ele, end="  ")
    print()





