import requests
import json
import os
import urllib.parse
from datetime import datetime, timedelta
import time
from colorama import *
import pytz

wib = pytz.timezone('Asia/Jakarta')

class BlockBits:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'europe-west1-lumia-app-de5e9.cloudfunctions.net',
            'Origin': 'https://tg-app-embed.lumia.stream',
            'Pragma': 'no-cache',
            'Referer': 'https://tg-app-embed.lumia.stream/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Block Bits - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str) -> dict:
        parsed_query = urllib.parse.parse_qs(query)
        user_data = json.loads(parsed_query['user'][0])   
        username = user_data.get("username", "") 
        data = {
            "avatar": "",
            "first_name": user_data.get("first_name", ""),
            "language": user_data.get("language_code", "en"),
            "last_name": user_data.get("last_name", ""),
            "referral_id": "",
            "user_id": user_data.get("id", ""),
            "username": f"@{username}"
        }
        return data

    def app_settings(self, query: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/settings'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def add_user(self, query: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/addUser'
        data = json.dumps({'userData':self.load_data(query), 'referralCode':"hDKG6y3n"})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def user_data(self, query: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/userData'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def complete_onboarding(self, query: str, type: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/updateOnboarding'
        data = json.dumps({'completedOnboarding':type})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def update_streak(self, query: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/updateStreak'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                if response.status_code == 500:
                    return None
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def start_farming(self, query: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/startFarming'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def claim_farming(self, query: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/claimFarming'
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def upgrade_level(self, query: str, price: int, level: int, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/updateUpgradeLevel'
        data = json.dumps({'price':price, 'upgradeLevel':level})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def start_tasks(self, query: str, task_id: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/taskProcess'
        data = json.dumps({'status':'verification_in_progress', 'task_id':task_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def claim_tasks(self, query: str, task_id: str, retries=5):
        url = 'https://europe-west1-lumia-app-de5e9.cloudfunctions.net/api/taskProcess'
        data = json.dumps({'status':'done', 'task_id':task_id})
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Init-Data': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}[ ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def question(self):
        while True:
            farming_upgrade = input("Upgrade Farming Rate Level? [y/n] -> ").strip().lower()
            if farming_upgrade in ["y", "n"]:
                farming_upgrade = farming_upgrade == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
        
        return farming_upgrade
    
    def process_query(self, query: str, farming_upgrade: bool):

        user = self.user_data(query)
        if not user:
            login = self.add_user(query)
            if not login:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Query ID Isn't Valid {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                return
            
            if login:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {login['first_name']} {Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT}Login Successfully{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                )
                time.sleep(1)

            user = self.user_data(query)

        if user:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['user']['first_name']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['user']['points']} Bits {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Farming Rate{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} x{user['user']['farming_upgrade_level']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            time.sleep(1)

            onboarding = user['user']['onboarding']
            for type, complete in onboarding.items():
                if type and not complete:
                    update = self.complete_onboarding(query, type)
                    if update:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Onboarding{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} Type {type} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    time.sleep(1)

            update = self.update_streak(query)
            if update:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {update['points']} Bits {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            farming = user['user']['farming_started']
            if farming == 0:
                start = self.start_farming(query)
                if start:
                    start_time = datetime.fromtimestamp(start['farming_started'] / 1000) - timedelta(hours=1)
                    claim_time = (start_time + timedelta(hours=7)).astimezone(wib).strftime('%x %X %Z')
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {claim_time} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                utc_now = datetime.utcnow()
                end_time = datetime.fromtimestamp(farming / 1000) - timedelta(hours=1)
                claim_time_wib = (end_time + timedelta(hours=7)).astimezone(wib).strftime('%x %X %Z')

                if utc_now >= end_time:
                    claim = self.claim_farming(query)
                    if claim:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {claim['pointsClaimed']} Bits {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        time.sleep(1)

                        start = self.start_farming(query)
                        if start:
                            start_time = datetime.fromtimestamp(start['farming_started'] / 1000) - timedelta(hours=1)
                            claim_time = (start_time + timedelta(hours=7)).astimezone(wib).strftime('%x %X %Z')
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {claim_time} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {claim_time_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1) 

            if farming_upgrade:
                current_level = self.user_data(query)['user']['farming_upgrade_level']
                level_list = self.app_settings(query)['UPGRADE_LEVEL_LIST']

                level = None
                price = None

                for item in level_list:
                    if item['rate'] > current_level:
                        level = item['rate']
                        price = item['price']
                        break

                balance = self.user_data(query)['user']['points']
                if balance >= price:
                    upgrade = self.upgrade_level(query, price, level)
                    if upgrade:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Rate Level Is Upgraded {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Current Rate{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} x{upgrade['farming_upgrade_level']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Rate Level Isn't Upgraded {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    less_balance = price - balance
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Rate Level Isn't Upgraded {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} -{less_balance} Bits {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Rate Level Is Skipping to Upgrade {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)
                
            tasks = self.app_settings(query)['TASK_LIST']
            if tasks:
                for task in tasks:
                    task_id = task['id']

                    user_tasks_data = self.user_data(query)['user'].get('tasks', {})

                    task_status = user_tasks_data.get(task_id, {}).get('status') if user_tasks_data else None

                    skip_start = ['done', 'verification_in_progress']

                    if not user_tasks_data or task_status not in skip_start:
                        start = self.start_tasks(query, task_id)
                        if start:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(1)

                    user_tasks_data = self.user_data(query)['user'].get('tasks', {})

                    if task_status == 'verification_in_progress':
                        claim = self.claim_tasks(query, task_id)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {task['points']} Bits {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        time.sleep(1)

                    elif task_status == 'done':
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}Is Already Completed{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            farming_upgrade = self.question()

            while True:
                self.clear_terminal()
                time.sleep(1)
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, farming_upgrade)
                        self.log(f"{Fore.CYAN+Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Block Bits - BOT.{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = BlockBits()
    bot.main()