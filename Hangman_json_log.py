import random
import os
import datetime
import json

class Hangman():

    def __init__(self):
        self.start()
        self.game(self.login())

    def start(self):
        """It's a function to check if log file exit , and create it if not"""
        if not os.path.isfile("log.json"):
            with open("log.json","w")as f:
                data={
                    "counter":int(0),
                    "people":[]
                    }
                json.dump(data, f)
            return

    def reset_fun(self):
        """It's a function to reset log file """
        with open("log.json","w") as f:

            data ={
                "counter":(0),
                "reset_time":str(datetime.datetime.now()),
                "people":[]
                }

            return json.dump(data,f)

    def login(self):
            """It's a function that takes the first command of the game and care of the log file """
            with open("log.json") as f:
                data=json.load(f)
                print(f"you have been logged {data['counter']} Times , by {len(data['people'])} people")

            print("r : reset , y:login , l:log , else : exit")

            input_logn_acces = input("\nUr choise ..  ?  ").lower()

            if input_logn_acces == "r":
                self.reset_fun()
                return None

            if input_logn_acces == "l":
                with open("log.json") as f:
                    log=json.load(f)

                    print(f"you logged {log['counter']} \n")
                    if "reset_time" in log:
                        print(f"Log file was reseted at : {log['reset_time']}")
                    print(f"the game played {len(log['people'])}, the players are :\n ")
                    for person in log["people"]:
                        print(person)
                    if len(log["people"]) == 0 :
                        print("No one played yet")

                return None

            if input_logn_acces == "y":
                with open("log.json") as f:
                    data=json.load(f)
                    data["counter"]+=1
                with open("log.json","w") as f :
                    json.dump(data,f)

                return True

            else:
                return None

    def insert(self,session_no,name,done,time):
        """It's the insertion of the player data into the log"""
        with open("log.json")as f :
            data=json.load(f)
            person = dict()
            person["session"] = session_no
            person["name"] = name
            person["done"] = done
            person["session_date"] = time
            data["people"].append(person)
            with open("log.json", "w") as e:
                json.dump(data, e)

    def game(self,inp):
        """The Gamed function , which responsable about words and others.."""
        if inp == None:
            return

        with open("log.json") as f :
            data=json.load(f)

        usr_name = input("Enter ur name :  ")
        words = ["this", "is", "the", "game","words"]
        hidden_word = random.choice(words)

        print("quit with typing exit or keep input \n")

        hdn_word_splited = []
        for i in hidden_word:
            hdn_word_splited.append(i)

        num_ltrs = len(hdn_word_splited)

        shown_char = []
        for i in range(num_ltrs):
            shown_char.append("_")

        print(shown_char)

        inp_by_usr_list = []

        start_key = 1
        while start_key:
            print(f"\n u have {num_ltrs} digit left \n")

            inp_by_usr = input("\nplz enter ur char ..... : ").lower()

            if inp_by_usr == "exit":
                start_key = None
                self.insert(data["counter"],usr_name,shown_char,str(datetime.datetime.now()))


            else:
                inp_by_usr_list.append(inp_by_usr)

                if inp_by_usr in hdn_word_splited:
                    hdn_word_splited.remove(inp_by_usr)
                    num_ltrs -= 1

                    print(f"u entered {inp_by_usr_list}")

                    x = hidden_word.rfind(f"{inp_by_usr}")
                    shown_char[x] = inp_by_usr

                    print(shown_char)


                else:
                    print("not there , try again", shown_char)

                if num_ltrs == 0:
                    print("Bravooo")
                    start_key = None
                    self.insert(data["counter"], usr_name, shown_char, str(datetime.datetime.now()))
                    print("u r done")


play=Hangman()