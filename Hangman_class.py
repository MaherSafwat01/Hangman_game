import random
import csv
import os
import datetime


class Hangman():

    def __init__(self):
        self.start()
        self.game(self.login())


    def start(self):
        if not os.path.isfile("log.txt"):
            with open("log.txt", "w") as f:
                f.write(f"log file created at {datetime.datetime.now()}")

        if not os.path.isfile("counter.csv"):
            with open("counter.csv", "w") as f:
                counter = 0
                f.write(f"login times : , {counter}")


    def reset_fun(self,cont):

        with open("counter.csv", "w") as f:
            f.write(f"login times : , {cont}")

        with open("log.txt", "w") as h:
            h.write(f"log file has been reset at {datetime.datetime.now()}")

    def login(self):

        with open("counter.csv", "r") as f:
            login_counter = csv.reader(f)
            for log, count in login_counter:
                print(log, count)
                counter = int(count)

            print("r : reset , y:login , l:log , else : exit")
            input_logn_acces = input("\nur choise ..  ?  ").lower()

            if input_logn_acces == "r":
                counter = 0
                self.reset_fun(counter)


            if input_logn_acces == "l":
                with open("log.txt", "r") as f:
                    print(f.read())

            if input_logn_acces == "y":
                counter += 1
                with open("counter.csv", "w") as f:
                    f.write(f"login times : , {counter}")

                return True


            else:
                return None

            return counter

    def game(self,cout):

        if cout == None :
            return
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
                with open("log.txt", "a") as f:
                    f.write(f"\nIn session {cout} by {usr_name} .. {shown_char} done , at time : {datetime.datetime.now()}")

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
                    with open("log.txt", "a") as f:
                        f.write(f"\nIn session {cout} by {usr_name} .. {shown_char} done , at time : {datetime.datetime.now()}")
                    print("u r done")


play=Hangman()
