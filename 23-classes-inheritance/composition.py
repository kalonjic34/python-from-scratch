class Paper():
    def __init__(self,text, case):
        self.text = text
        self.case = case
        
class Briefcase():
    def __init__(self,price):
        self.price = price
        self.papers = []
        
    def add_paper(self,paper):
        self.papers.append(paper)
        
    def view_notes(self):
        return [paper.text for paper in self.papers]
    
class Lawyer():
    def __init__(self,name, briefcase):
        self.name = name
        self.briefcase = briefcase
        
    def write_note(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)
        
    def view_notes(self):
        print(self.briefcase.view_notes())
        
cheap_briefcase = Briefcase(price=19.99)
vinny= Lawyer(name= "Vincent",briefcase= cheap_briefcase)

vinny.write_note("My client is innocent", "AS-2ZK1")
vinny.write_note("There is no evidence of a crime!", "AS-2ZK1")
vinny.write_notes()