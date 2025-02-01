from resources.classes.word_scraper import Scraper


def main():
    print("Hello from word-score-app!")

    ### user inputs:
    page_url = "www.example.com"
    word = "word"

    scraper_1 = Scraper(page_url, word)
    total_word_score = scraper_1.word_occurrences
    print("Total word score is: ", total_word_score)

if __name__ == "__main__":
    main()
