import argparse


description = """Mass clones all of the repositories for a given user or
organisation.

Cloned repos are stored in a folder, `git_user`, in the current working
directory.

Currently supported sites are:
    - GitHub."""

help_git_user = """The username of the person or organisation you're
interested in."""


def initialise_args() -> argparse.Namespace:
    """
    Initialises all of the needed arguments for the program.
    """
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("git_user", help=help_git_user)

    return parser.parse_args()


def main():
    pass


if __name__ == "__main__":
    main()
