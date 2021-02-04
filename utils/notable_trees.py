import pandas as pd
from urllib.request import urlopen
import json
from coordinates import get_coordinates, LocationUnknownException


def get_unique_list(df):
    return df["coord"].unique()


def __clean_df_trees(df):
    df = df.drop(["datasetid", "record_timestamp"], axis=1)
    df = df.rename(columns={"fields.equipement_adresse": "address", "fields.quantite": "quantity", "fields.commune_niveau_1": "municipality",
                            "fields.libelle": "text", "fields.libelle_complet": "full_text", "fields.identifiant": "tree_type"})

    #Change columns type
    df["address"] = df["address"].convert_dtypes()
    df["quantity"] = df["quantity"].convert_dtypes()
    df["municipality"] = df["municipality"].convert_dtypes()
    df["text"] = df["text"].convert_dtypes()
    df["full_text"] = df["full_text"].convert_dtypes()
    df["tree_type"] = df["tree_type"].convert_dtypes()

    return df


def __get_coordinates(df):
    #Get coordinates (latitude,longitude)
    # df["address"].replace(regex="\r+\n+\t+", value=" ", inplace=True)
    # df["coord"] = df["address"].apply(get_coordinates)
    # df.to_csv("Stuff/test.csv")
    df = pd.read_csv("Stuff/test.csv")

    #Delete rows without coordinates
    df = df.dropna()
    return df


def get_notable_trees():
    # # Notable trees
    url = "https://www.odwb.be/api/records/1.0/search/?dataset=arbres-remarquables&q=&rows=-1&facet=equipement_adresse&facet=libelle&facet=identifiant&facet=quantite"

    response = urlopen(url)
    json_data = response.read().decode('utf-8', 'replace')

    d = json.loads(json_data)
    df_trees = pd.json_normalize(d['records'])

    df_trees = __clean_df_trees(df_trees)
    df_trees = __get_coordinates(df_trees)

    return df_trees
