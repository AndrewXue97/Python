#student id - 101004154
#student name - Andrew Xue

import paramiko
from datetime import datetime

class SSHClient:
    def __init__(self, hostname, username, password, port=22):

        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__port = port
        self.__client = None
        self.__shell = None
        self.__connect()

    def __connect(self):
        try:
            self.__client = paramiko.SSHClient()
            self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__client.connect(self.__hostname, username=self.__username, password=self.__password, port=self.__port)
            print("Successfully connected.")
        except paramiko.SSHException as e:
            print(f"Failed to connect: {e}")

    def start_shell(self):
        self.__shell = self.__client.invoke_shell()

    def send_command(self, command):
        if self.__shell is None:
            raise Exception("Shell not started. Use start_shell() to start it.")
        self.__shell.send(command + '\n')
        response = ""
        while True:
            if self.__shell.recv_ready():
                response += self.__shell.recv(20000).decode('utf-8')
            else:
                break
        return response

    def exec_command(self, command):
        stdin, stdout, stderr = self.__client.exec_command(command)
        output = stdout.read().decode('utf-8')
        return output

    def save_output(self, command, output):
        today = datetime.now()
        day = today.strftime("%d")
        month = today.strftime("%B")
        year = today.strftime("%Y")
        hour = today.strftime("%H")
        minutes = today.strftime("%M")

        file_name = f"{command}_{day}_{month}_{year}-{hour}_{minutes}.txt"

        with open(file_name, 'w') as file:
            file.write(output)

    def __del__(self):
        if self.__client:
            self.__client.close()
