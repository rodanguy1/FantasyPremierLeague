import os

GAME_WEEK = int(os.environ.get('GAME_WEEK'))


async def get_user_transfers(fpl, user):
    output = ""
    user1_transfers = await user.get_transfers(GAME_WEEK)
    for transfer in user1_transfers:
        player_out = (await fpl.get_player(transfer['element_out'])).web_name
        player_in = (await fpl.get_player(transfer['element_in'])).web_name
        output += "{} -> {}".format(player_out, player_in)
        output += "   "
    if output == "":
        output = "None"
    return output


async def get_user_chips(user):
    return "Chips: ```{}```".format(await user.get_active_chips(GAME_WEEK))
