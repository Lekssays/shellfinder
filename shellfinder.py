import requests

websites = []
endpoints = []

print("""
   _____ __         ___________           __         
  / ___// /_  ___  / / / ____(_)___  ____/ /__  _____
  \__ \/ __ \/ _ \/ / / /_  / / __ \/ __  / _ \/ ___/
 ___/ / / / /  __/ / / __/ / / / / / /_/ /  __/ /    
/____/_/ /_/\___/_/_/_/   /_/_/ /_/\__,_/\___/_/     
                                                     
	""")
print("Shell Finder v0.0.1 by Ahmed Lekssays (0x70776e)\n\n")
print("[*] INFO: Websites should start with 'http://' or 'https://' and should not end with '/'")

print("[*] INFO: Loading websites...")
websites = [website.rstrip('\n') for website in open('websites.txt')]

print("[*] INFO: Loading endpoints...")
endpoints = [endpoint.rstrip('\n') for endpoint in open('endpoints.txt')]

print("[*] INFO: Searching...")
try:
	for website in websites:
		print("[*] INFO: Target: " + website)
		for endpoint in endpoints:
			url = website + "/" + endpoint
			res = requests.get(url)
			if(res.status_code == 200):
				print("[+] SUCCESS: Shell found at: " + url)
except:
	print("[-] ERROR")
