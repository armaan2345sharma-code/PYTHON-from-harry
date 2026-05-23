'''
Pascal case 
EmplyeeName -->PascalCase
Camel case
isNumeric--> camelCase
'''
class RailwayForm:
    formType="Railway Form"
    def printData(self):
        print (f"Name is{self.name}")
        print(f"Train is{self.train}")

harrysApplication=RailwayForm()
harrysApplication.name="Harry"
harrysApplication.train="Rajdhani express"
harrysApplication.printData()
