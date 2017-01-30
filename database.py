import psycopg2

def interaction_database(command):
    connection = psycopg2.connect("dbname=Ontsnapperdam user=postgres host=localhost port=5432")
    cursor = connection.cursor()

    cursor.execute(command)
    connection.commit()

    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        pass

    cursor.close()
    connection.close()

    return results

def upload_score(name, score):
    interaction_database("UPDATE highscores SET highscores = {} WHERE usernames = '{}'"
                           .format(score, name))

def insert_players(name, score):
    interaction_database("INSERT INTO highscores VALUES ('{}', NULL)". format(name, score))


def download_scores():
    return interaction_database("SELECT * FROM highscores")

def download_top_score():
    result = ""
    result += interaction_database("SELECT * FROM highscores ORDER BY highscores ASC")[0][0] + " "
    result += str(interaction_database("SELECT * FROM highscores ORDER BY highscores ASC")[0][1])
    return result

allscores = download_scores()
winner = download_top_score()

print(download_scores())

print(download_top_score())

