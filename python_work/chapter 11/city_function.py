def get_city_country(city, country, population = 0):
    """Format city and country name"""
    if population:
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()