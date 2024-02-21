from city_function import get_city_country

def test_city_countries():
    """Do city countries like Cape Town, South Africa"""
    formatted_name = get_city_country("cape town", "south africa")
    assert formatted_name == "Cape Town, South Africa"

def test_city_countries_population():
    """Do city countries population like Cape Town, South Africa, 35_000_000"""
    formatted_name = get_city_country("Cape Town", "South Africa", 62_000_000)
    assert formatted_name == "Cape Town, South Africa - Population 62000000"