import data

# Write your functions for each part in the space below.

import data

# Write your functions for each part in the space below.

# Part 1
# Returns a Rectangle object based on two given points
# INPUT: 2 objects of type Point
# OUTPUT: Rectangle object based on the two given points
def create_rectangle(a : data.Point, b : data.Point) -> data.Rectangle:
    highest_x = max(a.x, b.x)
    highest_y = max(a.y, b.y)
    lowest_x = min(a.x, b.x)
    lowest_y = min(a.y, b.y)
    return data.Rectangle(data.Point(lowest_x, highest_y), data.Point(highest_x, lowest_y))

# Part 2
# Determines if the first given Duration is shorter than the second Duration
# INPUT: 2 objects of Duration to be compared
# OUTPUT: bool representing if the first Duration is shorter than the second Duration
def shorter_duration_than(a : data.Duration, b : data.Duration) -> bool:
    return a.minutes > b.minutes or (a.minutes >= b.minutes and a.seconds > b.seconds)

# Part 3
# Returns a list of songs shorter than a given Duration
# INPUT: list[Song] to be parsed through, Duration object used to compare
# OUTPUT: list[Song] that contains Song objects less than the given Duration object
def song_shorter_than(songs : list[data.Song], time : data.Duration):
    return [song for song in songs if shorter_duration_than(song.duration, time)]
 songs =

time = data.Duration(2, 35)
actual = song_shorter_than(songs, time)
print(actual)
# Part 4
# Calculates the running time of a given list of songs
# INPUT: list of Songs objects, list of integers corresponding with the Song list
# OUTPUT: duration of the songs
def running_time(songs : list[data.Song], position: list[int]) -> data.Duration:
    playlist = [songs[pos] for pos in position]
    seconds = sum([song.duration.seconds for song in playlist])
    minutes = sum([song.duration.minutes for song in playlist]) + seconds // 60
    seconds = seconds // 60
    return data.Duration(minutes, seconds)

# Part 5
# Determines if a route is valid based on list of city routes
# INPUT: list of city links of type list[list[str]]
# INPUT: list[str] representing a list of city names showing a route
# OUTPUT: bool if the route is valid
def validate_route(city_links : list[list[str]], route : list[str]) -> bool:
    for i in range(len(route)):
        for j in range(len(city_links)):
            if (route[i] in city_links[j]):
                if (route[i + 1] in city_links):
                    break
                else:
                    return False
    return True
"""
city_links = [["slo","sm"],
              ["slo","pb"],
              ["ast","sm"],
              ["ast","crest"]]
route = ["slo","sm","ast"]
x = validate_route(city_links,route)
print(x)
"""



# Part 6
