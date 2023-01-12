import args
import github
import clone


def main() -> None:
    arguments = vars(args.initialise_args())

    git_user = arguments["git_user"]

    repositories = github.get_repos(git_user)

    clone.create_path(git_user)
    clone.clone_repos(git_user, repositories)


if __name__ == "__main__":
    main()
