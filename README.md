# HackYourCity_Mons

The municipality of Mons asked us to develop a website that would increase tourism in the city. They also explained to us how the lack of parking space was preventing tourism from developing.
During 3 days we developed a prototype to answer this.
The general idea is to promote bicycle trips by allowing a person or a family to organize their day. 
On one hand, they have a list of events, museums, ...
On the other hand, they can organize their trips by taking advantage of points of interest such as monuments, remarkable trees, ...

## The team
[Austin](https://github.com/Achouffe666)  
[Axelle](https://github.com/GodIsADJ)  
[Lise](https://github.com/lise-amen)  
[Pierre](https://github.com/Wasilp)

## Usage
Run the `routes.py` file in tour termial : `python routes.py`
Access the API by using this url : http://localhost:5000/

## Folder hierarchy
```
HackYourCity_Mons
|   .gitignore
|   README.md
|   routes.py : The back-end running with Flask
|   
+---clustering_station_velo
|       cluster.py : A machine learning algorithm to help the city of Mons to choose where to place bicycle parking
|       
+---data : The csv files we can use
|       ...
|       
+---static : The html style (css, ...)
|       ...
|           
+---templates
|       index.html : The default html page (with the list of events)
|       route.html : The second page (with he map)
|       
\---utils
    |   coordinates.py : returns a latitude and longitude from an address
    |   map.py : return the map created with folium
    |   notable_trees.py : This file cleans up the list of remarkable trees. 
    |       It can be used as a basis for any other CSV containing data you wish to display on the map.
    |               
```

## Documentation of the libraries we have used
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) : To display the website
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html) : to clean the dataset
- [Geopy](https://geopy.readthedocs.io/en/latest/) : To get the coordinates
- [Osmnx](https://osmnx.readthedocs.io/en/stable/osmnx.html) : to manipulate coordinates
- [Folium](https://python-visualization.github.io/folium/) : to diplay a map of New York