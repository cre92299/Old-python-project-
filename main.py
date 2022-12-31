from time import sleep
from datetime import date
from collections import Counter

actions = {
    'action1': 'It was terrible                                       1',
    'action2': 'It was pretty bad                                     2',                                     
    'action3': 'It was alright                                        3',
    'action4': 'It was pretty good, nothing special about it though   4',
    'action5': 'It was amazing!!!!!!!!!                               5',
}

def ask_for_rating():
    print('Hey. . ')
    sleep(0.7)
    print('Soooooooo. . ..  . How was your day?')
    sleep(0.25)
    print(
        "-----------------------------------------",
        "\n",
        actions["action1"],
        "\n",
        actions["action2"],
        "\n",
        actions["action3"],
        "\n",
        actions["action4"],
        "\n",
        actions["action5"],
        "\n",
        "-----------------------------------------",
    )

def report_rating(rating):
    with open('report.txt', 'a') as f:
        f.write(f"\n {rating} | {date.today()}")

def print_rating_stats():
    with open('report.txt') as file:
        report_file = file.read()
    
    ratings = ''.join(report_file).split()[0::3]
    rating_counts = Counter(ratings)
    
    print(f"The action {rating} was reported {rating_counts.get(rating)} times")

def print_response(rating):
    if rating == '1':
        print("make the rest of your day better")
    elif rating == '2':
        print("make the rest of your day count")
    elif rating == '3':
        print("Pretty good, enjoy the rest of your day")
    elif rating == '4':
        print("Nice, enjoy the rest of your day")
    elif rating == '5':
        print("Congrats, hope you did lots of fun stuff in your day :DDD")

def main():
    ask_for_rating()
    rating = input('Which of these sounds right?  : ')
    if rating not in ['1', '2', '3', '4', '5']:
        print('Wrong number')
        sleep(2)
        exit()
    ensure_report = input("Do you want to report this to 'report.txt' (Y - Yes, N - No) :")
    if ensure_report == 'Y':
        report_rating(rating)
    print_response(rating)
    print_rating_stats()
    sleep(3)

if __name__ == "__main__":
    main()



