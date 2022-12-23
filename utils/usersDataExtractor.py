import os

from utils.teamModifier import remove_identical_players
from utils.userDataExtractor import get_user_transfers, get_user_chips

GAME_WEEK = int(os.getenv('GAME_WEEK'))


async def get_users_picks(user1, user2):
    user1_picks = await user1.get_picks(GAME_WEEK)
    user2_picks = await user2.get_picks(GAME_WEEK)
    return user1_picks, user2_picks


async def get_users_by_match(fpl, match):
    user1 = await fpl.get_user(match[0])
    user2 = await fpl.get_user(match[1])
    return user1, user2


async def get_users_clean_picks(user1, user2):
    user1_picks, user2_picks = await get_users_picks(user1, user2)
    user1_clean_picks, user2_clean_picks = remove_identical_players(user1_picks[GAME_WEEK], user2_picks[
        GAME_WEEK])
    return user1_clean_picks, user1_picks, user2_clean_picks, user2_picks


# won't be activated on GW 17 due to unlimited transfers
async def get_users_transfers_and_chips(fpl, user1, user2):
    output = ""
    if GAME_WEEK != 17:
        output = "GameWeek Transfers And Chips:\n"
        user1_transfers = await get_user_transfers(fpl, user1)
        user2_transfers = await get_user_transfers(fpl, user2)
        output += "{}:\n    {}\n    Transfers: ```{}```\n".format(user1.name, await get_user_chips(user1),
                                                                         user1_transfers)
        output += "{}:\n    {}\n    Transfers: ```{}```\n".format(user2.name, await get_user_chips(user2),
                                                                         user2_transfers)
    return output
