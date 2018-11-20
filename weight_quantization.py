import math
import numpy as np

def weight_quantize(data):
    sign = 0

    if data == 0:
        integer = decimal = k = new_data = 0
        return integer, decimal, k, new_data

    if data < 0:
        sign = 1
        data = -data

    if data < 1 and data > 0:
        integer = math.floor(math.log(1.0 / data, 10))
        decimal = integer - 7
        k = math.floor(math.log(128.0 / data, 2))
        tmp = round(data * math.pow(2, k))
        new_data = tmp / math.pow(2, k)
    else:
        integer = data // 10 + 1
        decimal = 7 - integer
        k = math.floor(math.log(128.0 / data, 2))
        tmp = round(data * math.pow(2, k))
        new_data = tmp / math.pow(2, k)

    if new_data > 127: new_data = 127
    new_data = new_data if sign == 0 else -new_data

    return integer, decimal, k, new_data

def smallQuantize(data, k):
    tmp = round(data * math.pow(2, k))
    new_data = tmp / math.pow(2, k)
    return new_data

def dataToBit(data_list, next_maximum):
    if type(data_list) != list:
        data_list = [data_list]

    Integer, Decimal, K, New_data = weight_quantize(next_maximum)
    # output = str(Integer) + " " + str(Decimal) + " " + str(K) + "\n"
    # f1.wirte(output)
    for i in range(len(data_list)):
        if data_list[i] >= next_maximum:
            data_list[i] = New_data
            # write to
            # f1.write(str(New_data) + " ")
            continue

        new_data = smallQuantize(data_list[i], K)
        # f1.write(str(New_data) + " ")
        data_list[i] = new_data

    # f1.write("\n")
    return data_list

print(weight_quantize(-0.6095397520212114))
input = np.random.random(5)
input = input.flatten().tolist()
print(input)
print(dataToBit(input, 0.5))
# input1 = np.zeros((2,1))
# # input = input.flatten().tolist()
# print(dataToBit(input, -1))


