"""
The script in this file assumes there is a `credentials.json` file configured as
follows:

{
    "smtp_host": "smtp.gmail.com",
    "smtp_port": 587,
    "user": "MYEMAIL@gmail.com",
    "password": "MYPASSWORD"
}
"""

import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # for sending text-only messages
from email.mime.image import MIMEImage # for image attachments
# from email.mime.image import MIMEAudio # for audio attachments
import smtplib

# SETTINGS
CREDENTIALS_FILE = "credentials.json"

# ##############################################################################
#                                SUPPORT
# ##############################################################################
def connect2server(user, password, host, port):
    """ Connect to an SMTP server. Note, this function assumes that the SMTP
        server uses TTLS connection """
    server = smtplib.SMTP(host=host,port=port)
    server.starttls()
    server.login(user=user, password=password)
    return server


def send_message(server, user, to, subject="", body="", attachments=[]):
    """ Given a server client object it sends an email

    Args:
        server: connection to the server object returned by connect2server()
        user:   your email eg: "email@domain.com"
        to:     list of emails to send to
        subject: subject heading
        body:    the text of the body of the email
        attachments: list of paths to image files to upload
    """
    # BUILD MESSAGE OBJECT
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ", ".join(to)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # if attachment is not None:
    for attachment in attachments:
        msg.attach(MIMEImage(open(attachment, mode="rb").read()))

    # SEND MESSAGE.
    return server.sendmail(user, to, msg.as_string())


# ##############################################################################
#                             MAIN
# ##############################################################################
# GET CREDENTIALS - from json file
with open(CREDENTIALS_FILE, mode="r") as f:
    credentials = json.load(f)

USER = credentials["user"]
PASSWORD = credentials["password"]
HOST = credentials["smtp_host"]
PORT = credentials["smtp_port"]

# CONNECT TO SERVER
server = connect2server(user=USER,password=PASSWORD,host=HOST,port=PORT)

# SEND MESSAGE
send_message(server=server, user=USER,
    to=["tony.stark@avengers.com", "starlord@guardians.com"],
    subject="funny images",
    body="check out these funny pictures of Groot",
    attachments=["/tmp/drunk_groot.jpg", "/tmp/groot_on_fire.jpg"])

# CLOSE CONNECTION TO SERVER
server.quit()
