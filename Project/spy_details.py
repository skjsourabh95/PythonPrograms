#a class to hold spy details
class Spy:
    name = "Sourabh Kumar Janghel"
    salutation = "Mr"
    age = 22
    rating = 4.0
    status = True
    chats = []
    current_status_message = None

    # method to set values to a spy
    def setSpy(self,name,salutation,age,rating,status):
        self.name = name
        self.salutation =salutation
        self.age = age
        self.rating = rating
        self.status = True

    #getter methods
    def getName(self):
        return self.name
    def getSalutation(self):
        return self.salutation
    def getage(self):
        return self.age
    def getrating(self):
       return self.rating
    def getstatus(self):
        return self.status

