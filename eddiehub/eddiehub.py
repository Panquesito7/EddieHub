import requests


def eddiehub():
    details = requests.get(
        "https://api.github.com/orgs/EddieHubCommunity"
    ).json()
    return details
