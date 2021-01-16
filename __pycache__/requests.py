from twilio.rest import Client
import sys
import os
import time
import socket

timeout = 1
socket.setdefaulttimeout(timeout)
t = "I used telegram"
sr = "+94774593440"
def setup():
    os.system("clear")
    print(name,"\n")
    irc_input = sid
    irc_joinig = token
    print_input = sid
    print_output = token
    client = Client(print_input, print_output)

    message = client.messages \
                    .create(
                         from_='whatsapp:+14155238886',
                         body= t,
                         to=sr
                 )
