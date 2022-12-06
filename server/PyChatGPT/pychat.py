# Builtins
import json
import os
import time

# Local
from PyChatGPT.Classes import auth as Auth
from PyChatGPT.Classes import chat as Chat

# Fancy stuff
import colorama
from colorama import Fore

colorama.init(autoreset=True)

class PyChatGPT: 

    def __init__(self):

        # Get email & password
        self.email = os.environ['email']
        self.password = os.environ['password']
        self.previous_convo_id = None

    def initialise(self): 
        try: 
            expired_creds = Auth.expired_creds()
            print(f"{Fore.GREEN} Checking if credentials are expired...")
            if expired_creds:
                print(f"{Fore.RED} Your credentials are expired." + f" {Fore.GREEN}Attempting to refresh them...")
                open_ai_auth = Auth.OpenAIAuth(email_address=self.email, password=self.password)

                print(f"{Fore.GREEN} Credentials have been refreshed.")
                open_ai_auth.begin()
                time.sleep(3)
                is_still_expired = Auth.expired_creds()
                if is_still_expired:
                    print(f"{Fore.RED} Failed to refresh credentials. Please try again.")
                    return False
                else:
                    print(f"{Fore.GREEN} Successfully refreshed credentials.")
                    return True
            else:
                print(f"{Fore.GREEN} Your credentials are valid.")
                return True
        except Exception as e:
            print(f"{Fore.RED} An error occurred: {e}")

    def conversate(self, input):
        try: 
            print(f"{Fore.GREEN} Sending request..." + Fore.RESET)
            access_token = Auth.get_access_token()
            
            if access_token == "":
                raise Exception("Access token is missing in /Classes/auth.json.")

            answer, previous_convo = Chat.ask(auth_token=access_token,
                                            prompt=input,
                                            previous_convo_id=self.previous_convo_id)
            if answer == "400" or answer == "401":
                print(f"{Fore.RED} Your token is invalid. Attempting to refresh..")
                open_ai_auth = Auth.OpenAIAuth(email_address=self.email, password=self.password)
                open_ai_auth.begin()
                time.sleep(3)
                return "There was an error: " + answer
            else:
                if previous_convo is not None:
                    self.previous_convo_id = previous_convo

            return answer
        except Exception as e:
            print(f"{Fore.RED} An error occurred: {e}")
        







