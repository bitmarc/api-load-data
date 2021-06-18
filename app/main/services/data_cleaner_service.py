"""
    Methods to manage files processing
"""

import pandas as pd


def parse_xlsx(file_path):
    """ Method to load file xlsx into dataframe object and prepare it to iterate """
    COL_NAMES=[
           "code",
           "name",
           "birth_date",
           "naturalization_date",
           "contract_date",
           "end_date",
           "driver_license_validity",
           "gender"
    ]
    df = pd.read_excel(file_path, usecols="A:H", header=None,names=COL_NAMES)
    df.drop([0],axis=0, inplace=True)
    df=df[df['code'].notna()]
    df.drop_duplicates(['code'],keep='last', inplace=True)

    df[
        [
            'birth_date',
            'naturalization_date',
            'contract_date','end_date',
            'driver_license_validity'
        ]
    ]=df[
        [
            'birth_date',
            'naturalization_date',
            'contract_date','end_date',
            'driver_license_validity'
        ]
    ].apply(
        pd.to_datetime,
        format='%Y-%m-%d',
        errors='coerce'
    )

    df[
        [
            'birth_date',
            'naturalization_date',
            'contract_date',
            'end_date',
            'driver_license_validity'
        ]
    ]=df[
        [
            'birth_date',
            'naturalization_date',
            'contract_date',
            'end_date',
            'driver_license_validity'
        ]
    ].astype(str)
    
    df.replace({'NaT':None},regex=True, inplace=True)
    return df