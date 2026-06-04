class animals:
    animal="mamels"
class pets(animals):
    pets="dogs" 
class dogs(pets):
    @staticmethod
    def bark():
        print("bow bow")
d=dogs()
d.bark()