# all-in-one-information-gathering-tool

give permission to files 
# chmod +x setup.sh
# chmod +x help.sh
# chmod +x allrecon6.py

Now  Swith to Super/Root user ( sudo su) 
run the command  ./allrecon6.py 
give domain/IP and choose selective number to perform scan 





# All-in-One Information Gathering Tool

## Description
This is an all-in-one automated information-gathering tool for reconnaissance and penetration testing. It integrates multiple scanning tools into a single script, allowing users to select a scan type from a menu and execute it automatically. The results are stored in organized folders for easy access.

## Features
- Whois Lookup
- Subdomain Enumeration (Assetfinder)
- Email & Domain OSINT (FinalRecon)
- Port Scan (Nmap)
- Website Recon (WhatWeb)
- DNS Enumeration (Dnsenum)
- Reverse IP Lookup
- SQL Injection Testing (SQLMap)
- DNS Server Info (Nslookup)
- Robots.txt Checking
- OS Detection
- Full Scan (Executes all available scans)
- Saves results in structured directories
- Uses `colorama` for enhanced terminal output

## Installation
Ensure you have the required dependencies installed before running the tool.

### Prerequisites
Install the following tools if they are not already available on your system:
```bash
sudo apt update && sudo apt install -y whois nmap dnsenum sqlmap assetfinder curl
pip install colorama
```

Additionally, install `FinalRecon`:
```bash
git clone https://github.com/thewhiteh4t/FinalRecon.git
cd FinalRecon
pip install -r requirements.txt
python3 setup.py install
```

## Usage
Run the script with:
```bash
python3 scanner.py
```
Or specify a target directly:
```bash
python3 scanner.py example.com
```

## Output
The scan results are saved in the `ScanResults` directory, with a separate folder created for each scan target, timestamped for reference.

## Screenshots
(Include relevant screenshots of the tool in action, if possible)

## License
This project is licensed under the MIT License.

## Disclaimer
This tool is intended for educational and ethical penetration testing purposes only. Unauthorized use against targets without permission is strictly prohibited.

