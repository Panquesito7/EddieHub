import requests


def member(username):
    try:
        details = requests.get(
            f"https://raw.githubusercontent.com/EddieHubCommunity/LinkFree/main/public/data/{username}.json"
        ).json()
    except:
        details = {
            "error": "User not found, Add data in https://github.com/EddieHubCommunity/LinkFree"
        }
    return details
