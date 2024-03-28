import pandas as pd


# util method to round down
def floor(number):
    return int(number)


# util method to round up
def ceil(number):
    return floor(number) + 1


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
    # finding max count and saving the key
    for key, value in value_dict.items():
        if value > max_count:
            result = key
            max_count = value
    return result


def find_variance(values, mean):
    value_sum = 0
    for value in values:
        value_sum += (value - mean) ** 2
    return value_sum / (len(values) - 1)  # finds the sample variance


# greater than method
def find_percentile_method_1(sorted_values, percentile):
    rank = ceil(len(sorted_values) * percentile)
    return sorted_values[rank]


# greater than or equal method
def find_percentile_method_2(sorted_values, percentile):
    rank = ceil(len(sorted_values) * percentile) - 1
    return sorted_values[rank]


# interpolation approach
def find_percentile_method_3(sorted_values, percentile):
    rank = (len(sorted_values) + 1) * percentile
    # if integer than use as rank
    if isinstance(rank, int):
        return sorted_values[rank]
    floor_val = sorted_values[floor(rank)]
    ceil_val = sorted_values[ceil(rank)]
    frac = rank - int(rank)
    # finds the difference between ceil and floor and multiplies it by fractional portion
    return (ceil_val - floor_val) * frac + floor_val


df = pd.read_csv('BostonHousing.csv')[['medv']]  # read csv and use only the MEDV column
medv = df['medv']
print('Minimum MEDV: ', find_minimum(medv))
print('Maximum MEDV: ', find_maximum(medv))
print('Range MEDV: ', find_maximum(medv) - find_minimum(medv))
print('Mean MEDV: ', find_mean(medv))
print('Mode MEDV: ', find_mode(medv))
print('Variance MEDV: ', find_variance(medv, find_mean(medv)))
print('Standard Deviation MEDV: ', find_variance(medv, find_mean(medv)) ** 0.5)

sorted_medv = list(medv)
sorted_medv.sort()  # sorts the list to use the percentile methods
print('40% percentile:')
print('1. (greater than) ', find_percentile_method_1(sorted_medv, 0.4))
print('2. (greater than or equal) ', find_percentile_method_2(sorted_medv, 0.4))
print('3. (interpolation) ', find_percentile_method_3(sorted_medv, 0.4))
print('80% percentile:')
print('1. (greater than) ', find_percentile_method_1(sorted_medv, 0.8))
print('2. (greater than or equal) ', find_percentile_method_2(sorted_medv, 0.8))
print('3. (interpolation) ', find_percentile_method_3(sorted_medv, 0.8))
