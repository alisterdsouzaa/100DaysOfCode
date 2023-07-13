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


def add_new_country(country_visited, total_visit, cities_visited):
    new_country = {"country": country_visited, "visits": total_visit, "cities": cities_visited}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "saint Peter"])
print(travel_log)
