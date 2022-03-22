# -*- coding: utf-8 -*-
'''booli_flatten.py'''

import json
import pandas as pd
# pip install cherrypicker
from cherrypicker import CherryPicker

#prova att köra!

def main():
    
    # WORKING DIRECTORY ÄR RELATIV TILL VAR DU ÖPPNAR VSCODE
    # INTE TILL VAR PYTHON FILEN DU KÖR ÄR SÅ OM DU SKA ÖPPNA villa_dalarna_1000.json
    # även om filerna ligger i samma mapp så öppnar man villa_dalarna_1000.json den via open(r"booli/villa/villa_dalarna_1000.json") INTE open(r"villa_dalarna_1000.json")
    # "#¤&¤"#¤"¤"#¤"#%&#&/ 
    with open(r'booli\villa\villa_dalarna_1000.json') as jf:
        result = json.load(jf)
    picker = CherryPicker(result)
    flat = picker['sold'].flatten().get()
    df_cherry = pd.DataFrame(flat)
    print(f'\ndf_cherry\n{df_cherry}')
    # using pandas to write CSV, ';'-separator, do not write the index, header/column names will be on first row
    df_cherry.to_csv('villa_dalarna_1000.csv', index=False, sep=';')

    # --| upg 1 |--
    df = pd.read_csv('villa_dalarna_1000.csv')
    print("HEAD", df.head(2))
    print("INFO", df.info())
    
    print("SUM - ISNULL", df.isnull().sum())
    #df.dropna()
    print("DROPPED None AND NULL!")
    #new_dataframe=pd.DataFrame()
    #new_dataframe['rooms']=df['rooms']
    print(df['rooms'])
    #new_dataframe=pd.DataFrame(df[['location_region_municipalityName', 'constructionYear', 'listPrice', 'plotArea', 'livingArea', 'rooms', 'soldDate', 'soldPrice', 'location_position_latitude', 'location_position_longitude']])

    #print("NEW DATAFRAME", new_dataframe)
# location_address_streetAddress;location_position_latitude;location_position_longitude;location_namedAreas_0;location_region_municipalityName;location_region_countyName;listPrice;livingArea;additionalArea;plotArea;source_name;
# source_id;source_type;source_url;rooms;published;constructionYear;objectType;booliId;soldDate;soldPrice;soldPriceSource;url;location_address_city;rent;location_position_isApproximate;floor;location_distance_ocean;apartment

    # Dubbelkolla NaN
    # Droppa NaN
    # Lägg till kolumn price_m2 (soldPrice/livingArea)
    # df['soldPrice/livingArea'] = df['soldPrice']/df['livingArea']
    # --| upg 2 |--

    # group_by() med municipalityName och visualisera medelvärden för hela Dalarna.
    #print(df.groupby('location_region_municipalityName','constructionYear').mean())
    # och/eller group_by() a) rooms, b) constructionYear or c) municipalityName
    # Visualisera med bar plots för varje outcome!

    # --| upg 3 |--

    # Boxplotta antal rum (rooms) vs soldPrice.
    # Ta bort outliers om nödvändigt.
    # Upprepa för plotArea och livingArea.

    # --| upg 4 |--

    # Hur korrelerar livingArea mot soldPrice? jointplot!
    # 
    # 


if __name__ == "__main__":
    main()
