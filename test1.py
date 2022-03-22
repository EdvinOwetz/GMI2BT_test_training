

import pandas as pd

import json

upg1_list = []

json_data=json.load(open(r'booli\villa\villa_dalarna_1000.json'))

pd.DataFrame.info(json_data['sold'])

#for jsonitem in json_data["sold"]:

    
#    upg1_list.append()



#df = pd.DataFrame(json_data["sold"])
#df = pd.DataFrame.from_dict(json_data["sold"])
#print(df)
#df.to_csv(r'ftkimm_random_fml_jolo_etc.csv', index = None)

