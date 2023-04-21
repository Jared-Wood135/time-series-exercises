# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. wrangle_store
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
from sklearn.model_selection import train_test_split
import prepare

# =======================================================================================================
# Imports END
# Imports TO wrangle_store
# wrangle_store START
# =======================================================================================================

def wrangle_store():
    '''
    Acquires the prepared 'store' dataset then returns a split version for exploration...

    INPUT:
    NONE

    OUTPUT:
    store.csv = ONLY IF IT IS NONEXISTANT
    train = train subset of prepared dataframe
    validate = validate subset of prepared dataframe
    test = test subset of prepared dataframe
    '''
    store = prepare.prepare_store()
    train_val, test = train_test_split(store, train_size=0.8, random_state=1349)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=1349)
    return train, validate, test

# =======================================================================================================
# wrangle_store END
# wrangle_store TO wrangle_germany
# wrangle_germany START
# =======================================================================================================

def wrangle_germany():
    '''
    Acquires the prepared 'germany' dataset then returns a split version for exploration...

    INPUT:
    NONE

    OUTPUT:
    germany.csv = ONLY IF IT IS NONEXISTANT
    train = train subset of prepared dataframe
    validate = validate subset of prepared dataframe
    test = test subset of prepared dataframe
    '''
    germany = prepare.prepare_germany()
    train_val, test = train_test_split(germany, train_size=0.8, random_state=1349)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=1349)
    return train, validate, test

# =======================================================================================================
# wrangle_germany END
# =======================================================================================================