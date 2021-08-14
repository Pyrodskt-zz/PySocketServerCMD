import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = "192.168.42.118"

port = 5001

filename = "1G.bin"

filesize = os.path.getsize(filename)

s = socket.socket()
print("connecting to {host}:{port}")

s.connect((host, port))

print("connected")

s.send(f"{filename}{SEPARATOR}{filesize}".encode())
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "rb") as f:
	while True:

		bytes_read = f.read(BUFFER_SIZE)
		if not bytes_read:
			break

		s.sendall(bytes_read)
		progress.update(len(bytes_read))

s.close()
