import os
import time

def send_data(file_name, data, pid, signal):
    write_to_file(file_name, data)
    send_signal(pid, signal)

def send_signal(pid, signal):
    os.kill(pid, signal)

def write_to_file(file_name, data, reset=True):
    with open(file_name, 'w') as file:
        file.write(data)

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_pid(file_name):
    pid = os.getpid()
    write_to_file(file_name, str(pid))
    return pid

def get_other_pid(other_file):
    other_pid = None
    while other_pid is None:
        try:
            other_pid = read_from_file(other_file)
        except:
            pass
            time.sleep(3)
    return int(other_pid)

def wait_loop(sleep_time, msg):
    while True:
        print(msg)
        time.sleep(3)
