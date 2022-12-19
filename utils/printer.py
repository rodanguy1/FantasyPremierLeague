from utils.teamDataCalculator import get_team_metadata


async def print_clean_match(fpl, user1, user1_clean_picks, user2, user2_clean_picks):
    print('*{} VS {}*'.format(user1.name, user2.name))
    print()
    await print_field_players(fpl, user1_clean_picks, user2_clean_picks)
    print()
    print("Bench:")
    await print_bench_players(fpl, user1_clean_picks, user2_clean_picks)


async def print_bench_players(fpl, user1_clean_picks, user2_clean_picks):
    for i in range(len(user1_clean_picks)):
        if user1_clean_picks[i]['multiplier'] == 0:
            player1 = await fpl.get_player(user1_clean_picks[i]['element'])
            player2 = await fpl.get_player(user2_clean_picks[i]['element'])
            print("```{} - {}```".format(player1.web_name, player2.web_name))
    print()


async def print_field_players(fpl, user1_clean_picks, user2_clean_picks):
    print("Clean Field Players:")
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
            print("```{} vs {}```".format(player1.web_name + player1_c,  player2.web_name + player2_c))


async def print_match_metadata_summary(fpl, user1_picks, user2_picks):
    print("Match metadata:")
    user1_total_cost, user1_average_points, user1_bps = await get_team_metadata(fpl, user1_picks)
    user2_total_cost, user2_average_points, user2_bps = await get_team_metadata(fpl, user2_picks)
    print("```Teams costs: {} vs {}```".format(user1_total_cost, user2_total_cost))
    print("```Teams average points: {:.2f} vs {:.2f}```".format(user1_average_points, user2_average_points))
    print("```Teams average bonus points: {:.2f} vs {:.2f}```".format(user1_bps, user2_bps))
    print()
    print()
