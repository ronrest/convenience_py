def user_choice(msg, legal_options={"yes", "no"}):
    choice = ""
    while choice.strip() not in legal_options:
        choice = raw_input(msg)
    return choice
