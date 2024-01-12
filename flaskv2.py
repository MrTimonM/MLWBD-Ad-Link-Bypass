from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import re 

app = Flask(__name__)

@app.route('/url=<path:url>', methods=['GET'])
def get_download_link(url):
    # Check if the URL contains "mlwbd"
    if "mlwbd" not in url:
        return jsonify({"error": "Go away Demon! Use only MLWBD link."})

    # first req
    response1 = requests.get(url)

    if response1.status_code == 200:
        # init soup
        soup1 = BeautifulSoup(response1.text, 'html.parser')

        # get FU
        fu_value = soup1.find('input', {'name': 'FU'}).get('value')

        # Second request
        second_url = "https://freethemesy.com/career-guide-software-development-for-your-bright-future"
        payload = {
            "FU4": fu_value
        }

        headers = {
            "authority": "freethemesy.com",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://freethemesy.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        response2 = requests.post(second_url, data=payload, headers=headers)

        match = re.search(r'window\.location\.href\s*=\s*"([^"]+)"', response2.text)

        if match:
            href_value = match.group(1)

            
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
            
            
            download_link = third_response.text

            
            return jsonify({"Download Link": download_link})
        else:
            return jsonify({"error": "Download Link token is not found"})
    else:
        return jsonify({"error": f"Check your url, demon. Status code: {response1.status_code}"})

if __name__ == '__main__':
    app.run(debug=True)
