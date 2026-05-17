import requests


def get_github_data(username):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    user = response.json()

    repo_response = requests.get(user["repos_url"])

    repos = repo_response.json()

    languages = []

    total_stars = 0

    top_repo = None

    max_stars = -1

    for repo in repos:

        if repo["language"]:
            languages.append(repo["language"])

        total_stars += repo["stargazers_count"]

        if repo["stargazers_count"] > max_stars:

            max_stars = repo["stargazers_count"]

            top_repo = repo

    followers = user["followers"]

    repo_count = user["public_repos"]

    if followers > 1000 or total_stars > 500:

        level = "Advanced Developer"

    elif followers > 100 or repo_count > 30:

        level = "Intermediate Developer"

    else:

        level = "Beginner Developer"

    return {
        "profile": user,
        "repos": repos[:6],
        "languages": list(set(languages)),
        "total_stars": total_stars,
        "top_repo": top_repo,
        "developer_level": level
    }