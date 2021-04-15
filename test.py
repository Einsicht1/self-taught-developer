def min_coin_count(value, coin_list):
    res = 0
    value1 = 0
    for coin in default_coin_list:
        coin_num = value // coin
        res += coin_num
        value -= coin_num * coin
        if value == 0:
            return res

default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))