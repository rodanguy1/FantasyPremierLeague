import os

from utils.teamDataCalculator import get_team_metadata


async def get_users_transfers(fpl, user1, user2):
    output = "GameWeek Transfers:\n"
    user1_transfers = await get_user_transfers(fpl, user1)
    user2_transfers = await get_user_transfers(fpl, user2)
    output += "{}: ```{}```\n".format(user1.name, user1_transfers)
    output += "{}: ```{}```\n".format(user2.name, user2_transfers)
    return output


async def get_user_transfers(fpl, user):
    output = ""
    user1_transfers = await user.get_transfers(int(os.environ.get('GAME_WEEK')))
    for transfer in user1_transfers:
        player_out = (await fpl.get_player(transfer['element_out'])).web_name
        player_in = (await fpl.get_player(transfer['element_in'])).web_name
        output += "{} -> {}".format(player_out, player_in)
        output += "   "
    return output


async def get_clean_match(fpl, user1, user1_clean_picks, user2, user2_clean_picks):
    output = await get_field_players(fpl, user1_clean_picks, user2_clean_picks)
    output += await get_bench_players(fpl, user1_clean_picks, user2_clean_picks)
    return output


async def get_bench_players(fpl, user1_clean_picks, user2_clean_picks):
    output = "\nBench:\n"
    for i in range(len(user1_clean_picks)):
        if user1_clean_picks[i]['multiplier'] == 0:
            player1 = await fpl.get_player(user1_clean_picks[i]['element'])
            player2 = await fpl.get_player(user2_clean_picks[i]['element'])
            output += "```{} - {}```\n".format(player1.web_name, player2.web_name)
    output += "\n"
    return output


async def get_field_players(fpl, user1_clean_picks, user2_clean_picks):
    output = "\nClean Field Players:\n"
    for i in range(len(user1_clean_picks)):
        if user1_clean_picks[i]['multiplier'] != 0 and user2_clean_picks[i]['multiplier']:
            player1 = await fpl.get_player(user1_clean_picks[i]['element'])
            player2 = await fpl.get_player(user2_clean_picks[i]['element'])
            player1_c = ""
            player2_c = ""
            if user1_clean_picks[i]['is_captain']:
                player1_c = " (C)"
            if user2_clean_picks[i]['is_captain']:
                player2_c = " (C)"
            output += "```{} vs {}```\n".format(player1.web_name + player1_c, player2.web_name + player2_c)
    return output


async def get_match_metadata_summary(fpl, user1_picks, user2_picks):
    output = "Match metadata:\n"
    user1_total_cost, user1_average_points, user1_bps = await get_team_metadata(fpl, user1_picks)
    user2_total_cost, user2_average_points, user2_bps = await get_team_metadata(fpl, user2_picks)
    output += "```Teams costs: {} vs {}```\n".format(user1_total_cost, user2_total_cost)
    output += "```Teams average points: {:.2f} vs {:.2f}```\n".format(user1_average_points, user2_average_points)
    output += "```Teams average bonus points: {:.2f} vs {:.2f}```\n\n\n".format(user1_bps, user2_bps)
    return output