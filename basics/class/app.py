class computer:
    def devices(self):
        print("the domain is ", self.domain, "and dept is " , self.dept)
    
    
    
    def __init__(self, domain , dept):
        self.domain = domain
        self.dept = dept
        print("object initiated")


kannan = computer("AWS", "IMS")
aravinth = computer("Network", "IMS")

kannan.devices()
aravinth.devices()

