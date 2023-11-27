def city_country(city, country):
    print(f"{city.title()}, {country.title()}")


city_country("Cape Town", "South Africa")
city_country(city="Paris", country="France")
city_country(country="United States of America", city="Texas")

def make_album(artist, album_title, number_of_songs=None):
    if number_of_songs:
        album = { "artist": artist, "album_title": album_title, "number_of_songs": number_of_songs }
    else:
        album = { "artist": artist, "album_title": album_title }
    return album

print()
album1 = make_album("Adele", "23", 12)
album2 = make_album("Tupac", "All Eyez on Me", 18)
album3 = make_album(album_title="Confessions", artist="Usher")

print(album1)
print(album2)
print(album3)

while True:
    print("\nPlease enter the artists details: ")
    print("(Enter 'q' at anytime to quit)")

    artist = input("Artist name: ")
    if artist == "q":
        break

    album_name = input("Album title: ")
    if album_name == "q":
        break

    number_of_songs = input("Number of songs on album: ")
    if number_of_songs == "q":
        break

    artist_details = make_album(artist, album_name, number_of_songs)

    print(artist_details)