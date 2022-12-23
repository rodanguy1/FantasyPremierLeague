import os


async def get_team_metadata(fpl, user_picks):
    total_cost = 0
    total_average_points_per_game = 0
    total_bonus_points = 0
    for player in user_picks[16]:
        player_meta = await fpl.get_player(player['element'])
        total_cost += player_meta.now_cost
        total_average_points_per_game += float(player_meta.points_per_game)
        total_bonus_points += player_meta.bonus
    return float(total_cost/10), total_average_points_per_game, float(total_bonus_points / int(os.getenv('GAME_WEEK')))


# async def get_minus_points(fpl, user):