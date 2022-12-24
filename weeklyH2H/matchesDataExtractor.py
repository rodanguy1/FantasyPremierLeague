import os

import aiohttp

from utils.fplConnector import get_connection
from utils.matchDataExtractor import get_match_output

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
        output = await get_matches_output(current_h2h_matches, fpl)
    return output


async def get_matches_output(current_h2h_matches, fpl):
    output = ""
    for match in current_h2h_matches:
        output += await get_match_output(fpl, match)
    return output




