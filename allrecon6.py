#!/usr/bin/env python3
import os
import subprocess
import sys
import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Base directory to store scan results
RESULTS_DIR = "ScanResults"

def banner():
    print(Fore.CYAN + """
     █████╗ ██╗     ██╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
    ██╔══██╗██║     ██║██╔══██╗██╔════╝██╔════╝ ██╔══██╗████╗  ██║
    ███████║██║     ██║██████╔╝█████╗  ██║  ███╗██████╔╝██╔██╗ ██║
    ██╔══██║██║     ██║██╔══██╗██╔══╝  ██║   ██║██╔═══╝ ██║╚██╗██║
    ██║  ██║███████╗██║██║  ██║███████╗╚██████╔╝██║     ██║ ╚████║
    ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═══╝

             All-in-One Information Gathering Tool
    """ + Style.RESET_ALL)

def create_target_dir(target):
    """Creates a directory for the target with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    target_dir = os.path.join(RESULTS_DIR, f"{target}_{timestamp}")
    os.makedirs(target_dir, exist_ok=True)
    return target_dir

def run_command(command, outfile, timeout=600):  # Increased timeout to 10 minutes
    """Runs a shell command, prints its output, and writes it to outfile."""
    print(f"\nRunning: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout)
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = "Command timed out."
    print(output)
    with open(outfile, "w") as f:
        f.write(output)
    print(f"Output saved to: {outfile}\n")

def whois_lookup(target, target_dir):
    outfile = os.path.join(target_dir, "whois.txt")
    run_command(f"whois {target}", outfile)

def subdomain_enumeration(target, target_dir):
    outfile = os.path.join(target_dir, "subdomains.txt")
    run_command(f"assetfinder --subs-only {target}", outfile)

def finalrecon_scan(target, target_dir):
    outfile = os.path.join(target_dir, "finalrecon.txt")
    run_command(f"finalrecon --url https://{target}/ --headers --sslinfo --whois --ps", outfile)

def nmap_scan(target, target_dir):
    outfile = os.path.join(target_dir, "nmap.txt")
    run_command(f"nmap -A {target}", outfile)

def website_recon(target, target_dir):
    outfile = os.path.join(target_dir, "whatweb.txt")
    run_command(f"whatweb {target}", outfile)

def dns_enumeration(target, target_dir):
    outfile = os.path.join(target_dir, "dnsenum.txt")
    run_command(f"dnsenum {target}", outfile)

def reverse_ip_lookup(target, target_dir):
    outfile = os.path.join(target_dir, "reverse_ip.txt")
    run_command(f"host {target}", outfile)

def sqlmap_scan(target, target_dir):
    outfile = os.path.join(target_dir, "sqlmap.txt")
    run_command(f"sqlmap -u {target} --batch", outfile)

def nslookup_scan(target, target_dir):
    outfile = os.path.join(target_dir, "nslookup.txt")
    run_command(f"nslookup {target}", outfile)

def robots_txt_check(target, target_dir):
    outfile = os.path.join(target_dir, "robots.txt")
    run_command(f"curl -s {target}/robots.txt", outfile)

def os_detection(target, target_dir):
    outfile = os.path.join(target_dir, "os_detection.txt")
    run_command(f"nmap -O {target}", outfile)

def display_menu():
    print(Fore.YELLOW + "\nSelect Scan Type:")
    print(Fore.BLUE + "1. Whois Lookup")
    print(Fore.BLUE + "2. Subdomain Enumeration (assetfinder)")
    print(Fore.BLUE + "3. Email & Domain OSINT (finalrecon)")
    print(Fore.BLUE + "4. Port Scan (nmap)")
    print(Fore.BLUE + "5. Website Recon (whatweb)")
    print(Fore.BLUE + "6. DNS Enumeration (dnsenum)")
    print(Fore.BLUE + "7. Reverse IP Lookup")
    print(Fore.BLUE + "8. XSS/SQL Injection Testing (sqlmap)")
    print(Fore.BLUE + "9. DNS Server Info (Nslookup)")
    print(Fore.BLUE + "10. Robots.txt Checking")
    print(Fore.BLUE + "11. OS Detection")
    print(Fore.BLUE + "12. Full Scan (All)")
    print(Fore.BLUE + "13. Exit")

def run_full_scan(target, target_dir):
    whois_lookup(target, target_dir)
    subdomain_enumeration(target, target_dir)
    finalrecon_scan(target, target_dir)
    nmap_scan(target, target_dir)
    website_recon(target, target_dir)
    #dns_enumeration(target, target_dir)
    reverse_ip_lookup(target, target_dir)
    sqlmap_scan(target, target_dir)
    nslookup_scan(target, target_dir)
    robots_txt_check(target, target_dir)
    os_detection(target, target_dir)

def main():
    banner()
    if len(sys.argv) < 2:
        target = input("Enter target domain or IP: ").strip()
    else:
        target = sys.argv[1].strip()

    target_dir = create_target_dir(target)
    print(f"Results will be stored in: {target_dir}")

    while True:
        display_menu()
        choice = input(Fore.CYAN + "\nEnter your choice: ")

        if choice == "1":
            whois_lookup(target, target_dir)
        elif choice == "2":
            subdomain_enumeration(target, target_dir)
        elif choice == "3":
            finalrecon_scan(target, target_dir)
        elif choice == "4":
            nmap_scan(target, target_dir)
        elif choice == "5":
            website_recon(target, target_dir)
        elif choice == "6":
            dns_enumeration(target, target_dir)
        elif choice == "7":
            reverse_ip_lookup(target, target_dir)
        elif choice == "8":
            sqlmap_scan(target, target_dir)
        elif choice == "9":
            nslookup_scan(target, target_dir)
        elif choice == "10":
            robots_txt_check(target, target_dir)
        elif choice == "11":
            os_detection(target, target_dir)
        elif choice == "12":
            run_full_scan(target, target_dir)
        elif choice == "13":
            print(Fore.RED + "\n[!] Exiting...")
            sys.exit(0)
        else:
            print(Fore.RED + "\n[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
