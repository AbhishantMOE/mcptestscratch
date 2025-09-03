from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/myapi")
def hit_api():
    api_url = "https://intercom-api-gateway.moengage.com/v2/iw/check-deeplink"
    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJpbnRlcmNvbSIsImNoYW5uZWwiOiJhcGkiLCJpYXQiOjE3NTY4MDA0NzcsImV4cCI6MTc1Njg4Njg3N30.6cEK6N8TXzoOlCm-phlYEgKbq8vofqZ7x6uoBjeznOg"

    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        "db_name": "NDTVProfit",
        "user_id": "eb50c9bb-fac4-44c7-b97d-36ab374c5ef8",
        "campaign_id": "68b2cd88c85096a0c1603cf0",
        "date": "2025-08-30",
        "region":"DC1"
    }

    try:
        # 4. Make the POST request with the URL, headers, and json payload
        response = requests.post(api_url, headers=headers, json=payload)
        
        # 5. Handle potential HTTP errors
        response.raise_for_status()

        # 6. Process the response from the third-party API
        api_response_data = response.json()

        print(api_response_data.get('status'))

        return api_response_data
        
        # return jsonify({
        #     "message": "Item created successfully!",
        #     "api_response": api_response_data
        # }), 200

    except requests.exceptions.HTTPError as err:
        return jsonify({"error": f"API request failed: {err}"}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
    #return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)