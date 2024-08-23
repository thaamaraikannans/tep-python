from os import environ, mkdir, walk


def demo_func():
    data = environ["GOPATH"]
    print(data)
    mkdir("F:/IMS/tep-devops/kannan")
    # root_dir = "F:/IMS/tep-devops"
    # for root, dirs, files in walk(root_dir):
    #     print(f"Directory: {root}")
    #     for filename in files:
    #         print(f"- {filename}")

demo_func()

