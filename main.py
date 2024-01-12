import requests
from bs4 import BeautifulSoup
import re 
from colorama import Fore, Style

# First request to get FU value
url1 = input(Fore.YELLOW + "Enter mlwbd movie url: " + Style.RESET_ALL) 

response1 = requests.get(url1)

if response1.status_code == 200:
    # Parse the HTML content
    soup1 = BeautifulSoup(response1.text, 'html.parser')

    # Find the input element with name="FU" and get its value
    fu_value = soup1.find('input', {'name': 'FU'}).get('value')

    # Second request
    url2 = "https://freethemesy.com/career-guide-software-development-for-your-bright-future"
    payload = {
        "FU4": fu_value
    }

    headers = {
        "authority": "freethemesy.com",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://freethemesy.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response2 = requests.post(url2, data=payload, headers=headers)

    match = re.search(r'window\.location\.href\s*=\s*"([^"]+)"', response2.text)

    if match:
        href_value = match.group(1)

        # Third POST request to namemeaningbengali.com
        third_url = "https://namemeaningbengali.com/new/l/api/m"
        third_payload = {
            "s": href_value
        }

        third_headers = {
            "authority": "namemeaningbengali.com",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://namemeaningbengali.com",
            "x-requested-with": "XMLHttpRequest"
        }

        third_response = requests.post(third_url, data=third_payload, headers=third_headers)

        # Print the third response
        print(Fore.GREEN + "Direct Download Link:", third_response.text + Style.RESET_ALL)
    else:
        print("Download token not found, need to rebuilt probably ; not hehe")
else:
    print(f'Failed to retrieve the first page. Status code: {response1.status_code}')

input(Fore.CYAN + "Enter any key to exit" + Style.RESET_ALL)
