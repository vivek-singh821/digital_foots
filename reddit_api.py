import requests

def get_reddit_data(username):

    url = f"https://www.reddit.com/user/{username}/about.json"

    headers = {
        "User-Agent": "DigitalFootprintBot/1.0"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return None

        json_data = response.json()

        if "data" not in json_data:
            return None

        data = json_data["data"]

        return {
            "name": data.get("name"),
            "karma": data.get("total_karma", 0),
            "icon": data.get("icon_img", "")
        }

    except:

        return None