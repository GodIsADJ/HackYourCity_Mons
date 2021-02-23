import osmnx as ox
import networkx as nx
import pandas as pd
import folium
from folium.plugins import MarkerCluster

def demo_map1():

    ox.config(log_console=True, use_cache=True)

    G_walk = ox.graph_from_place('Mons, Hainaut, Belgium',simplify=False, network_type='walk')

    orig_node = ox.get_nearest_node(G_walk,
                                    (50.454096, 3.9418326))

    dest_node = ox.get_nearest_node(G_walk,
                                    (50.455476, 3.9517038))

    route = nx.shortest_path(G_walk,
                            orig_node,
                            dest_node, weight='lenght')

    ox.folium.plot_route_folium

    route_map = ox.plot_route_folium(G_walk, route)



    # récupère les coordonnées de la liste arbre
    df_trees = pd.read_csv("data/test.csv")
    df_trees = df_trees.dropna()
    tree_coord_list = df_trees["coord"].unique()

    for i, coord in enumerate(tree_coord_list, start=0) : 

        coord = tree_coord_list[i]
        coord = coord.replace("[", "")
        coord = coord.replace("]", "")
        l = coord.split(",")

        latitude = l[0]
        longitude = l[1]

        latitude = float(l[0])
        longitude = float(l[1])
        icon_url = 'static/icones/tree_icone.png'
        popup = popup = '<strong>' + "Tilleul (Tilia)/Tilleul de Hollande : la légende raconte que le bois de ses ancêtres aurait servi à fabriquer des lances pour combattre le doudou" + '</strong>'
        icon = folium.features.CustomIcon(icon_url,icon_size=(28, 30))  # Creating a custom Icon
        folium.Marker([latitude, longitude], icon=icon, popup = popup).add_to(route_map)


    icon_path = 'static/icones/station.png'
    icon = folium.features.CustomIcon(icon_path,icon_size=(28, 30))
    folium.Marker([50.454096, 3.9418326], icon=icon).add_to(route_map)

    popup = popup = '<strong>' + 'hello doudou' + '</strong>'
    icon_path = 'static/icones/musee_doudou.png'
    icon = folium.features.CustomIcon(icon_path,icon_size=(28, 30))
    folium.Marker([50.455476, 3.9517038], icon=icon, popup=popup).add_to(route_map)

    df = pd.read_csv('data/arceaux-velos_publication.csv',sep=';')
    parking_bike = df['Geo Point']

    for i, coord in enumerate(parking_bike, start=0) : 

        l = coord.split(",")

        latitude = l[0]
        longitude = l[1]

        icon_url = 'static/icones/parking_bike.png'
        icon = folium.features.CustomIcon(icon_url,icon_size=(28, 30))  # Creating a custom Icon
        folium.Marker([latitude,longitude], icon=icon).add_to(route_map)

    df = pd.read_csv('data/monuments_mons_lat_lon.csv')
    monuments = df['coordinate']
    df = df.dropna()

    for i, coord in enumerate(latitude, start=0) : 

        latitude = df['latitude'][i]
        longitude = df['longitude'][i]

        icon_url = 'static/icones/monument.png'
        icon = folium.features.CustomIcon(icon_url,icon_size=(28, 30))  # Creating a custom Icon
        folium.Marker([latitude,longitude], icon=icon).add_to(route_map)

    icon_path = 'static/icones/bike.png'
    icon = folium.features.CustomIcon(icon_path,icon_size=(28, 30))
    folium.Marker([50.45871144, 3.95662095], icon=icon).add_to(route_map)

    icon_path = 'static/icones/bike.png'
    icon = folium.features.CustomIcon(icon_path,icon_size=(28, 30))
    folium.Marker([50.45505764, 3.95287386], icon=icon).add_to(route_map)

    icon_path = 'static/icones/bike.png'
    icon = folium.features.CustomIcon(icon_path,icon_size=(28, 30))
    folium.Marker([50.45535941, 3.95968002], icon=icon).add_to(route_map)

    icon_path = 'static/icones/bike.png'
    icon = folium.features.CustomIcon(icon_path,icon_size=(50, 50))
    folium.Marker([50.45144295, 3.94943058], icon=icon).add_to(route_map)

    icon_path = 'static/icones/bike.png'
    icon = folium.features.CustomIcon(icon_path,icon_size=(50, 50))
    folium.Marker([50.454827, 3.940081], icon=icon).add_to(route_map)

    icon = folium.features.CustomIcon(icon_path,icon_size=(50, 50))
    folium.Marker([50.454753, 3.940031], icon=icon).add_to(route_map)

    return route_map._repr_html_()