import question_game_funcs

print("""Welcome to the question game!
        Here you'll be asked to choose a topic and answer questions on it, if you guess 3/5 them right you can go to the next topic.
        Guess too many wrong and it's over!
        If you guess all of the topics to the end you'll be taken to a secret topic with questions from any possible genre.
        Get all the answers right and you win the game in an amazing way, if not it won't be an amazing victory, you decide how your legacy ends!
        Will you be overall victorious or just good enough to get by?  Lets find out!""")

completed_topics = []
question_game_funcs.game_selection(completed_topics)