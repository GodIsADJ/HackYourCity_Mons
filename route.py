import networkx as nx
import osmnx as ox


# PRE : prend comme entrée les coordonnées de départ et d'arrivée sous forme de tuple et le poids 
# POST : retourne une liste de node du chemin le plus court entre les deux points 
def get_route (point_from : tuple,  point_to : tuple, weight) :
    ox.config(log_console=True, use_cache=True)

    origin_node =  ox.get_nearest_node(G_walk,(50.454096, 3.9418326))

    destination_node = ox.get_nearest_node(G_walk,(50.4537353, -3.9451452))

    route = nx.dijkstra_path(G_walk, origin_node, destination_node)

    return route 

# POST : enregistre la carte dans un fichier route.html
def generate_graph(): 
    # plot the route with folium
    # like above, you can pass keyword args along to folium PolyLine to style the lines
    m2 = ox.plot_route_folium(G_walk, route)
    # save as html file then display map as an iframe
    filepath = 'route.html'
    m2.save(filepath)



# calcul le réseau de route de la ville de Mons
G_walk = ox.graph_from_place('Mons, Hainaut, Belgium', network_type='bike')

# coordonnées de départ et d'arrivée
point_from = (50.454096, 3.9418326) 
point_to = (50.4537353, -3.9451452)

# calcul le chemin le plus court entre deux points
route = get_route(point_from, point_to, 1)

# génère la carte du trajet
generate_graph()



