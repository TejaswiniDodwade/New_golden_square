class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
    def format(self):
        print("printing self title")
        print(self.title)
        return f'{self.title} : {self.contents}'
    def count_words(self):
       total_words = len(self.contents.split())
       print("printing total words 1")
       print(total_words)
       return total_words
    def reading_time(self, wpm):
       total_words = len(self.contents.split()) 
       total_time = total_words / wpm
       return total_time
    def reading_chunk(self, wpm, minutes):
       split_list = self.contents.split()
       count_of_words = wpm * minutes
       reading_chunk = " ".join(split_list[0:count_of_words])
       return reading_chunk
    
diary_entry = DiaryEntry("My Title" ,"Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.") 
diary_entry.format()
diary_entry.count_words()
print(diary_entry.reading_time(1))
print(diary_entry.reading_chunk(10,2))