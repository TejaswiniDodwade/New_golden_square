class GrammarStats:
    def __init__(self):
        self.text_check = 0
        self.check_pass = 0

        
    def check(self, text):
        self.text_check += 1 
        print("printing self.text")
        print(self.text_check)
        if text[0].isupper() and text[-1] in [".","!","?"]:
            self.check_pass += 1 
            print("=====================")
            print("printing check_pass")
            print(self.check_pass)
            return True
           
        else:
            return False
           
           
    def percentage_good(self):
        total_pass = (self.check_pass / self.text_check) * 100
        return total_pass
        

        
        
grammar_stats = GrammarStats()
print(grammar_stats.check("What is your name?"))
print(grammar_stats.check("What is your name"))
print(grammar_stats.check("What is your name?"))
print(grammar_stats.check("What is your name"))
print(grammar_stats.percentage_good())