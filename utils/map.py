import networkx as nx
import osmnx as ox
import folium
from utils.notable_trees import get_notable_trees, get_unique_list

def get_map(point_from: tuple=(50.454096, 3.9418326),  point_to: tuple=(50.4537353, -3.9451452)):
    G_walk = ox.graph_from_place('Mons, Hainaut, Belgium', network_type='bike')
    ox.config(log_console=True, use_cache=True)
    origin_node = ox.get_nearest_node(G_walk, point_from)
    destination_node = ox.get_nearest_node(G_walk, point_to)
    route = nx.bellman_ford_path(G_walk, origin_node, destination_node)
    m = ox.plot_route_folium(G_walk, route)

    df_trees = get_notable_trees()
    tree_list_coordinate = get_unique_list(df_trees)

    for i, coord in enumerate(tree_list_coordinate, start=0):

        coord = tree_list_coordinate[i]
        coord = coord.replace("[", "")
        coord = coord.replace("]", "")
        l = coord.split(",")

        latitude = l[0]
        longitude = l[1]

        latitude = float(l[0])
        longitude = float(l[1])

        folium.Marker([latitude, longitude],
                      popup="<i>Mt. Hood Meadows</i>").add_to(m)

    return m._repr_html_()
