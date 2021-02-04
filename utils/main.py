import pandas as pd
from urllib.request import urlopen
import json

from coordinates import get_coordinates, LocationUnknownException

def get_unique_list(df):
    return df["coord"].unique()
def clean_df_trees(df):
    df = df.drop(["datasetid", "record_timestamp"], axis=1)
    df = df.rename(columns={"fields.equipement_adresse": "address", "fields.quantite": "quantity", "fields.commune_niveau_1": "municipality","fields.libelle": "text", "fields.libelle_complet": "full_text", "fields.identifiant": "tree_type"})
    return df


# # Notable trees
# url = "https://www.odwb.be/api/records/1.0/search/?dataset=arbres-remarquables&q=&rows=-1&facet=equipement_adresse&facet=libelle&facet=identifiant&facet=quantite"

# response = urlopen(url)
# json_data = response.read().decode('utf-8', 'replace')

# d = json.loads(json_data)
# df_trees = pd.json_normalize(d['records'])
# df_trees = clean_df_trees(df_trees)

# #Change columns type
# df_trees["address"] = df_trees["address"].convert_dtypes()
# df_trees["quantity"] = df_trees["quantity"].convert_dtypes()
# df_trees["municipality"] = df_trees["municipality"].convert_dtypes()
# df_trees["text"] = df_trees["text"].convert_dtypes()
# df_trees["full_text"] = df_trees["full_text"].convert_dtypes()
# df_trees["tree_type"] = df_trees["tree_type"].convert_dtypes()

# #Get coordinates (latitude,longitude)
# df_trees["address"].replace(regex="\r+\n+\t+", value=" ", inplace=True)
# df_trees["coord"] = df_trees["address"].apply(get_coordinates)
df_trees = pd.read_csv("Stuff/test.csv")

#Delete rows without coordinates
df_trees = df_trees.dropna()



# if __name__ == "__main__":
