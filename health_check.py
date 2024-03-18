#!/usr/bin/env python3
### This python programme sends an email to
##Report an error if CPU usage is over 80%
##Report an error if available disk space is lower than 20%
##Report an error if available memory is less than 500MB
##Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
import email
import shutil
import psutil
import email.message
import mimetypes
import os.path
import smtplib
import sys
import socket
#######Available disk space##########
def check_disk_full(disk,min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    if percent_free < min_percent:
        return f'Error - Available disk space is less than 20%'
######Available memory###########
def check_memory_full(disk,min_g):
    du = shutil.disk_usage(disk)
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_g:
        return f'Error - Available memory is less than 500MB'
    
########### CPU Usage ########
def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    
    if usage > percent:
        
        return f'Error - CPU usage is over 80%'
###### name resolution ########    
def name_resolution(localipaddress):
    localhost = socket.gethostbyname(localipaddress)
    if localhost != "127.0.0.1":
        return f'Error - localhost cannot be resolved to 127.0.0.1'
    

if check_disk_full("/",20):
    subject=check_disk_full("/",20)
elif check_memory_full("/",0.5):
    subject=check_memory_full("/",0.5)
elif check_cpu_usage(80):
    subject=check_cpu_usage(80)
elif name_resolution(localipaddress):
    subject=name_resolution(localipaddress)

print(subject)
    
def generate(sender, recipient, subject, body):
    """Creates an email with an attachement."""
  # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body) 
    
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = " Please check your system and resolve the issue as soon as possible."


def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('10.0.0.238')
    mail_server.send_message(message)
    mail_server.quit()
 
message=generate(sender, recipient, subject, body)
send(message)
