from lib.estimate_reading import *

def test_estimate_reading_time():
    result1 = estimate_reading_time("Today we have a lot of programming languages that can realize our needs, but the most important question is how to teach programming to beginner students. In this paper we suggest using Python for this purpose, because it is a programming language that has neatly organized syntax and powerful tools to solve any task. Moreover it is very close to simple math thinking. Python is chosen as a primary programming language for freshmen in most of leading universities. Writing code in python is easy. In this paper we give some examples of program codes written in Java, C++ and Python")
    assert result1 == .5