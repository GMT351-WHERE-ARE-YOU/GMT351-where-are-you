#Melih Altay Flask test_1


from flask import  Flask
import folium



app = Flask(__name__)

@app.route("/")

def base():
    # this is base map
    map = folium.Map(
        location=[39.885036, 32.733902]
    )
    return map._repr_html_()

@app.route("/open-street-map")
def open_street_map():
    # this map using stamen toner
    map = folium.Map(
        location=[39.885036, 32.733902],
        tiles='Stamen Toner',
        zoom_start=13
    )
    return map._repr_html_()

@app.route("/map-marker")
def map_marker():
    # this map using stamen terrain
    # we add some marker here
    map=folium.Map(
        location=[39.885036, 32.733902],
        tiles="Stamen Terrain",
        zoom_start=12

    )
    folium.Marker(
        location=[39.885036, 32.733902],
        popup="<b>Marker here<b>",
        tooltip="Click Here"

    ).add_to(map)

    folium.Marker(
        location=[39.886036, 32.833902],
        popup="<b>Marker here<b>",
        tooltip="Click Here",
        icon=folium.Icon(color="green")

    ).add_to(map)
    return map._repr_html_()
if __name__=="__main__":
    app.run(debug=True)
