from resources.classes.word_scorer import WordScorer

def main():
    print("Hello from word-score-app!")

    ### user inputs:
    page_url = "https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0"
    word = "hooks"

    ### make the search:
    word_score_1 = WordScorer(page_url, word)
    all_pages = word_score_1.build_pages_set()
    total_occurrences = word_score_1._word_occurrences
    print("The app visited", len(all_pages), "pages.")
    print("Total word score is: ", total_occurrences)

if __name__ == "__main__":
    main()
