# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. prepare_store
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is specifically created for exercises within this repository...
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import numpy as np
import pandas as pd
import acquire

# =======================================================================================================
# Imports END
# Imports TO prepare_store
# prepare_store START
# =======================================================================================================

def prepare_store():
    '''
    Acquires the vanilla 'store' dataset then returns a prepared version for exploration...

    INPUT:
    NONE

    OUTPUT:
    store.csv = ONLY IF IT IS NONEXISTANT
    newstore = pandas dataframe
    '''
    store = acquire.acquire_store()
    store.sale_date = pd.to_datetime(store.sale_date)
    store = store.set_index(store.sale_date)
    store = store.drop(columns='sale_date')
    store['month'] = store.index.month
    store['dayofweek'] = store.index.dayofweek
    store['sales_total'] = store.sale_amount * store.item_price
    newstore = store
    return newstore

# =======================================================================================================
# prepare_store END
# prepare_store TO prepare_germany
# prepare_germany START
# =======================================================================================================

def prepare_germany():
    '''
    Acquires the vanilla 'germany' dataset then returns a prepared version for exploration...

    INPUT:
    NONE

    OUTPUT:
    germany.csv = ONLY IF IT IS NONEXISTANT
    newgermany = pandas dataframe
    '''
    germany = acquire.acquire_germany()
    germany.Date = pd.to_datetime(germany.Date)
    germany = germany.set_index(germany.Date)
    germany = germany.drop(columns='Date')
    germany['year'] = germany.index.year
    germany['month'] = germany.index.month
    germany.Wind = germany.Wind.fillna(round(germany.Wind.mean(), 3))
    germany.Solar = germany.Solar.fillna(round(germany.Solar.mean(), 3))
    germany['Wind+Solar'] = germany['Wind+Solar'].fillna(round(germany['Wind+Solar'].mean(), 3))
    newgermany = germany
    return newgermany

# =======================================================================================================
# prepare_germany END
# =======================================================================================================