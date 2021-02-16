# by Kami Bigdely
# Extract class
class Actors:
    def __init__(self, first_names, last_names, birth_year, movies):
        self.first_names = first_names
        self.last_names = last_names
        self.birth_year = birth_year
        self.movies = movies

    def send_hiring_email(self, emails):
        for i, email in enumerate(emails):
            if self.birth_year[i] > 1985:
                print(self.first_names[i], self.last_names[i])
                print('Movies Played: ', end=' ')
                for m in self.movies[i]:
                    print(m, end=', ')
                print()
                print("email sent to: ", email)

first_names = ['Elizabeth', 'Jim']
last_names = ['Debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virginia', 'Guardians of the Galaxy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

actors = new Actors(first_names, last_names, birth_year, movies)
actors()
