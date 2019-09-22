import folium

map = folium.Map(location=[12.958016, 77.744033],
                 zoom_start=1, tiles="openstreetmap")
# folium.TileLayer('openstreetmap').add_to(map)
map.save("f.html")

number = 4 + 4
