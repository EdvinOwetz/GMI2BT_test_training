# -*- coding: utf-8 -*-
'''booli_flatten.py'''

import json
from turtle import showturtle
import pandas as pd
# pip install cherrypicker
from cherrypicker import CherryPicker
import matplotlib as mlt
import matplotlib.pyplot as plt
from scipy.__config__ import show
import seaborn as sns

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
    df = pd.read_csv('villa_dalarna_1000.csv',sep=';')
    print(df)
    print("HEAD", df.head(2))
    print("INFO", df.info())
    
    #print("SUM - ISNULL", df.isnull().sum())
    #df.dropna(inplace=True,axis=1)
    print("DROPPED None AND NULL!")
    #new_dataframe=pd.DataFrame()
    #new_dataframe['rooms']=df['rooms']
    #print(df['rooms'])
    new_dataframe=pd.DataFrame(df[['location_region_municipalityName', 'constructionYear', 'listPrice', 'plotArea', 'livingArea', 'rooms', 'soldDate', 'soldPrice', 'location_position_latitude', 'location_position_longitude']])

    print("NEW DATAFRAME", new_dataframe)
    print(new_dataframe.info())
    
    #new_dataframe.dropna(inplace=True)
    print("The after image? ", new_dataframe)
    print(new_dataframe.info())
    
    print("The mean value? ",new_dataframe.mean())
    
    print(new_dataframe["location_region_municipalityName"].unique())
    
    print(new_dataframe.fillna(new_dataframe.mean()))
    
    ort=new_dataframe["location_region_municipalityName"].unique()
    
    dataframelista=[]
    for item in ort:
        tmp_df=new_dataframe.loc[new_dataframe['location_region_municipalityName']==item]
        tmp_df=tmp_df.mean()
        dataframelista.append(tmp_df)

    yetanother_dataframe=pd.DataFrame(dataframelista)
    print(yetanother_dataframe.columns)
    yetanother_dataframe.insert(loc=0, column="ort", value=ort)
    origin_column=list(yetanother_dataframe.columns)
    column_list=["County", "Year", "List Price", "plotArea", "Area", "Rooms", "Sold Date", "Sold Price", "Latitude", "Longitude"]
    yetanother_dataframe.rename(columns=dict(zip(origin_column,column_list)),inplace=True)
    yetanother_dataframe["price_m2"] = yetanother_dataframe["Sold Price"] / yetanother_dataframe["Area"]
    
    print(yetanother_dataframe)
    
    #sns.countplot(new_dataframe["rooms"])
    #plt.show()
    sns.countplot(new_dataframe["location_region_municipalityName"])
    plt.show()
    
    sns.boxplot(x=new_dataframe["rooms"],y=new_dataframe["soldPrice"])
    plt.show()
    
    
    #sns.plot(x=new_dataframe["listPrice"],y=new_dataframe["livingArea"]) 
    #sns.scatterplot(x=new_dataframe["listPrice"],y=new_dataframe["livingArea"])
    #sns.lineplot(y=new_dataframe["listPrice"],x=new_dataframe["livingArea"])
    #plt.show()
    #yetanother_dataframe.plot.bar(yetanother_dataframe["Rooms"],yetanother_dataframe["Area"])
    #plt.plot(yetanother_dataframe["Rooms"],yetanother_dataframe["plotArea"])
    #plt.show()
    #print(df)
    
    
# location_address_streetAddress;location_position_latitude;location_position_longitude;location_namedAreas_0;location_region_municipalityName;location_region_countyName;listPrice;livingArea;additionalArea;plotArea;source_name;
# source_id;source_type;source_url;rooms;published;constructionYear;objectType;booliId;soldDate;soldPrice;soldPriceSource;url;location_address_city;rent;location_position_isApproximate;floor;location_distance_ocean;apartment

    # Dubbelkolla NaN
    # Droppa NaN
    # Lägg till kolumn price_m2 (soldPrice/livingArea)
    #df['soldPrice/livingArea'] = df['soldPrice']/df['livingArea']
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
