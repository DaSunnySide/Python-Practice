from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")


class PythonProjects():
    def __init__(self, msg):
        self.msg = msg
        self.print_message()

        util = Utilities()
        util.print_msg_with_time(msg)

    def print_message(self):
        print(self.msg)


class Utilities():
    def print_msg_with_time(selfself, msg):
        print(msg + ' @ ' + today)


if __name__ == '__main__':
    inst = PythonProjects("a message")

