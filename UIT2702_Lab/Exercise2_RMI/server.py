# Run order:
#   1) python -m Pyro4.naming        (start the name server, keep it running)
#   2) python server.py              (in a second terminal)
#   3) python client.py              (in a third terminal)
import Pyro4
from calc import Calculator

daemon = Pyro4.Daemon()
calc_uri = daemon.register(Calculator)

# Use a name server to regsiter for a namespace.
name_server = Pyro4.locateNS()
name_server.register("ex2.calculator", calc_uri)

print(f"<SERVER> Calculator for RMI Accessible via 'ex2.calculator' or {calc_uri}")

daemon.requestLoop()
