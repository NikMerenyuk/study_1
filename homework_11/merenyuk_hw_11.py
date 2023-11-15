# TASK 1
#
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


def main():
    summa = 0
    while True:
        choice = (int(input('Сколько песен выбрать?(1-9) -> ')))
        for i_song in range(choice):
            name_song = (input(f'Название {i_song + 1} песни: '))
            get_song = violator_songs.get(name_song)
            if get_song:
                summa += violator_songs[name_song]
            else:
                print('Такой песни нет в списке!')
                break
        return f'Общее время звучания: {round(summa, 2)}'


print(main())


# TASK 2
#
# data = {
# "address": "0x544444444444",
# "ETH": {
# "balance": 444,
# "totalIn": 444,
# "totalOut": 4
# },
# "count_txs": 2,
# "tokens": [
# {
# "fst_token_info": {
# "address": "0x44444",
# "name": "fdf",
# "decimals": 0,
# "symbol": "dsfdsf",
# "total_supply": "3228562189",
# "owner": "0x44444",
# "last_updated": 1519022607901,
# "issuances_count": 0,
# "holders_count": 137528,
# "price": False
# },
# "balance": 5000,
# "totalIn": 0,
# "total_out": 0
# },
# {
# "sec_token_info": {
# "address": "0x44444",
# "name": "ggg",
# "decimals": "2",
# "symbol": "fff",
# "total_supply": "250000000000",
# "owner": "0x44444",
# "last_updated": 1520452201,
# "issuances_count": 0,
# "holders_count": 20707,
# "price": False
# },
# "balance": 500,
# "totalIn": 0,
# "total_out": 0
# }
# ]
# }

# print(f'Список ключей: {list(data.keys())}\n'
#       f'Список значений: {list(data.values())}')

# a = (data['ETH'].setdefault('total_diff', 100))
# print(data['ETH'])

# rename = data['tokens'][0]['fst_token_info']['name'] = 'doge'
# print(data['tokens'][0]['fst_token_info']['name'])

# change = data['tokens'][0].pop('total_out')
# data['ETH']['totalOut'] = change
# print(data['ETH']['totalOut'])

# total = data['tokens'][1]['sec_token_info'].pop('price')
# data['tokens'][1]['sec_token_info'].setdefault('total_price', total)
# print(data['tokens'][1]['sec_token_info'])
