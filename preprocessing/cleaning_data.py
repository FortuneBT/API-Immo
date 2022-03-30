#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor


raw_data = pd.read_csv('./data/data.csv')


# # Preprocessing
def manage_raw_data(raw_data:pd.DataFrame) -> pd.DataFrame:
    # Remove nul price and change data type as float
    raw_data = raw_data[pd.to_numeric(raw_data['Price'], errors='coerce').notnull()]
    raw_data = raw_data.astype({"Price": float}, errors='raise')
    # Remove duplicate ID's
    raw_data = raw_data.drop_duplicates(['Immoweb ID'], keep='last')
    # ### Determining the variables of interest
    # As Fire places and Tenement building has so many missing values, we will drop these columns. We can apply the same for the Garden surface but instead of drop this column we will replace it with new feature (Region)
    # We also do not use Garden & Terrace surface. These columns will be drop after handeling missing values.
    df = raw_data.drop(columns =['Tenement building', 'How many fireplaces?', 'Garden orientation'])
    # ### Dealing with missing values
    building_condition_map = {'As new': 6, 'Just renovated': 5, 'Good': 4, 'To be done up': 3, 'To renovate':2, 'To restore':1}
    df = df.applymap(lambda s: building_condition_map.get(s) if s in building_condition_map else s)
    df['Building condition'] = df['Building condition'].fillna(2)
    return df

def change_kitchen(df:pd.DataFrame) -> pd.DataFrame:
    # #### Kitchen Type
    Kit_type_dict = {"USA uninstalled" : 0, 
                    "Not installed" : 0, 
                    "Installed": 1, 
                    "USA installed": 1,
                    "Semi equipped": 1,
                    "USA semi equipped": 1,
                    "Hyper equipped": 2,
                    "USA hyper equipped": 2
                    }

    df = df.replace(Kit_type_dict)
    df["Kitchen type"] = df["Kitchen type"].fillna(0)
    return df

def change_furnished(df:pd.DataFrame) -> pd.DataFrame:   
    # Fill missing values
    df['Furnished'] = df['Furnished'].fillna("No")
    df['Furnished'] = df['Furnished'].apply(lambda v: 0 if v == "No" else 1)
    return df

def change_bedrooms(df:pd.DataFrame) -> pd.DataFrame:
    # #### Bedrooms
    # Fill missing values with 2 bedrooms
    df['Bedrooms'] = df['Bedrooms'].fillna(2).astype(int)
    return df

def change_swimming_pool(df:pd.DataFrame) -> pd.DataFrame:
    # #### Swimming Pool
    # Fill missing values with value 0
    df['Swimming pool'].fillna(0, inplace = True)
    df['Swimming pool'] = df['Swimming pool'].apply(lambda v: 0 if v == "No" else 1)
    return df


def change_surface_plot(df:pd.DataFrame) -> pd.DataFrame:
    # #### Surface of the plot
    # Fill empty values with 0
    df['Surface of the plot'].fillna(0, inplace = True)
    return df

def change_area(df:pd.DataFrame) -> pd.DataFrame:  
    # #### Living area
    a = sorted(df['property sub-type'].unique())
    b = df.groupby('property sub-type')['Living area'].median()
    dict_sub_type_area = {}
    for name, num in zip(a, b):
        dict_sub_type_area[name] = float(num)
    """def fill_living_area(col):  
        
        if col['Living area'] > 0:
            return col['Living area']
        else:
            for k, v in dict_sub_type_area.items():
                if col['property sub-type'] == k:
                    col['Living area'].str.replace('nan',v)

    df['Living area'] = df.apply(lambda col: fill_living_area(col), axis=1)"""

    # #### Fill missing values in Living area row
    df_la_no_null = df.copy()

    def fill_living_area(col):  
        if col['Living area'] > 0:
            return col['Living area']
        else: 
            if col['property sub-type'] == 'APARTMENT':
                return 101.0
            else:
                return 254.0

    df_la_no_null['Living area'] = df_la_no_null.apply(lambda col: fill_living_area(col), axis=1)

    return df

def change_number_frontages(df:pd.DataFrame) -> pd.DataFrame:
    # #### Number of Frontages
    #get ['number of frontages'] with values and calc mean
    selected_rows = df[~df['Number of frontages'].isnull()]
    mean_num_of_frontages = selected_rows['Number of frontages'].mean(axis=0).round(0)
    # fill mean value to missing value
    df['Number of frontages'] = df['Number of frontages'].fillna(mean_num_of_frontages)
    # changing data type as int
    df['Number of frontages'] = df['Number of frontages'].astype(int)
    return df


def conv(value : str) -> int:
    #convert boolean value to number
    if value == False: 
        return 0
    elif value == True:
        return 1
    else:
        return 1

