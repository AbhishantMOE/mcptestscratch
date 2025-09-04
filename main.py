from fastmcp import FastMCP
import requests
from typing import Any

mcp = FastMCP(name="MoEngage API Client")

@mcp.tool()
def check_deeplink(
    db_name: str, 
    user_id: str, 
    campaign_id: str, 
    date: str, 
    region: str
) -> Any:
    """
    Fetches the result of the MoEngage check-deeplink API.

    Args:
        db_name: The database name, e.g., "NDTVProfit".
        user_id: The unique identifier for the user.
        campaign_id: The unique identifier for the campaign.
        date: The date for the request in YYYY-MM-DD format.
        region: The data center region, e.g., "DC1".
    """
    api_url = "https://intercom-api-gateway.moengage.com/v2/iw/check-deeplink"
    bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJpbnRlcmNvbSIsImNoYW5uZWwiOiJhcGkiLCJpYXQiOjE3NTY5NTM3NzgsImV4cCI6MTc1NzA0MDE3OH0.4vV-MBv4X4UGw1DBX8vsyYa5L91g5ycZqHtH7KoqW4k"  # Use a valid token

    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }

    # The payload is now dynamically created from the function arguments
    payload = {
        "db_name": db_name,
        "user_id": user_id,
        "campaign_id": campaign_id,
        "date": date,
        "region": region
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        api_response_data = response.json()
        return api_response_data
    except requests.exceptions.HTTPError as err:
        return {"error": f"API request failed: {err}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred: {e}"}

if __name__ == '__main__':
    mcp.run()