def list_topics():
    return [
        "working tree",
        "staging area",
        "local repository",
        "remote repository",
        "git init",
        "git add",
    ]

def show_progress():
    return "Git branch workflow completed"

def print_topics():
    for index, topic in enumerate(list_topics(), start=1):
        print(f"{index}. {topic}")

def print_my_name():
    print("My name is John Doe.")

if __name__ == "__main__":
    print_topics()
    print_my_name()
    print("hi")

