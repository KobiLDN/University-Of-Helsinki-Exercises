# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    with open(filename) as file:
        station_dict = {}
        for station in file:
            station = station.replace("\n", "")
            parts = station.split(";")
            if parts[0] == "Longitude":
                continue
            station_dict[parts[3]] = (float(parts[0]), float(parts[1]))
    return station_dict

def distance(stations: dict, station1: str, station2: str):
   long1, lat1 = stations[station1]
   long2, lat2 = stations[station2]
   x_km = (long1 - long2) * 55.26
   y_km = (lat1 - lat2) * 111.2
   return math.sqrt(x_km**2 + y_km**2)

def greatest_distance(stations: dict):
    # calculate distance between first station and the rest and store it
    # calculate distance of next station and the rest and match it with stored value
    # if the new value is greater this becomes the stored value
    #dict[key] = value
    #print(stations)
    station1 = ""
    station2 = ""
    stat1ofgradis = ""
    stat2ofgradis = ""
    greatest_distance = 0.0

    for location in stations:
        #print(location,"first i")
        station1 = location
        for location2 in stations:
            station2 = location2
            #print(location2, "second i")
            distance1 = distance(stations, station1, station2)
            if distance1 > greatest_distance:
                greatest_distance = distance1
                stat1ofgradis = station1
                stat2ofgradis = station2
    return (stat1ofgradis, stat2ofgradis, greatest_distance)


if __name__ == "__main__":
    program = True
    if program:
        filename = input("bike info: ")
    else:
        # now this is the False branch, and is never executed
        filename = "stations1.csv"
    stations = get_station_data(filename)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)