items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 250
  }
]

prices=list(map(lambda x:x['price'], items ))
print(prices)

def add_taxes(x):
    x['taxes'] = x['price'] * 1.19
    return x

new_items= list(map(add_taxes,items))
print(new_items)