# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. acquire_swapi
4. acquire_germany
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is specifically created for the question set from 'acquire.ipynb'...

This file generally acquires and merges data for Star Wars and Open Power Systems Data for Germany...
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
import os
import env
import requests

# =======================================================================================================
# Imports END
# Imports TO acquire
# acquire START
# =======================================================================================================

def acquire_swapi():
    '''
    Obtains the vanilla version of the people, starships, and planets api then joins all 3 tables.

    INPUT:
    NONE

    OUTPUT:
    swapi = pandas dataframe of all 3 tables
    '''
    people = requests.get('https://swapi.dev/api/people/')
    planets = requests.get('https://swapi.dev/api/planets/')
    starships = requests.get('https://swapi.dev/api/starships/')
    data_people = people.json()
    people_df = pd.DataFrame(data_people['results'])
    people_df.to_csv('people.csv')
    data_planets = planets.json()
    planets_df = pd.DataFrame(data_planets['results'])
    planets_df.to_csv('planets.csv')
    data_starships = starships.json()
    starships_df = pd.DataFrame(data_starships['results'])
    starships_df.to_csv('starships.csv')
    swapi = pd.concat([people_df, starships_df, planets_df], axis=1)
    return swapi

# =======================================================================================================
# acquire_swapi END
# acquire_swapi TO acquire_germany
# acquire_germany START
# =======================================================================================================

def acquire_germany():
    '''
    Obtains the vanilla version of the germany data and creates a .csv

    INPUT:
    NONE

    OUTPUT:
    germany = pandas dataframe of germany info
    '''
    germany = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    germany.to_csv('germany.csv')
    return germany

# =======================================================================================================
# acquire_germany END
# =======================================================================================================