from src.stations.domain.entities.ChargingStation import ChargingStation
from src.stations.domain.value_objects.Location import Location
from src.stations.domain.value_objects.PostalCode import PostalCode
from src.stations.domain.value_objects.Availability import Availability
import pandas as pd


class ChargingStationRepo:
    def __init__(self):
        self._stations = []  # Internal storage for ChargingStation objects

    def add(self, station):
        """
        Adds a ChargingStation to the repository if there is no station at the same location.

        :param station: ChargingStation object to add
        """
        # Check if a station with the same location already exists
        for existing_station in self._stations:
            if (existing_station.location.postal_code.code == station.location.postal_code.code and
                    existing_station.location.latitude == station.location.latitude and
                    existing_station.location.longitude == station.location.longitude):
                raise ValueError("A ChargingStation already exists at this location.")

        # If no existing station is found at the same location, add the new station
        self._stations.append(station)

    def remove(self, station_id):
        """
        Removes a ChargingStation from the repository by ID.

        :param station_id: ID of the station to remove
        """
        self._stations = [s for s in self._stations if s.id != station_id]

    def find_by_id(self, station_id):
        """
        Finds a ChargingStation by its ID.

        :param station_id: ID of the station to find
        :return: ChargingStation object or None if not found
        """
        for station in self._stations:
            if station.id == station_id:
                return station
        return None

    def find_all(self):
        """
        Retrieves all ChargingStations in the repository.

        :return: List of ChargingStation objects
        """
        return self._stations

    def find_by_postal_code(self, postal_code):
        """
        Finds all ChargingStations in a specific postal code.

        :param postal_code: Postal code to filter stations by
        :return: List of ChargingStation objects
        """
        return [station for station in self._stations if postal_code in str(station.location.postal_code.code)]

    def find_available(self):
        """
        Finds all available ChargingStations.

        :return: List of ChargingStation objects
        """
        return [station for station in self._stations if station.is_available]

    def load_data_from_csv(self, csv_path):
        """
        Loads ChargingStations from a CSV file.

        :param csv_path: Path to the CSV file to load
        """
        dataframe = pd.read_csv(csv_path, sep=";")

        # Convert to string and replace commas with periods
        dataframe['Breitengrad'] = dataframe['Breitengrad'].astype(str).str.replace(',', '.')
        dataframe['Längengrad'] = dataframe['Längengrad'].astype(str).str.replace(',', '.')
        dataframe['Nennleistung Ladeeinrichtung [kW]'] = dataframe['Nennleistung Ladeeinrichtung [kW]'].astype(str).str.replace(',','.')


        for idx, row in dataframe.iterrows():
            try:
                postal_code = int(row['Postleitzahl'])
                # Try to create Location object with postal code, latitude, and longitude
                location = Location(postal_code=postal_code, latitude=float(row['Breitengrad']),
                                    longitude=float(row['Längengrad']))
                availability = Availability("available")
                charging_station = ChargingStation(id=len(self._stations), location=location, availability=availability,
                                                   power=float(row['Nennleistung Ladeeinrichtung [kW]']))
                self.add(charging_station)  # Add the charging station to the repository
            except ValueError as e:
                # If an error occurs (e.g., invalid postal code or other issue), log the error and skip the row
                print(f"Skipping row {idx} due to error: {e}")
                continue
