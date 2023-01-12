import pathlib
import subprocess

from typing import List, Tuple
from os import environ


# Strings for text colouring
CLR_RED = "\033[91m"
CLR_YLW = "\033[93m"
CLR_GRN = '\033[92m'
CLR_STD = "\033[0m"


def create_path(git_user: str) -> None:
    """
    Makes a folder in the current folder for a given `git_user`.

    Args:
        git_user (str): The name of an user or organisation.
    """
    pathlib.Path(f"{git_user}").mkdir(exist_ok=True)


def clone_repos(git_user: str, repos: List[Tuple[str, str]]) -> None:
    """
    Clones every repository found in the `repos` list into the `git_user`
    folder.

    If an error occurs the output is displayed to the user, no exception is
    raised however.

    Args:
        git_user (str): The name of an user or organisation.
        repos (List[Tuple[str, str]]): A list of tuples, with each tuple
            containing both the full repository name i.e
            `owner_name/repo_name`, and the git clone URL.
    """
    for repo in repos:
        full_repo_name, clone_url = repo
        print(f"Trying to clone {full_repo_name}")

        command = ["git", "-C", f"{git_user}", "clone", f"{clone_url}"]

        env = environ.copy()
        env["GIT_TERMINAL_PROMPT"] = "0"

        try:
            subprocess.run(command, check=True, capture_output=True, env=env)
        except subprocess.CalledProcessError as e:
            error_message = f'{CLR_YLW}{e.stderr.decode("utf-8")}{CLR_STD}'
            print(f"{CLR_RED}Error{CLR_STD}:\n{error_message}")
        else:
            print(f"{CLR_GRN}Successfully cloned {full_repo_name}{CLR_STD}\n")


def main():
    pass


if __name__ == "__main__":
    main()
