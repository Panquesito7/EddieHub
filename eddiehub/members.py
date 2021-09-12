import requests


def member(username):
    details = requests.get(
        f"https://raw.githubusercontent.com/EddieHubCommunity/LinkFree/main/public/data/{username}.json"
    ).json()
    return details
