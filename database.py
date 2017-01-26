import psycopg2

# Connect and set up cursor
def interaction_database(command):
    connection = psycopg2.connect("dbname=Ontsnapperdam user=postgres host=localhost port=5432")
    cursor = connection.cursor()

# Execute command
    cursor.execute(command)
    connection.commit()

# Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
# Nothing to fetch
        pass

# Close connection
    cursor.close()
    connection.close()

    return results

# Uploads a score into the highscore table
def upload_score(, score):
    interaction_database("UPDATE highscores SET highscores =  WHERE usernames = '{}'"
                         .format(score, name))


# Downloads score data from database
def download_scores():
    return interaction_database("SELECT * FROM highscores")


# Downloads the top score from database
def download_top_score():
    result = interaction_database("SELECT * FROM highscores ORDER BY highscores")[0][1]
    return result
