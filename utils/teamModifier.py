def remove_identical_players(list1, list2):
    # Make copies of the input lists so that we don't modify the original lists
    copy1 = list1.copy()
    copy2 = list2.copy()
    for player in copy1:
        del player["position"]
        del player['is_vice_captain']

    for player in copy2:
        del player["position"]
        del player['is_vice_captain']

    # Remove any elements that appear in both lists
    for player in copy1.copy():
        for player2 in copy2.copy():
            if player['element'] == player2['element'] and player['is_captain'] == player2['is_captain'] and \
                    player['multiplier'] == player2['multiplier'] and player2['multiplier'] != 0:
                copy1.remove(player)
                copy2.remove(player2)

    # Return the two modified lists
    return copy1, copy2
