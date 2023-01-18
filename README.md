# entity

A mass repository cloner for various git repository services.

# What sites are supported?

Currently it's only GitHub, however I plan to soon add Gitlab and Gitea too.

# How do I use it?

```
usage: main.py [-h] git_user

Mass clones all of the repositories for a given user or
organisation.

Cloned repos are stored in a folder, `git_user`, in the current working
directory.

Currently supported sites are:
    - GitHub.

positional arguments:
  git_user    The username of the person or organisation you're
              interested in.

options:
  -h, --help  show this help message and exit
```

# To-do:

- Add support for sites
    - Gitea
    - Gitlab
    - Sourcehut?
- Add argument for specifying custom folder path
- Add argument for custom `git clone` commands
    - Will need to read more into them though
- Make `pyproject.toml` file
- Possible `config.py` file
    - Since some instances of services may require auth? Not sure.
    - `RATE_LIMIT` variable
    - `MAX_REPOS` variable
- Add pagination logic for GitHub, since the API doesn't return everything
in one chunk
