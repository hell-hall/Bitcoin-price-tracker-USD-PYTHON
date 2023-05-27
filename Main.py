import requests
import json
import time
import pandas as pd
import matplotlib.pyplot as plt

def make_request():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()
        return data['bitcoin']['usd']
    except requests.exceptions.RequestException as error:
        print('Error:', error)


def start():
    price_array = []
    index_array = []
    i = 1
    interval = int(input('How much time in between samples (secs): '))
    samples = int(input('How many samples: '))

    # Make sure interval and samples are valid
    if interval <= 0 or samples <= 0:
        print('Please make sure that your interval and sample value is greater than 0.')
        start()

    while samples > 0:
        bitcoin_value = make_request()
        price_array.append(bitcoin_value)
        index_array.append('Sample ' + str(i))
        print('Price:', bitcoin_value)
        time.sleep(interval)
        i += 1
        samples -= 1

    print('Price Array:', price_array)
    print('Sample Array:', index_array)

    # Create a DataFrame
    df = pd.DataFrame({'Sample': index_array, 'Price (USD)': price_array})

    # Create a bar chart using pandas and matplotlib
    df.plot(x='Sample', y='Price (USD)', kind='bar')
    plt.xlabel('Sample')
    plt.ylabel('Price (USD)')
    plt.title('Bitcoin Price Samples')
    plt.show()

start()
