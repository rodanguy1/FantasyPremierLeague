async def print_clean_match(fpl, user1, user1_clean_picks, user2, user2_clean_picks):
    print(user1.name, " VS ", user2.name, ":")
    await print_field_players(fpl, user1_clean_picks, user2_clean_picks)
    print()
    print("bench:")
    await print_bench_players(fpl, user1_clean_picks, user2_clean_picks)


async def print_bench_players(fpl, user1_clean_picks, user2_clean_picks):
    for i in range(len(user1_clean_picks)):
        if user1_clean_picks[i]['multiplier'] == 0:
            player1 = await fpl.get_player(user1_clean_picks[i]['element'])
            player2 = await fpl.get_player(user2_clean_picks[i]['element'])
            print(player1.web_name, " - ", player2.web_name)
    print()
    print()


async def print_field_players(fpl, user1_clean_picks, user2_clean_picks):
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
            print(player1.web_name + player1_c, " vs ", player2.web_name + player2_c)