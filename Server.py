import Pyro4
from Airport import Airport


daemon = Pyro4.Daemon()

url = "localhost"
user = "root"
password = "Password123"
airport = Airport(url, user, password)

uri = daemon.register(airport)
ns = Pyro4.locateNS()
ns.register('Airport', uri)

daemon.requestLoop()