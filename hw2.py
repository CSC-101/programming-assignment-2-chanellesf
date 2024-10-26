from typing import Optional

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
    return a.minutes < b.minutes or (a.minutes <= b.minutes and a.seconds < b.seconds)

# Part 3
# Returns a list of songs shorter than a given Duration
# INPUT: list[Song] to be parsed through, Duration object used to compare
# OUTPUT: list[Song] that contains Song objects less than the given Duration object
def song_shorter_than(songs : list[data.Song], time : data.Duration):
    return [song for song in songs if shorter_duration_than(song.duration, time)]

# Part 4
# Calculates the running time of a given list of songs
# INPUT: list of Songs objects, list of integers corresponding with the Song list
# OUTPUT: duration of the songs
def running_time(songs : list[data.Song], positions: list[int]) -> data.Duration:
    playlist = [songs[pos] for pos in positions]
    seconds = sum([song.duration.seconds for song in playlist])
    minutes = sum([song.duration.minutes for song in playlist]) + seconds // 60
    seconds = seconds % 60
    return data.Duration(minutes, seconds)

# Part 5
# Determines if a route is valid based on list of city routes
# INPUT: list of city links of type list[list[str]]
# INPUT: list[str] representing a list of city names showing a route
# OUTPUT: bool if the route is valid
def validate_route(city_links : list[list[str]], route : list[str]) -> bool:
    if len(route) == 0: return True
    for i in range(len(route)-1):
        city = route[i]
        correct_city_link_list = [city_link for city_link in city_links if city in city_link and route[i + 1] in city_link]
        if len(correct_city_link_list) == 0:
            return False
    return True

# Part 6
# Returns the index with the highest value at index 0
# INPUT: list[list[int]] representing the list to be parsed through
# OUTPUT: int representing the index of the list with the largest first element
def largest_first_element(nums : list[[int]]) -> int:
    largest = 0
    for i in range(len(nums)):
        if(nums[largest][0] < nums[i][0]):
            largest = i
    return largest

# Returns the index at which the longest contiguous repetition begins, or None
# INPUT: list of type integers to be parsed through
# OUTPUT: integer representing the index at which the largest contiguous repetition begins,
#         or None if there is no repetition
def longest_repetition(nums : list[int]) -> Optional[int]:
    if (len(nums) == 0 or nums == []): return None
    count = 1
    index = 0
    repetitions = []
    for i in range(len(nums) - 1):
        if(nums[i] == nums[i+1]):
            count += 1
        else:
            repetitions.append([count,index])
            count = 1
            index = i + 1
    return repetitions[largest_first_element(repetitions)][1]
