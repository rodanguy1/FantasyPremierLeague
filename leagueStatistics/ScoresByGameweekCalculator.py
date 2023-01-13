import asyncio
import os

import aiohttp
import xlsxwriter

from utils.fplConnector import get_connection

GAME_WEEK = int(os.getenv('GAME_WEEK'))


async def get_users_h2h_results():
    players_to_tab = {'Guy Rodan': 0, 'eitan ganeles': 1, 'Or Finkelstein': 2, 'Yedidya Weiss': 3, 'Nir Mesery': 4,
                      'Dor Stern': 5, 'Orel Assa': 6, 'Dan Russ': 7}
    score_by_gw = [[0] * 1] * len(players_to_tab)
    async with aiohttp.ClientSession() as session:
        fpl = await get_connection(session)
        h2h_league = await fpl.get_h2h_league(os.getenv('H2H_LEAGUE_ID'))

        for game_week in range(1, GAME_WEEK + 1):
            fixtures = await h2h_league.get_fixture(game_week)
            for fixture in fixtures:
                await insert_players_results(fixture, game_week, players_to_tab, score_by_gw)
    await export_excel(players_to_tab, score_by_gw)


async def insert_players_results(fixture, game_week, players_to_tab, score_by_gw):
    player1_index = players_to_tab[fixture['entry_1_player_name']]
    player2_index = players_to_tab[fixture['entry_2_player_name']]
    scores_1_so_far = score_by_gw[player1_index].copy()
    scores_1_so_far.append(scores_1_so_far[game_week - 1] + fixture['entry_1_total'])
    score_by_gw[player1_index] = scores_1_so_far
    scores_2_so_far = score_by_gw[player2_index].copy()
    scores_2_so_far.append(scores_2_so_far[game_week - 1] + fixture['entry_2_total'])
    score_by_gw[player2_index] = scores_2_so_far


async def export_excel(players_to_tab, score_by_gw):
    workbook = xlsxwriter.Workbook('score_by_gw.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    for data in range(0, GAME_WEEK + 1):
        worksheet.write(row, 0, data)
        row += 1
    row = 0
    for col, data in enumerate(list(players_to_tab.keys())):
        worksheet.write_string(row, col + 1, data)
    row = 1
    for col, data in enumerate(score_by_gw):
        worksheet.write_column(row, col + 1, data)
    workbook.close()


if __name__ == '__main__':
    asyncio.run(get_users_h2h_results())
