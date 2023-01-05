from devices import Firewall
from devices import Switch
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a switch instance
switch27 = Switch ("switch27")
# Configure it
switch27.configure_switch()
# Create a switch instance
switch28 = Switch("switch28")
# Verify a CRC
switch28.calculate_crc("dummy data")

