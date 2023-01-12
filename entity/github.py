import requests
from time import sleep
from typing import List, Tuple


BASE = "https://api.github.com"


def get_repos(git_user: str) -> List[Tuple[str, str]]:
    """
    Obtains the full repository name and git clone URLs for every repository
    under a given `git_user`.

    The information is returned as a list of tuples, with each tuple composing
    of the information mentioned above.

    Args:
        git_user (str): Can be either a GitHub username or organisation name.
    """
    query = requests.get(f"{BASE}/users/{git_user}/repos")

    sleep(1)

    if query.ok:
        query = query.json()
        return [(repo["full_name"], repo["clone_url"]) for repo in query]
    else:
        raise requests.HTTPError(f"{query.status_code} - Invalid `git_user`")


def main():
    pass


if __name__ == "__main__":
    main()
