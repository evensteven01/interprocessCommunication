# Just getting familiar with signals first. We'll receive one from shell.
import signal
import os
import time

def receive_signal(signum, stack):
    print(f'Received: {signum}')

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

pid = os.getpid()
print(f'My PID is: {pid}')

while True:
    print(f'Waiting... To send me a signal, on OSX type '
          f'"kill -s USR1 {pid}" '
          f' or "kill -s USR2 {pid}"')
    time.sleep(3)
