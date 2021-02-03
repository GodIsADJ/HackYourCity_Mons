import pandas as pd
from urllib.request import urlopen
import json


def clean_df_trees(df):
    df = df.drop(["datasetid","record_timestamp"],axis=1)
    df = df.rename(columns={"fields.equipement_adresse":"adress","fields.quantite":"quantity","fields.commune_niveau_1":"municipality","fields.libelle":"text","fields.libelle_complet":"full_text","fields.identifiant":"tree_type"})
    return df


# Notable trees
url = "https://www.odwb.be/api/records/1.0/search/?dataset=arbres-remarquables&q=&rows=-1&facet=equipement_adresse&facet=libelle&facet=identifiant&facet=quantite"

response = urlopen(url)
json_data = response.read().decode('utf-8', 'replace')

d = json.loads(json_data)
df_trees = pd.json_normalize(d['records'])
df_trees = clean_df_trees(df_trees)

print(df_trees.columns)

# if __name__ == "__main__":
    
