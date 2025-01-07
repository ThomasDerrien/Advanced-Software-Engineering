from domain.entities.ChargingStation import ChargingStation
from domain.value_objects.Location import Location
from domain.value_objects.PostalCode import PostalCode
from domain.value_objects.Availability import Availability
import pandas as pd
class ChargingStationRepo:
    def __init__(self):
        self._stations = []  # Internal storage for ChargingStation objects

    def add(self, station):
        """
        Adds a ChargingStation to the repository.

        :param station: ChargingStation object to add
        """
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

    def load_data_from_csv(self,csv_path):
            # Load data from the data source (e.g., CSV file, database, etc.)
            dataframe = pd.read_csv(csv_path,sep=";")

            # Convert to string
            dataframe['Breitengrad']  = dataframe['Breitengrad'].astype(str)
            dataframe['Längengrad']   = dataframe['Längengrad'].astype(str)

            # Now replace the commas with periods
            dataframe['Breitengrad']  = dataframe['Breitengrad'].str.replace(',', '.')
            dataframe['Längengrad']   = dataframe['Längengrad'].str.replace(',', '.')

            dataframe                 = dataframe[(dataframe["Bundesland"] == 'Berlin') & 
                                                    (dataframe["Postleitzahl"] > 10115) &  
                                                       (dataframe["Postleitzahl"] < 14200)]
            charging_stations = []
            for idx, row in dataframe.iterrows():
                postal_code = row['Postleitzahl']
                location = Location(postal_code=postal_code,latitude=float(row['Breitengrad']), longitude=float(row['Längengrad']))
                availability = Availability("available")
                charging_station = ChargingStation(id=len(self._stations), location=location, availability=availability, power=row['Nennleistung Ladeeinrichtung [kW]'])
                self.add(charging_station)