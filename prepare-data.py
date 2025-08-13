import pandas as pd
import numpy as np
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
list_file_path = os.path.join(base_dir, "prices", "symbols_valid_meta.csv")

df = pd.read_csv(list_file_path)
symbol_list = df['Symbol'].tolist()

# Parse data for usage

# 60 trading day's worth of inputs,
# 1 trading day for labelling (up or down)

X = []
Y = []

for symbol in symbol_list:
    try:
        symbol_file_path = os.path.join(base_dir, "prices", "symbols_merged", f"{symbol}.csv")
        symbol_df = pd.read_csv(symbol_file_path)
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
print(len(Y))

X = np.array(X)
Y = np.array(Y)

np.savez("stock_data.npz", X_data=X, Y_data=Y)