################################################################################################
#       IF THE CODE DOESNT WORK AND MAKES MODULES IMPORTING ERRORS, DO :
#       export PYTHONPATH=:PYTHONPATH:(location of project)/Advanced-Software-Engineering (linux)
#       set PYTHONPATH=%PYTHONPATH%;(location of project)\Advanced-Software-Engineering  (windows cmd)
#       $env:PYTHONPATH="$env:PYTHONPATH;(location of project)\Advanced-Software-Engineering" (windows powershell)
################################################################################################
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

from src.stations.infrastructure.repositories.ChargingStationRepo import ChargingStationRepo
from src.stations.application.services.ChargingStationService import ChargingStationService

# Chemin vers le projet
project_loc = r"C:\Users\INSA\Documents\GitHub\Advanced-Software-Engineering"

# Cache the repository initialization to avoid reloading the data on every interaction
@st.cache_resource
def get_charging_station_repo():
    repo = ChargingStationRepo()
    repo.load_data_from_csv(f"{project_loc}/src/shared/infrastructure/datasets/Ladesaeulenregister.csv")
    return repo

# Cache the service initialization, but pass the repo as a non-hashable argument by renaming it
@st.cache_resource
def get_charging_station_service(_repo):
    return ChargingStationService(_repo)

# Streamlit app
st.title('Map of Electric Charging Stations')

# Initialize services and repositories
charging_station_repo = get_charging_station_repo()
charging_station_service = get_charging_station_service(charging_station_repo)

# Add a text input for postal code search
search_plz = st.text_input("Enter Postal Code (PLZ) to filter:", "")

# Filter the charging stations by the entered postal code
if search_plz:
    filtered_stations = charging_station_service.find_by_postal_code(search_plz)
else:
    filtered_stations = charging_station_service.get_all_charging_stations()

if not filtered_stations:
    st.warning(f"No charging stations found for postal code: {search_plz}")

# Create a Folium map
m = folium.Map(location=[52.52, 13.40], zoom_start=10)

# Use MarkerCluster to cluster markers
marker_cluster = MarkerCluster(
    disableClusteringAtZoom=14,  # Stop clustering beyond zoom level 14
    maxClusterRadius=50          # Increase cluster radius to group markers more aggressively
).add_to(m)

# Add markers for each charging station in the filtered list
cmap = {
    "available": "green",      # State "available" is green
    "unavailable": "red",      # State "unavailable" is red
    "maintenance": "orange"    # State "maintenance" is orange
}
for station in filtered_stations:
    tooltip = f"ID : {station.id}, PLZ : {station.location.postal_code.code}, availability : {station.availability.state}"
    folium.Marker(
        location=[station.location.latitude, station.location.longitude],
        tooltip=tooltip,
        icon=folium.Icon(color=cmap[station.availability.state])
    ).add_to(marker_cluster)

# Display the map in Streamlit
folium_static(m, width=800, height=600)
