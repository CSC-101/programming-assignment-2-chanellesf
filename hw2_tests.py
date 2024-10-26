from unittest import expectedFailure

import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        a = data.Point(2,2)
        b = data.Point(10,10)
        actual = hw2.create_rectangle(a,b)
        expected = data.Rectangle(data.Point(2,10), data.Point(10,2))
        self.assertEqual(actual, expected)

    def test_create_rectangle_2(self):
        a = data.Point(2,2)
        b = data.Point(2,10)
        actual = hw2.create_rectangle(a,b)
        expected = data.Rectangle(data.Point(2,10), data.Point(2,2))
        self.assertEqual(actual,expected)

    # Part 2
    def test_shorter_duration_than_1(self):
        a = data.Duration(3,49)
        b = data.Duration(3,50)
        actual = hw2.shorter_duration_than(a,b)
        expected = True
        self.assertEqual(actual, expected)

    def test_shorter_than_2(self):
        a = data.Duration(5,4)
        b = data.Duration(3,10)
        actual = hw2.shorter_duration_than(a,b)
        expected = False
        self.assertEqual(actual, expected)

    # Part 3
    def test_song_shorter_than_1(self):
        songs =[data.Song("Megan Thee Stallion", "Cobra", data.Duration(2, 49)),
               data.Song("Megan Thee Stallion & Cardi B", "WAP",data.Duration(3, 7)),
               data.Song("Megan Thee Stallion (ft. Yuki Chiba)", "Mamushi",data.Duration(2, 37)),
               data.Song("Chappell Roan", "HOT TO GO!",data.Duration(3, 5)),
               data.Song("Mitski", "I Want You", data.Duration(3, 4)),
               data.Song("Mitski", "My Love Mine All Mine", data.Duration(2, 18))]
        time = data.Duration(2, 35)
        actual = hw2.song_shorter_than(songs, time)
        expected = [data.Song("Mitski", "My Love Mine All Mine", data.Duration(2, 18))]
        self.assertEqual(actual, expected)

    def test_song_shorter_than_2(self):
        songs = [data.Song("Megan Thee Stallion","Cobra", data.Duration(2, 49)),
                 data.Song("Megan Thee Stallion & Cardi B","WAP", data.Duration(3,7)),
                 data.Song("Megan Thee Stallion (ft. Yuki Chiba)","Mamushi",data.Duration(2,37)),
                 data.Song("Chappell Roan","HOT TO GO!",data.Duration(3,5)),
                 data.Song("Mitski","I Want You",data.Duration(3,4)),
                 data.Song("Mitski","My Love Mine All Mine", data.Duration(2,18))
                ]
        time = data.Duration(3,0)
        actual = hw2.song_shorter_than(songs, time)
        expected = [data.Song("Megan Thee Stallion","Cobra", data.Duration(2, 49)),
                    data.Song("Megan Thee Stallion (ft. Yuki Chiba)","Mamushi",data.Duration(2,37)),
                    data.Song("Mitski","My Love Mine All Mine", data.Duration(2,18))]
        self.assertEqual(actual,expected)

    # Part 4
    def test_running_time_1(self):
        songs = [data.Song("Tame Impala","New Person, Same Mistakes",data.Duration(6,3)),
                 data.Song("Weezer","Buddy Holly",data.Duration(2,39)),
                 data.Song("Thundercat","Them Changes",data.Duration(3,8)),
                 data.Song("SZA","Kill Bill",data.Duration(2,34))]
        pos = [0,1,2,3,0]
        actual = hw2.running_time(songs,pos)
        expected = data.Duration(20,27)
        self.assertEqual(actual,expected)

    def test_running_time_2(self):
        songs = [data.Song("The Beatles","Girl",data.Duration(2,43)),
                 data.Song("Claude Debussy","The Girl with the Flaxen Hair",data.Duration(2,36)),
                 data.Song("Pipes And Drums Of The Royal Tank Regiment", "Amazing Grace",data.Duration(2,36)),
                 data.Song("Miles Davis","So What",data.Duration(9,5)),
                 data.Song("Led Zepplin","Black Dog",data.Duration(4,55))]
        pos = [4,2,3,0,1]
        actual = hw2.running_time(songs, pos)
        expected = data.Duration(21,55)
        self.assertEqual(actual,expected)

    # Part 5
    def test_validate_route_1(self):
        city_links = [["slo", "sm"],
                      ["slo", "pb"],
                      ["ast", "sm"],
                      ["ast", "crest"]]
        route = ["slo", "sm", "ast"]
        actual = hw2.validate_route(city_links, route)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_route_2(self):
        city_links = [["slo", "sm"],
                      ["slo", "pb"],
                      ["ast", "sm"],
                      ["ast", "crest"]]
        route = ["slo", "ast"]
        actual = hw2.validate_route(city_links, route)
        expected = False
        self.assertEqual(actual, expected)

    # Part 6
    def longest_repetition_1(self):
        nums = [1, 1, 2, 2, 1, 1, 1, 3]
        actual = longest_repetition(nums)
        expected = 4
        self.assertEqual(actual,expected)

    def longest_repetition_2(self):
        nums = [1,2,3,4,5]
        actual = longest_repetition(nums)
        expected = None
        self.assertEqual(actual,expected)

    def longest_repetition_3(self):
        nums = []
        actual = longest_repetition(nums)
        expected = None
        self.assertEqual(actual,expected)




if __name__ == '__main__':
    unittest.main()
