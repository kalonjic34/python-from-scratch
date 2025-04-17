class FilmMaker():
    def gice_interview(self):
        print("I love making movies")
        
class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts!")
        
# class JackOfAllTrades(Director,ScreenWriter):
class JackOfAllTrades(ScreenWriter,Director):
    pass

stallone = JackOfAllTrades()
stallone.gice_interview()

print(JackOfAllTrades.mro())