class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.total_rating = 0
        self.count = 0

    def rate(self, rating: int):
        self.total_rating += rating
        self.count += 1

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.total_rating == 0:
            return f"{self.title} ({self.seasons} seasons)" \
                   f"\ngenres: {genre_string}" \
                   f"\nno ratings"
        else:
            average = self.total_rating / self.count
            return f"{self.title} ({self.seasons} seasons)" \
                   f"\ngenres: {genre_string}" \
                   f"\n{self.count} ratings, average {average:.1f} points"

def minimum_grade(rating: float, series_list: list):
    ratingList = []
    for i in series_list:
        if i.total_rating >= rating:
            ratingList.append(i)
    return ratingList


def includes_genre(genre: str, series_list: list):
    genreList = []
    for i in series_list:
        if genre in i.genres:
            genreList.append(i)
    return genreList


if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)