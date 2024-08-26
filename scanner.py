import requests

def load_payloads(file_path):
    """Load payloads from a specified file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Payload file {file_path} not found.")
        return []

def scan_for_sql_injection(url):
    """Scan a URL for SQL Injection vulnerabilities using loaded payloads."""
    payloads = load_payloads('payloads/sql_injection.txt')
    print(f"Scanning {url} for SQL Injection vulnerabilities...")

    for payload in payloads:
        full_url = f"{url}{payload}"
        response = requests.get(full_url)
        if ("syntax error" in response.text or "mysql_fetch" in response.text or
            "You have an error in your SQL syntax" in response.text):
            print(f"[+] SQL Injection vulnerability found with payload: {payload}")
            return
    print("[-] No SQL Injection vulnerability found.")

def scan_for_xss(url):
    """Scan a URL for Cross-Site Scripting (XSS) vulnerabilities using loaded payloads."""
    payloads = load_payloads('payloads/xss.txt')
    print(f"Scanning {url} for XSS vulnerabilities...")

    for payload in payloads:
        full_url = f"{url}{payload}"
        response = requests.get(full_url)
        if payload in response.text:
            print(f"[+] XSS vulnerability found with payload: {payload}")
            return
    print("[-] No XSS vulnerability found.")

def scan_for_directory_traversal(url):
    """Scan a URL for Directory Traversal vulnerabilities using loaded payloads."""
    payloads = load_payloads('payloads/directory_traversal.txt')
    print(f"Scanning {url} for Directory Traversal vulnerabilities...")

    for payload in payloads:
        full_url = f"{url}{payload}"
        response = requests.get(full_url)
        if response.status_code == 200 and "root" in response.text:
            print(f"[+] Directory Traversal vulnerability found with payload: {payload}")
            return
    print("[-] No Directory Traversal vulnerability found.")

def main():
    target_url = input("Enter the target URL (e.g., http://example.com/index.php?param=): ")
    print("\nSelect scan type:")
    print("1. SQL Injection")
    print("2. XSS")
    print("3. Directory Traversal")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        scan_for_sql_injection(target_url)
    elif choice == '2':
        scan_for_xss(target_url)
    elif choice == '3':
        scan_for_directory_traversal(target_url)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
