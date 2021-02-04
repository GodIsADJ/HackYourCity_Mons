import networkx as nx
import osmnx as ox
import pandas as pd
import folium


# PRE : prend comme entrée les coordonnées de départ et d'arrivée sous forme de tuple et le poids 
# POST : retourne une liste de node du chemin le plus court entre les deux points 
def get_route (point_from : tuple,  point_to : tuple, weight) :
    ox.config(log_console=True, use_cache=True)

    origin_node =  ox.get_nearest_node(G_walk,(50.454096, 3.9418326))

    destination_node = ox.get_nearest_node(G_walk,(50.4537353, -3.9451452))

    route = nx.dijkstra_path(G_walk, origin_node, destination_node)

    return route 

# PRE : prend le réseau de route et la liste de node de la route en argument
# POST : enregistre la carte dans un fichier route.html
def generate_graph(m): 
    # save as html file then display map as an iframe
    filepath = 'route.html'
    m.save(filepath)

def tree_list() : 
    df_trees = pd.read_csv("Stuff/test.csv")
    df_trees = df_trees.dropna()
    tree_coord_list = df_trees["coord"].unique()
    return tree_coord_list 

# calcul le réseau de route de la ville de Mons
G_walk = ox.graph_from_place('Mons, Hainaut, Belgium', network_type='bike')

# coordonnées de départ et d'arrivée
point_from = (50.454096, 3.9418326) 
point_to = (50.4537353, -3.9451452)

# calcul le chemin le plus court entre deux points
route = get_route(point_from, point_to, 1)

m = ox.plot_route_folium(G_walk, route)

# récupère les coordonnées de la liste arbre
tree_list_coordinate = tree_list()

print(tree_list_coordinate[0])


folium.Marker([50.454096, 3.9418326], popup="<i>Mt. Hood Meadows</i>").add_to(m)


# génère la carte du trajet
generate_graph(m)




