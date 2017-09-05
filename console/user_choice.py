# ==============================================================================
#                                                                    USER_CHOICE
# ==============================================================================
def user_choice(msg, legal_options={"yes", "no"}):
    """ Prompts for user input in termimal untill user selects one of
        the legal options from the set.

        Continues prompting the user with same message untill they enter
        a legal option.

    Args:
        msg: (str) Message to prompt the user.
        legal_options: (set of str) The set of acceptable responses
    Returns: (str)
        Returns the legal choice that was entered by the user
        (with whitespaces stripped)
    """
    choice = ""
    while choice.strip() not in legal_options:
        choice = raw_input(msg)
    return choice
