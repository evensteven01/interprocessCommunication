import signal
import os
import time

from common import (write_pid, get_other_pid,
                    write_to_file, read_from_file,
                    send_data, wait_loop)

pid = None
file = 'signal1.txt'
data_file = 'data1.txt'
send_signal = signal.SIGUSR2
other_file = 'signal2.txt'
other_data_file = 'data2.txt'
other_pid = None

def receive_signal(signum, stack):
    data = read_from_file(other_data_file)
    print(f'Received from app2 data: {data}')
    out_data = input('What do you want to send?')
    send_data(data_file, out_data, other_pid, send_signal)

def start(start_text):
    send_data(data_file, start_text, other_pid, send_signal)

print('Writing pid to file')
pid = write_pid(file)
print("Getting other app's pid")
other_pid = get_other_pid(other_file)
print(f"Other app's pid: {other_pid}")

signal.signal(signal.SIGUSR1, receive_signal)

start('Lets kick this off!')

msg = f'Waiting for app2...'
wait_loop(3, msg)
