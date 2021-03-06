def shopping_in_store(goods_list) -> tuple:
    """ Returns price of a single purchase and stock balance """
    result = 0
    for product in goods_list:
        if stock[product] > 0:
            result += prices[product]
            stock[product] -= 1
        if stock[product] == 0:
            print('Note! Some of your needed products are out of stock. Please come later or pre-order them.')
    return f'Price is: {result}', '\n'.join(f'{k}: {v}' for k, v in stock.items())


shop_list = ['iphone', 'macbook', 'airpods']
prices = {'iphone': 1500,
          'macbook': 2000,
          'airpods': 500,
          'ipad': 1300,
          'appleTV': 800}
stock = {'iphone': 15,
         'macbook': 0,
         'airpods': 3,
         'ipad': 5,
         'appleTV': 25}
print(*(shopping_in_store(shop_list)), sep='\nStock balance: \n')
