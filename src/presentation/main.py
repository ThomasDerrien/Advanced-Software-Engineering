import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from datetime import datetime

# Import domain and infrastructure
from src.community.domain.entities.Rating import Rating
from src.community.domain.value_objects.RatingValue import RatingValue
from src.community.domain.events.RatingCreatedEvent import RatingCreatedEvent
from src.community.infrastructure.repositories.RatingRepository import RatingRepository
from src.community.application.services.RatingService import RatingService
from src.stations.domain.value_objects.PostalCode import PostalCode
from src.stations.infrastructure.repositories.ChargingStationRepo import ChargingStationRepo
from src.stations.application.services.ChargingStationService import ChargingStationService

# Path to project
PROJECT_LOC = r"C:\Users\INSA\Documents\GitHub\Advanced-Software-Engineering"


# Cache the repository initialization for ratings
@st.cache_resource
def get_rating_repo():
    return RatingRepository()


# Cache the service initialization for ratings, passing the charging station service as a non-hashable argument
@st.cache_resource
def get_rating_service(_rating_repo, _charging_station_service):
    return RatingService(_rating_repo, _charging_station_service)


@st.cache_resource
def get_charging_station_repo():
    repo = ChargingStationRepo()
    repo.load_data_from_csv(f"{PROJECT_LOC}/src/shared/infrastructure/datasets/Ladesaeulenregister.csv")
    return repo


# Cache the service initialization, but pass the repo as a non-hashable argument by renaming it
@st.cache_resource
def get_charging_station_service(_repo):
    return ChargingStationService(_repo)


# Streamlit app title and styling
st.set_page_config(page_title="ChargeHubBerlin", page_icon="⚡", layout="wide")
st.title("ChargeHubBerlin")
st.markdown("""
    Welcome to **ChargeHubBerlin**, your platform to explore charging stations, post ratings, and view reviews!
    """)

# Initialize repositories and services
charging_station_repo = get_charging_station_repo()
charging_station_service = get_charging_station_service(charging_station_repo)
rating_repo = get_rating_repo()
rating_service = get_rating_service(rating_repo, charging_station_service)

# Sidebar navigation with icons and styling
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a Page", ["Map View", "Post a Rating", "View Ratings"], index=0)

# Map View Page
if page == "Map View":
    st.header("Explore Charging Stations on the Map")

    # Text input for postal code search
    search_plz = st.number_input("Enter Postal Code (PLZ) to filter:", min_value=0, max_value=99999, step=1)
    try:
        postal_code = PostalCode(search_plz)
    except ValueError:
        st.warning("Please enter a valid postal code")

    # Filter stations based on postal code
    filtered_stations = charging_station_service.find_by_postal_code(
        search_plz) if search_plz else charging_station_service.get_all_charging_stations()

    if not filtered_stations:
        st.warning(f"No charging stations found for postal code: {search_plz}")

    m= folium.Map(location=[52.52, 13.40], zoom_start=10)

    # Marker cluster with customization
    marker_cluster = MarkerCluster(
        disableClusteringAtZoom=14,
        maxClusterRadius=50
    ).add_to(m)

    # Marker color mapping
    cmap = {"available": "green", "unavailable": "red", "maintenance": "orange"}
    for station in filtered_stations:
        tooltip = f"Name: {station.name[:10]}..., PLZ: {station.location.postal_code.code}, Availability: {station.availability.state}"
        folium.Marker(
            location=[station.location.latitude, station.location.longitude],
            tooltip=tooltip,
            icon=folium.Icon(color=cmap.get(station.availability.state, "blue"))
        ).add_to(marker_cluster)

    folium_static(m, width=800, height=600)

# Post a Rating Page
elif page == "Post a Rating":
    st.header("Post a Rating for a Charging Station")

    # Filter stations based on postal code
    search_plz = st.number_input("Enter Postal Code (PLZ) to filter:", min_value=0, max_value=99999, step=1)
    try:
        postal_code = PostalCode(search_plz)
    except ValueError:
        st.warning("Please enter a valid postal code")
    filtered_stations = charging_station_service.find_by_postal_code(
        search_plz) if search_plz else charging_station_service.get_all_charging_stations()

    if filtered_stations:

        # Station selection
        station_names = [station.name for station in filtered_stations]
        selected_station_name = st.selectbox("Select a Station to Rate", station_names)
        station_id = dict(zip(station_names, [station.id for station in filtered_stations]))[selected_station_name]

        # Rating and review form
        with st.form("rating_form"):
            rating = st.slider("Rate this station (1-5)", 1, 5, key="rating")
            review = st.text_area("Write a review", placeholder="Share your experience...")
            submit_button = st.form_submit_button("Submit Rating")

        if submit_button:
            try:
                # Create Rating entity
                rating_value = RatingValue(rating)
                station = charging_station_service.repository.find_by_id(station_id)
                rating_entity = Rating(id=f"{station_id}-{datetime.now().timestamp()}", value=rating_value,
                                       station_id=station_id, text=review)

                # Submit rating and trigger event
                rating_service.rating_repository.add(rating_entity)
                RatingCreatedEvent(rating_entity).publish()

                st.success(f"Your rating of {rating} and review has been submitted. Thank you!")
            except Exception as e:
                st.error(f"Error submitting the rating: {e}")
    else:
        st.warning(f"No charging stations found for postal code: {search_plz}")

# View Ratings Page
elif page == "View Ratings":
    st.header("View Ratings for a Charging Station")

    # Filter stations by postal code
    search_plz = st.number_input("Enter Postal Code (PLZ) to filter:", min_value=0, max_value=99999, step=1)
    try:
        postal_code = PostalCode(search_plz)
    except ValueError:
        st.warning("Please enter a valid postal code")
    filtered_stations = charging_station_service.find_by_postal_code(
        search_plz) if search_plz else charging_station_service.get_all_charging_stations()

    if filtered_stations:
        # Select station to view ratings
        station_names = [station.name for station in filtered_stations]
        selected_station_name = st.selectbox("Select a Station to View Ratings", station_names)
        selected_station_id = dict(zip(station_names, [station.id for station in filtered_stations]))[
            selected_station_name]

        # Retrieve and display ratings
        ratings = rating_service.rating_repository.find_by_station_id(selected_station_id)
        if ratings:
            for rating in ratings:
                # Determine color and emoji based on rating value
                color = "#D4EDDA" if rating.ratingValue.value >= 4 else "#FFF3CD" if rating.ratingValue.value == 3 else "#F8D7DA"
                emoji = "😊" if rating.ratingValue.value >= 4 else "😐" if rating.ratingValue.value == 3 else "😞"

                # Display styled rating
                st.markdown(f"""
                <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; margin-bottom: 10px; background-color: {color};">
                    <h4 style="margin-bottom: 5px;">Rating: {emoji} {rating.ratingValue.value}/5</h4>
                    <p style="margin-bottom: 0;">{rating.text}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"No ratings found for this station.")
    else:
        st.warning(f"No charging stations found for postal code: {search_plz}")