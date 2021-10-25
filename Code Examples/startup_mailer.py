#!/usr/bin/env python3
'''
    Name: startup_mailer.py
    Author: William Loring
    Created: 09/06/21
    Purpose: Email the IP address of the local GoPiGo
    Original code from: https://gist.github.com/johnantoni/8199088

# ------------------------------------------------
# History
# ------------------------------------------------
# Author        Date            Comments
# Loring        10/23/21        Added test for internet access

'''

import smtplib                            # Use to send mail
from email.message import EmailMessage    # Create email message
import ssl                                # Create secure context to send mail
import socket           # Create local socket to get local IP address
import datetime         # Get the current date and time
from time import sleep  # Use in loop to pause for trying connections

# *******************************************#
# Change the following email address to
# the email account receives email
# Add another email address to the list to
# send messages to multiple accounts
EMAIL_DESTINATION = ["Your Email Address"]

# ******************************************#
# Use a gmail email account with:
#   Two factor authentication turned off
#   Allow insecure apps
# This email account is used to send email
EMAIL_SOURCE = "Your Email Address"
EMAIL_PASSWORD = "Your Email Address Password"

# ********************************************************#
#     DO NOT CHANGE ANYTHING BELOW THIS POINT             #
# ********************************************************#

# Constants for connection to smtp server
SMTP_SERVER = "smtp.gmail.com"
PORT = 587


def send_mail(email_source, email_password, email_destination):
    # Test internet access and return local ip address
    local_ip_address = test_internet_connection()

    # Track how many times we have tried to send email
    tries = 0
    # Loop until we connect with the SMTP server
    while True:
        # After 60 tries, exit
        if (tries > 60):
            exit()
        try:
            # Connect to SMTP server
            smtpserver = smtplib.SMTP(
                SMTP_SERVER,
                PORT,
                timeout=30
            )
            break
        except Exception as e:
            print(e)
            # Increment the number of tries
            tries = tries + 1
            # Wait 1 second before we try again
            sleep(1)

    # Show all communication with the server
    # smtpserver.set_debuglevel(True)   # For testing only

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Say hello to the smtp server
    smtpserver.ehlo()
    smtpserver.starttls(context=context)
    smtpserver.ehlo
    # Logon to the smtp server
    smtpserver.login(
        email_source,
        email_password
    )

    # Get current time and date
    today = datetime.datetime.now()
    # Format current time and date
    today = today.strftime('%I:%M %p %x')

    # Email message
    message_content = str(
        today) + "\nThe GoPiGo IP address is: \n" + str(local_ip_address)
    subject = str(local_ip_address) + ' IP address for GoPiGo ' + str(today)

    # Create Email message
    msg = EmailMessage()
    msg.set_content(message_content)
    msg["Subject"] = subject
    msg["From"] = email_source
    msg["To"] = email_destination

    # Send email message
    smtpserver.send_message(msg)
    # Say goodbye to the smtp server
    smtpserver.quit()


def test_internet_connection():
    # Get local IP Address by connecting to Google DNS server
    # This step is needed if there is more than one IP address on the host
    tries = 0
    while True:
        if(tries > 60):
            exit()
        try:
            local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Ip address and port to connect to
            local_socket.connect(("8.8.8.8", 80))
            local_ip_address = local_socket.getsockname()[0]
            # print(ip_address) # For testing only
            break
        except Exception as e:
            # Print exception for testing
            print(e)
            # Increment the number of tries
            tries = tries + 1
            # Wait 3 second before we try again
            sleep(3)
    return local_ip_address


def main():
    send_mail(
        EMAIL_SOURCE,
        EMAIL_PASSWORD,
        EMAIL_DESTINATION,
    )


# Call main function
if __name__ == "__main__":
    main()
