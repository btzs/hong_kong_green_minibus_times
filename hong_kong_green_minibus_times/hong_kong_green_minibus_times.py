"""Main module."""


import requests
import time

class BusClient():
    def __init__(self):
        self.api_url = 'https://data.etagmb.gov.hk/'
        self.bus_route = 'route'
        self.bus_stop = 'stop'
        self.bus_route_stop = 'route-stop'
        self.bus_eta = 'eta'
    
    # get bus routes available in region
    def get_bus_routes(self, region):
        return requests.get(self.api_url + self.bus_route + '/' + region).json()
    
    # get bus route data
    def get_bus_route_data(self, region, route_code):
        return requests.get(self.api_url + self.bus_route + '/' + region + '/' + route_code).json()
    
    # get bus route stops by route id and route sequence 
    def get_bus_route_stops_by_id(self, route_id, route_seq):
        return requests.get(self.api_url + self.bus_route_stop + '/' + str(route_id) + '/' + str(route_seq)).json()

    def get_arrivals_by_stop(self, route_id, stop_id):
        # /eta/route-stop/{route_id}/{stop_id}
        return requests.get(self.api_url + self.bus_eta + '/' + self.bus_route_stop + '/' + str(route_id) + '/' + str(stop_id)).json()


