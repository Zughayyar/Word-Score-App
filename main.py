from resources.classes.word_scorer import WordScorer


def main():
    print("Hello from word-score-app!")

    ### user inputs:
    page_url = "www.example.com"
    word = "word"

    ### make the search:
    word_score_1 = WordScorer(page_url, word)
    all_pages = word_score_1.build_pages_set()
    total_occurrences = word_score_1.word_occurrences()
    all_pages = word_score_1.build_pages_set()
    total_occurrences = word_score_1.word_occurrences()
    print("The app visited", all_pages.size, "pages.")
    print("Total word score is: ", total_occurrences)

if __name__ == "__main__":
    main()
