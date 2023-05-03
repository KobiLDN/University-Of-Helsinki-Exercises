def sort_by_seasons(items: list):

    def order_by_seasons(item: dict):
        return item["seasons"]

        #return [value for key, value in item.items() if key == "seasons"]

        # for key, value in item.items():
        #     if key == "seasons":
        #         return value

    return sorted(items, key=order_by_seasons)

if __name__ == "__main__":
    shows = [{'name': 'The Wire', 'rating': 9.3, 'seasons': 5}, {'name': 'Game of Thrones', 'rating': 9.2, 'seasons': 8}, {'name': 'Band of Brothers', 'rating': 9.4, 'seasons': 1}, {'name': 'Sopranos', 'rating': 9.2, 'seasons': 6}, {'name': 'Sherlock', 'rating': 9.1, 'seasons': 4}]
    # sort_by_seasons(shows)
    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")
