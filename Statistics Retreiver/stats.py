import requests

url = "https://www.crazygames.com/game/downtown-1930s-mafia"
headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_data():
    response = requests.get(url, headers=headers)

    string = response.text

    idx1 = string.find("ratingCount") + len("ratingCount:") + 1
    idx2 = string.find("upvotes") + len("upvotes:") + 1
    idx3 = string.find("downvotes") + len("downvotes:") + 1

    ratingCount = ""
    upvotes = ""
    downvotes = ""

    while string[idx1] != "}":
        ratingCount += string[idx1]
        idx1 += 1

    while string[idx2] != ",":
        upvotes += string[idx2]
        idx2 += 1

    while string[idx3] != ",":
        downvotes += string[idx3]
        idx3 += 1

    return [ratingCount, upvotes, downvotes]