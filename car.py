class Car(object):
    def __init__(self, color, model, company, speedLimit):
        self.color = color
        self.model = model
        self.company = company
        self.speedLimit = speedLimit
    def start(self):
        print ('Started')
    def stop(self):
        print('Stopped')
    def accelarate(self):
        print('Accelarating')

Audi = Car("red", 3, "Audi", 150)

print (Audi.color)
print (Audi.start())
