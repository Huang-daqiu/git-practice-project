def list_topics():
    return [
        "working tree",
        "staging area",
        "local repository",
        "remote repository",
        "git init",
        "git add",
    ]


def print_topics():
    for index, topic in enumerate(list_topics(), start=1):
        print(f"{index}. {topic}")


if __name__ == "__main__":
    print_topics()

