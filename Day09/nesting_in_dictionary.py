# Nesting

capitals = {
    "France": "Paris",
    "India": "Delhi",
    "Japan": "Tokyo"
}

# Nesting list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg"]
}

# Nesting dictionary in a list

travel_log = [
    {
        "country": "India",
        "cities_visited": ["Pune", "Mumbai", "Bengaluru"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visit": 5
    }
]

print(travel_log)