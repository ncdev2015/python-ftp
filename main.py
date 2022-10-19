import ftplib

FTPSERVER = ''
USER = ''
PASSWORD = ''
PORT = 00

server = ftplib.FTP()
server.connect(FTPSERVER, PORT)
server.login(USER, PASSWORD)

# Load file to server in "/" path
filename = "txt.txt"
with open(filename, "rb") as file:    
    server.storbinary(f"STOR {filename}", file)

# Download file from server
filename = "txt.txt"
with open(filename, "wb") as file:
    # Command for Downloading the file "RETR filename"
    server.retrbinary(f"RETR {filename}", file.write)

server.dir()