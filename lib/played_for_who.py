from lib import COLOUR
from lib.request_api import get_career_dummy_1, get_career_dummy_2
from lib.table_maker import careers_to_table


class Controller:

    def __init__(self, player_1, player_2):
        self.player_1_name = player_1[0]
        self.player_2_name = player_2[0]
        self.player_1_career = get_career_dummy_1(self.player_1_name)
        self.player_2_career = get_career_dummy_2(self.player_2_name)
        self.table = careers_to_table(self.player_1_name, self.player_2_name, self.player_1_career, self.player_2_career)


    def show_table(self):
        for row in self.table:
            print(row)

    def show_key(self):
        print(f"""
            Key:
                [{COLOUR.SHARED}█████{COLOUR.END}] = Players at the same club during the same season.
                [{COLOUR.COMMON}█████{COLOUR.END}] = Clubs that are common with both players.
        """)


if __name__ == "__main__":
    pass
