import pandas as pd
import numpy as np


df = pd.read_csv("prices/symbols_valid_meta.csv")
symbol_list = df['Symbol'].tolist()

# Parse data for usage

# 60 trading day's worth of inputs,
# 1 trading day for labelling (up or down)

X = []
Y = []

for symbol in symbol_list:
    try:
        symbol_df = pd.read_csv(f"prices/symbols_merged/{symbol}.csv")
    except FileNotFoundError:
        pass
    

    day_count = 0

    current_X = []

    for index, row in symbol_df.iterrows():

        change_val = row['Close'] - row['Open']
        change_direction = 0

        if change_val > 0:
            change_direction = 1

        
        if day_count == 60:

            X.append(current_X)
            Y.append(change_direction)

            current_X = []
            day_count == 0

        else:
            current_X.append(change_direction)

        day_count += 1


print(len(X))
