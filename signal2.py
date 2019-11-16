import signal
import os
import time

from common import (write_pid, get_other_pid,
                    write_to_file, read_from_file,
                    send_data, wait_loop)

pid = None
file = 'signal2.txt'
data_file = 'data2.txt'
other_file = 'signal1.txt'
other_data_file = 'data1.txt'
other_pid = None
send_signal = signal.SIGUSR1

def receive_signal(signum, stack):
    data = read_from_file(other_data_file)
    print(f'Received from app1 data: {data}')
    out_data = data[len(data)::-1]
    print(f'Replying with: {out_data}')
    send_data(data_file, out_data, other_pid, send_signal)

print('Writing pid to file')
pid = write_pid(file)
print("Getting other app's pid")
other_pid = get_other_pid(other_file)
print(f"Other app's pid: {other_pid}")


signal.signal(signal.SIGUSR2, receive_signal)

msg = f'Waiting for app1...'
wait_loop(3, msg)
