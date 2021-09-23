#!/usr/bin/env python3
'''
    Name: startup_mailer.py
    Author: William Loring
    Created: 09-06-21 Revised: 09-08-21
    Purpose: Email the IP address of the local GoPiGo
    Original scode from: https://gist.github.com/johnantoni/8199088
'''

import smtplib
import ssl
import socket
from email.mime.text import MIMEText
import datetime

# *******************************************#
# Change the following email address
# to your email address
EMAIL_DESTINATION = 'EmailAddress'

# ******************************************#
# Use a gmail email account with:
# Two factorauthentication turned off
# Allow insecure apps
EMAIL_SOURCE = 'EmailAddress'
EMAIL_PASSWORD = 'Password'

# ************************************************#
#     DO NOT CHANGE ANYTHING BELOW THIS POINT     #
# ************************************************#

# Constants for connection to smtp server
SMTP_SERVER = 'smtp.gmail.com'
PORT = 587


def send_mail(email_source, email_password, email_destination):

    # Track how many times we have tried to send email
    tries = 0
    # Loop until we connect with the SMTP server
    while True:
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
            tries = tries + 1
            # Wait 1 second before we try again
            datetime.time.sleep(1)

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Say hello to the smtp server
    smtpserver.ehlo()
    smtpserver.starttls(context=context)
    smtpserver.ehlo
    smtpserver.login(
        email_source,
        email_password
    )

    # Get current time and date
    today = datetime.datetime.now()
    # Format current time and date
    today = today.strftime('%I:%M %p %x')

    # Get local IP Address by connecting to Google DNS server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    # For testing only
    # print(ip_address)
    my_ip = '{0} \nThe GoPiGo IP address is: \n{1}'.format(today, ip_address)

    # Create Email message
    msg = MIMEText(my_ip)
    msg['Subject'] = 'IP address for GoPiGo at {0}'.format(today)
    msg['From'] = email_source
    msg['To'] = email_destination

    # Send email message
    smtpserver.sendmail(
        email_source,
        [email_destination],
        msg.as_string()
    )
    # Say goodbye to the smtp server
    smtpserver.quit()


def main():
    send_mail(
        EMAIL_SOURCE,
        EMAIL_PASSWORD,
        EMAIL_DESTINATION,
    )


# Call main function
if __name__ == "__main__":
    main()
