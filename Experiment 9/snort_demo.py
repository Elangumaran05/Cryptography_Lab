# Demonstration of Intrusion Detection System (IDS) Using Snort
# Simulation and execution commands for Snort on Windows

import subprocess
import sys

print("==================================================")
print("  Snort Intrusion Detection System (IDS) Demo")
print("==================================================")
print("1. Installation check: bin\\snort.exe -V")
print("2. Interface listing:  bin\\snort.exe -W")
print("3. Sniffer mode:       bin\\snort.exe -v -i 5")
print("4. Rule execution:     bin\\snort.exe -A console -q -i 5 -R rules\\local.rules")
print("--------------------------------------------------")
print("IDS Alert Trigger:")
print("Generating ICMP Ping traffic to 8.8.8.8...")
print()
print("[**] [1:1000001:1] ICMP Ping Detected [**]")
print("[**] [1:1000001:1] ICMP Ping Detected [**]")
print("[**] [1:1000001:1] ICMP Ping Detected [**]")
print("[**] [1:1000001:1] ICMP Ping Detected [**]")
print("==================================================")
