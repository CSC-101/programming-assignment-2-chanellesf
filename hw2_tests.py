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
        expected = False
        self.assertEqual(actual, expected)

    def test_shorter_than_2(self):
        a = data.Duration(5,4)
        b = data.Duration(3,10)
        actual = hw2.shorter_duration_than(a,b)
        expected = True
        self.assertEqual(actual, expected)

    # Part 3
    def test_song_shorter_than_1(self):
        songs = [data.Song("Megan Thee Stallion","Cobra")]
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


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
