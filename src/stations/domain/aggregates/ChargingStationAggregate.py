class ChargingStationAggregate:
    def __init__(self):
        self.groups = {}  # Dictionary to group stations by a key (e.g., postal code)

    def add_station(self, station, group_key):
        """
        Adds a station to a group based on the group key.

        :param station: ChargingStation object to add
        :param group_key: Key to group the station by (e.g., postal code)
        """
        if group_key not in self.groups:
            self.groups[group_key] = []
        self.groups[group_key].append(station)

    def get_group(self, group_key):
        """
        Retrieves all stations in a specific group.

        :param group_key: Key of the group to retrieve
        :return: List of ChargingStation objects
        """
        return self.groups.get(group_key, [])

    def get_all_groups(self):
        """
        Retrieves all groups of stations.

        :return: Dictionary of groups with their stations
        """
        return self.groups
    