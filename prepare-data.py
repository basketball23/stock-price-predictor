import pandas as pd
import numpy as np


df = pd.read_csv("prices/symbols_valid_meta.csv")
symbol_list = df['Symbol'].tolist()

# Parse data for usage

# 60 trading day's worth of inputs,
# 1 trading day for labelling (up or down)
for symbol in symbol_list:
    symbol_df = pd.read_csv(f"prices/symbols_merged/{symbol}.csv")

    day_count = 0

    for index, row in symbol_df.iterrows():
        day_count += 1
        
        if index == symbol_df.index[-1]:
            pass
            # 

        if day_count == 60:
            # add logic to add the next label for the 60 days
            day_count == 0

        else:
            pass