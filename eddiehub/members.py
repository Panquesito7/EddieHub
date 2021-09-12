import requests


def member(username):
    try:
        details = requests.get(
            f"https://raw.githubusercontent.com/EddieHubCommunity/LinkFree/main/public/data/{username}.json"
        ).json()
    except:
        orgs = requests.get(f"https://api.github.com/users/{username}/orgs").json()
        joined = False
        for org in orgs:
            if "EddieHubCommunity" in org["login"]:
                joined = True
        if not joined:
            error = "User not join EddieHub. Please join on https://github.com/EddieHubCommunity " \
            "if already joined change visibility to public."
        else:
            error = "User not found, Add data in https://github.com/EddieHubCommunity/LinkFree"
        details = {
            "error": error
        }
    return details


def members():
    results = requests.get(
        "https://api.github.com/orgs/EddieHubCommunity/members"
    ).json()
    return results
