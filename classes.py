import datetime

class LogMixIn:
    def log(self, message):
        print(f'[Log] {datetime.datetime.now()}: {message}')


class Shipment(LogMixIn):
    id = 1

    def get(self):
        return self.id
    
shipment = Shipment()
shipment.log('Log Message')

id = 2

print(shipment.get())