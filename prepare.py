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
# =======================================================================================================