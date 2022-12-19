import os

import aiohttp

from utils.fplConnector import get_connection
from utils.printer import print_clean_match, print_match_metadata_summary
from utils.teamModifier import remove_identical_players

GAME_WEEK = int(os.getenv('GAME_WEEK'))


async def get_game_week_matches(fpl):
    h2h_league = await fpl.get_h2h_league(os.getenv('H2H_LEAGUE_ID'))
    fixtures = await h2h_league.get_fixture(GAME_WEEK)
    current_h2h_matches = list(map(lambda fixture: [fixture['entry_1_entry'], fixture['entry_2_entry']], fixtures))
    return current_h2h_matches


async def weekly_h2h():
    async with aiohttp.ClientSession() as session:
        fpl = await get_connection(session)
        current_h2h_matches = await get_game_week_matches(fpl)
        for match in current_h2h_matches:
            user1, user2 = await get_users_by_match(fpl, match)
            user1_picks, user2_picks = await get_users_picks(user1, user2)
            user1_clean_picks, user2_clean_picks = remove_identical_players(user1_picks[GAME_WEEK], user2_picks[
                GAME_WEEK])
            await print_clean_match(fpl, user1, user1_clean_picks, user2, user2_clean_picks)
            await print_match_metadata_summary(fpl, user1_picks, user2_picks)


async def get_users_picks(user1, user2):
    user1_picks = await user1.get_picks(GAME_WEEK)
    user2_picks = await user2.get_picks(GAME_WEEK)
    return user1_picks, user2_picks


async def get_users_by_match(fpl, match):
    user1 = await fpl.get_user(match[0])
    user2 = await fpl.get_user(match[1])
    return user1, user2
