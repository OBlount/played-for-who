from lib import COLOUR
from prettytable import PrettyTable


def careers_to_table(player_1_name, player_2_name, player_1_career, player_2_career) -> str:
    table = PrettyTable()
    table.field_names = ["Season", player_1_name, player_2_name]
    longest_career = __longest_career(player_1_career, player_2_career)
    for season in range(len(longest_career)):
        table.add_row([
            __get_string_from_record(list(longest_career.keys()), season),
            __get_string_from_record(list(player_1_career.values()), season),
            __get_string_from_record(list(player_2_career.values()), season)
        ])
    table.align[player_1_name] = 'r'
    table.align[player_2_name] = 'l'
    table = __add_splash_of_colour(table.get_string(), player_1_career, player_2_career)
    return table

def __longest_career(player_1_career, player_2_career):
    player_1_career_length = len(player_1_career)
    player_2_career_length = len(player_2_career)
    return player_1_career if player_1_career_length >= player_2_career_length else player_2_career


def __get_string_from_record(record, index) -> str:
    try:
        return record[index]
    except IndexError:
        return "N/A"


def __add_splash_of_colour(table: str, player_1_career: dict, player_2_career: dict) -> str:
    coloured_table = table.splitlines()
    common_clubs_set = set(player_1_career.values()) & set(player_2_career.values())
    for row in range(len(coloured_table)):
        for common_club in common_clubs_set:
            if(common_club in coloured_table[row]):
                coloured_table[row] = coloured_table[row].replace(common_club, COLOUR.COMMON + common_club + COLOUR.END)
    for season in range(len(__longest_career(player_1_career, player_2_career))):
        player_1_record = __get_string_from_record(list(player_1_career.values()), season)
        player_2_record = __get_string_from_record(list(player_2_career.values()), season)
        if(player_1_record == player_2_record):
            coloured_table[season + 3] = coloured_table[season + 3].replace(COLOUR.COMMON, "")
            coloured_table[season + 3] = coloured_table[season + 3].replace(COLOUR.END, "")
            coloured_table[season + 3] = COLOUR.BOLD + COLOUR.SHARED + coloured_table[season + 3] + COLOUR.END
    return coloured_table


if __name__ == "__main__":
    pass
