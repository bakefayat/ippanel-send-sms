import numpy as np
import pandas as pd


def add_to_set():
    pan = pd.read_excel('customers.xlsx')
    df = pd.DataFrame(pan, )
    df = df.replace({np.nan: None})
    name = df['name'].tolist()
    price = df['price'].tolist()
    number = df['number'].tolist()
    names = []
    prices = []
    numbers = []
    for i in range(0, len(name)):
        if number[i] and price[i] and name[i]:
            if type(number[i]) != int:
                number[i] = number[i].strip()
            name[i] = name[i].strip()
            if number[i] and price[i] and name[i]:
                names.append(name[i])
                prices.append(price[i])
                numbers.append(number[i])

        # dict[name[i]] = price[i]
    info = zip(names, prices, numbers)
    return list(info)
