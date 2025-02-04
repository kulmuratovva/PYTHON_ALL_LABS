class MyString:
    def getString(self):
        self.sentence = input("Enter a sentence: ")  

    def printString(self):
        print("Upper case:", self.sentence.upper())  


my_string = MyString()
my_string.getString()
my_string.printString()
