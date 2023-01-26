import os
from argparse import ArgumentParser
from lib.played_for_who import Controller


def main():
    ap = ArgumentParser(
                prog        = "played-for-who",
                description = "Compare two football players' careers side by side.")
    ap.add_argument("player_1", nargs=1,
                    help="The name of the first player you wish to query.")
    ap.add_argument("player_2", nargs=1,
                    help="The name of the second player you wish to compare with.")
    args = ap.parse_args()
    ctrl = Controller(args.player_1, args.player_2)
    ctrl.show_key()
    ctrl.show_table()


if __name__ == "__main__":
    if os.path.abspath(f"{os.curdir}") != os.path.abspath(__file__)[0:-8:1]:
        print("[ERROR] Please start the bot from the same directory as the main.py file.")
        exit()
    main()
