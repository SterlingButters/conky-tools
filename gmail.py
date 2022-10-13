import imaplib
import time
import pandas as pd
import email
import base64
import json
from dotenv import load_dotenv
import os
load_dotenv()

# https://coderzcolumn.com/tutorials/python/imaplib-simple-guide-to-manage-mailboxes-using-python

USERNAME = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

################ IMAP SSL Connection ##############################
start = time.time()

try:
    imap_ssl = imaplib.IMAP4_SSL(host="imap.gmail.com", port=993) # imaplib.IMAP4_SSL_PORT = 993
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    imap_ssl = None

# print("Connection Object : {}".format(imap_ssl))
print("${font monospace:normal:size=6}"+"Total Time Taken: {:,.2f} Seconds".format(time.time() - start))

############### Login to Mailbox ######################
# print("Logging into mailbox...")

try:
    resp_code, response = imap_ssl.login(USERNAME, PASSWORD)
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    resp_code, response = None, None

print("Response {}: {}".format(resp_code, response[0].decode()))

#################### List Directories #####################
try:
    resp_code, directories = imap_ssl.list(directory="[Gmail]",) # pattern="*Starred*"
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    resp_code, directories = None, None

# print("Response Code : {}".format(resp_code))
# print("========= List of Directories =================\n")
# for directory in directories:
#     print(directory.decode())

############### Number of Messages per Directory ############
# print("\n=========== Mail Count Per Directory ===============\n")
counts = []
directory_names = []
for directory in directories:
    directory_name = directory.decode().split('"')[-2]
    directory_name = '"' + directory_name + '"'
    if directory_name == '"[Gmail]"':
        continue
    try:
        resp_code, mail_count = imap_ssl.select(mailbox=directory_name, readonly=True)
        directory_names.append(directory_name.replace("[Gmail]/", "").replace("\"", ""))
        counts.append(mail_count[0].decode())
    except Exception as e:
        print("{} - ErrorType : {}, Error : {}".format(directory_name, type(e).__name__, e))
        resp_code, mail_count = None, None

count_df = pd.DataFrame(columns=directory_names)
count_df.loc[len(count_df)] = counts
print("${font monospace:normal:size=10}"+count_df.to_string(index=False))

############### Set Mailbox #############
resp_code, mail_count = imap_ssl.select(mailbox="[Gmail]/Important", readonly=True) # DEFAULT: mailbox="INBOX"
############### Retrieve Mail IDs Directory #############
resp_code, mail_ids = imap_ssl.search(None, "ALL")
# print("Mail IDs : {}\n".format(mail_ids[0].decode().split()))

############### Display Few Messages Directory #############
MAIL_DICT = {}
new_id = 1
for mail_id in reversed(mail_ids[0].decode().split()[-5:]):
    # print("================== Start of Mail [{}] ====================".format(mail_id))
    resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)')

    message = email.message_from_bytes(mail_data[0][1])

    body = ""
    for part in message.walk():
        # print(part)
        if part.get_content_type() == "text/plain":
            # print(part.get_content_type(), part.get_content_charset(), part.get_content_maintype(), part.get("Content-Transfer-Encoding"))
            if part.get("Content-Transfer-Encoding") is None or \
               part.get("Content-Transfer-Encoding").lower() == 'quoted-printable':
                body_lines = part.as_string().split("\n")
                body += "\n".join(body_lines[3:])
            elif part.get("Content-Transfer-Encoding").lower() == 'base64':
                body_lines = part.as_string().split("\n")
                body += base64.b64decode("".join(body_lines[3:])).decode("utf-8")
            else:
                body += "Unrecognized Transfer Encoding: {}\n".format(part.get("Content-Transfer-Encoding")) + part.as_string()

        elif part.get_content_type() == "multipart/alternative":
            # print(part.as_string())
            pass

        else: # text/html (tends to be duplicate of base64/quoted printable), image/png, multipart/related
            pass
            # print("Unrecognized Content Type: ", part.get_content_type())

        MAIL_DICT["email{}".format(new_id)] = {"From": message.get("From").split("<")[0].rstrip(),
                                                 "To": message.get("To"),
                                                "Bcc": message.get("Bcc"),
                                               "Date": message.get("Date")[:-6],
                                            "Subject": message.get("Subject"),
                                               "Body": body.replace("\n", " ").replace("\r", "").split("From: Andrew Butters <sterlingbutters@tamu.edu>")[0],
                                                  "m": 0
                                              }

    new_id += 1
    # print("================== End of Mail [{}] ====================\n".format(mail_id))

# print(json.dumps(MAIL_DICT, indent=4))
with open('/home/sterlingbutters/Utilities/conky-tools/mail.json', 'w') as f:
    json.dump(MAIL_DICT, f, indent=4)

############# Close Selected Mailbox #######################
imap_ssl.close()

############### Logout of Mailbox ######################
# print("Logging Out....")
try:
    resp_code, response = imap_ssl.logout()
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    resp_code, response = None, None
# print("Response {}: {}".format(resp_code, response[0].decode()))