current_usernames = ['sunny123', 'cool_dude45', 'admin', 'sparkle_girl', 'ninja_warrior', 'music_lover']
new_users = ['sunny123', 'superstar_23', 'sparkle_girl', 'glitter_princess', 'shadow_ninja', 'music_lover']

curr_users = [username.lower() for username in current_usernames]

for new_user in new_users:
    if new_user.lower() in curr_users:
        print('person need to enter new username')
    else:
        print('username is available')