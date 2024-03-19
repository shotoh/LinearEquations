import pandas as pd


def find_minimum(values):
    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    return min_value


def find_maximum(values):
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
    return max_value


def find_mean(values):
    value_sum = 0
    for value in values:
        value_sum += value
    return value_sum / len(values)


def find_mode(values):
    value_dict = dict()
    # maps all values into a dict, key being the medv, value being the count
    for value in values:
        if value in value_dict:
            value_dict[value] += 1
        else:
            value_dict[value] = 1
    result = values[0]
    max_count = value_dict[result]
    for key, value in value_dict.items():
        # finding max count
        if value > max_count:
            result = key
            max_count = value
    return result


def find_variance(values, mean):
    value_sum = 0
    for value in values:
        value_sum += (value - mean) ** 2
    return value_sum / (len(values) - 1)


df = pd.read_csv('BostonHousing.csv')[['medv']]  # read csv and use only the MEDV column
medv = df['medv']
print('Minimum MEDV: ', find_minimum(medv))
print('Maximum MEDV: ', find_maximum(medv))
print('Range MEDV: ', find_maximum(medv) - find_minimum(medv))
print('Mean MEDV: ', find_mean(medv))
print('Mode MEDV: ', find_mode(medv))
print('Variance MEDV: ', find_variance(medv, find_mean(medv)))
print('Standard Deviation MEDV: ', find_variance(medv, find_mean(medv)) ** 0.5)
