
import math


# 1. Calculate distance using Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):

    # Convert degrees into radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Difference between coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    # Earth's radius in kilometres
    earth_radius = 6371

    distance = earth_radius * c

    return distance


# 2. Calculate bearing
def calculate_bearing(lat1, lon1, lat2, lon2):

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    dlon = math.radians(lon2 - lon1)

    x = math.sin(dlon) * math.cos(lat2)

    y = (
        math.cos(lat1) * math.sin(lat2)
        - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    )

    bearing = math.degrees(math.atan2(x, y))

    # Convert into 0 to 360 degrees
    bearing = (bearing + 360) % 360

    return bearing


# 3. Convert bearing into compass direction
def compass_direction(bearing):

    directions = [
        "North",
        "North-East",
        "East",
        "South-East",
        "South",
        "South-West",
        "West",
        "North-West"
    ]

    index = round(bearing / 45) % 8

    return directions[index]


# 4. Estimate walking time
def walking_time(distance, speed=4.5):

    time_minutes = (distance / speed) * 60

    return time_minutes