def change_garden(df:pd.DataFrame) -> pd.DataFrame:
    # #### Garden/Garden Surface & Terrace/Surface
    df['Garden'] = df['Garden'].fillna(df['Garden surface'].notnull())
    df['Garden'] = df['Garden'].apply(conv)
    return df
 

def change_terrace(df:pd.DataFrame) -> pd.DataFrame:
    df['Terrace'] = df['Terrace'].fillna(df['Terrace surface'].notnull())
    df['Terrace'] = df['Terrace'].apply(conv)
    # As it was mentioned before these columns will not be used for further analysis    
    df = df.drop(columns =['Garden surface', 'Terrace surface'])
    return df


def create_new_column(df:pd.DataFrame) -> pd.DataFrame:
    # ### Creating new Columns
    # #### Price per m2
    df['price/m2'] = (df['Price']/ df['Living area']).round(2)
    return df


def manage_outliers(df:pd.DataFrame) -> pd.DataFrame:
    df.drop(['Furnished'], axis = 1)
    # ### Dealing with Outliers
    # #### Price
    # This variable is equal to the 99th percentile of the 'Price' variable
    q = df['Price'].quantile(0.99)
    # Then we can create a new df, with the condition that all prices must be below the 99 percentile of 'Price'
    data_1 = df[df['Price']<q]
    "this way we have removed the top 1% of the data about 'Price'"
    # #### Living area
    q = data_1['Living area'].quantile(0.99)
    data_2 = data_1[data_1['Living area']< q]
    # #### Surface of the plot
    q = data_2['Surface of the plot'].quantile(0.99)
    data_3 = data_2[data_2['Surface of the plot']< q]
    # #### Number of frontages
    q = data_3['Number of frontages'].quantile(0.99)
    data_4 = data_3[data_3['Number of frontages']< q]
    # #### Bedrooms
    q = data_4['Bedrooms'].quantile(0.99)
    data_5 = data_4[data_4['Bedrooms']< q]
    data_cleaned = data_5.reset_index(drop=True)

    axis_name = ['Building condition',
    'Kitchen type',
    'Bedrooms',
    'Number of frontages',
    'Surface of the plot',
    'Living area']

    log_price = np.log(data_cleaned['Price'])
    # Then we add it to our data frame
    data_cleaned['log_price'] = log_price
    data_cleaned= data_cleaned.drop(['Price'], axis=1)

    return data_cleaned

def multicolinearity(data_cleaned:pd.DataFrame) -> pd.DataFrame:
    # ### Multicolineratiy
    variables = data_cleaned[['Building condition', 'Kitchen type', 'Bedrooms',
        'Furnished', 'Number of frontages', 'Swimming pool', 'Garden',
        'Terrace', 'Surface of the plot', 'Living area']]
    vif = pd.DataFrame() 
    vif["VIF"] = [variance_inflation_factor(variables.values, i) for i in range(variables.shape[1])]
    vif["Features"] = variables.columns
    data_no_multicollinearity = data_cleaned.drop(['Number of frontages', 'Building condition'],axis=1)
    return data_no_multicollinearity


def categorical_encoding(data_no_multicollinearity:pd.DataFrame) -> pd.DataFrame:
    # ### Categorical data encoding
    data_no_multicollinearity['Post code'].astype(str)
    post_code_stat = data_no_multicollinearity['Post code'].value_counts(ascending=False)
    """print('Total no of Poste code where data points are more than 10 = %s' % (len(post_code_stat[post_code_stat > 10])))
    print('Total no of Poste code where data points are less than 10 = %s' % (len(post_code_stat[post_code_stat <= 10])))
    """
    pc_stat_less_10 = post_code_stat[post_code_stat <= 10]
    data_post_code = data_no_multicollinearity.copy()
    data_post_code['Post code'] = data_no_multicollinearity['Post code'].apply(lambda x: 'other' if x in pc_stat_less_10 else x )
    data_no_pro_type = data_post_code.drop(columns=['Immoweb ID', 'Property type', 'price/m2'])
    data_with_dummies = pd.get_dummies(data_no_pro_type, drop_first=True)
    df_reg = data_with_dummies.copy()
    return df_reg


def start_dataframe():

    df = manage_raw_data(raw_data)
    df = change_kitchen(df)
    df = change_furnished(df)
    df = change_bedrooms(df)
    df = change_swimming_pool(df)
    df = change_surface_plot(df)
    df = change_area(df)
    df = change_number_frontages(df)
    df = change_garden(df)
    df = change_terrace(df)
    df = create_new_column(df)

    data_cleaned = manage_outliers(df)

    data_no_multicollinearity = multicolinearity(data_cleaned)

    df_reg = categorical_encoding(data_no_multicollinearity)

    return df_reg


