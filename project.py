import folium
import random
import webbrowser

# Coordinates of 4 intersections (customize for your city)
intersections = {
   "Dehradun": (30.3165, 78.0322),
    "Delhi": (28.7041, 77.1025),
    "Noida": (28.5355, 77.3910),
    "Jaipur": (26.9124, 75.7873)

}

def get_color(traffic_density):
    if traffic_density <= 5:
        return 'green'
    elif traffic_density <= 12:
        return 'orange'
    else:
        return 'red'

def simulate_traffic_map():
    # Create a base map
    traffic_map = folium.Map(location=[28.6, 77.2], zoom_start=10)

    for name, coords in intersections.items():
        # Simulate traffic density (0 to 20)
        traffic_density = random.randint(0, 20)
        color = get_color(traffic_density)

        # Add marker to the map
        folium.CircleMarker(
            location=coords,
            radius=10,
            popup=f"{name}\nTraffic: {traffic_density} vehicles",
            color=color,
            fill=True,
            fill_color=color
        ).add_to(traffic_map)

    # Save and open the map
    traffic_map.save("smart_traffic_map.html")
    webbrowser.open("smart_traffic_map.html")

# Run the simulation
simulate_traffic_map()
