import math
import pandas


def find_sd(data, length):
    # find mean
    sum_data = sum(data)
    mean = sum_data / length

    xi_xbars = []
    for i in data:
        xi_xbar_data = i - mean
        xi_xbars_data = pow(xi_xbar_data, 2)
        xi_xbars.append(xi_xbars_data)

    sum_xi_xbars = 0
    for j in xi_xbars:
        sum_xi_xbars = sum_xi_xbars + j
    s_d = math.sqrt(sum_xi_xbars / (length - 1))
    return round(s_d, 4)


data_item = pandas.read_csv('student - Sheet1.csv')

data_integers = data_item.select_dtypes(include=['float64', 'int64'])
length_item = len(data_integers)
for i in data_integers:
    sd = find_sd(data_integers[i], length_item)
    print(f"standard deviation of {i} = {sd}")


