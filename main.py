from resources.classes.word_scorer import WordScorer

def main():
    print("Hello from word-score-app!")

    ### user inputs:
    page_url = "https://www.lipsum.com/"
    word = "lorem"

    ### make the search:
    word_score_1 = WordScorer(page_url, word)
    all_pages = word_score_1.build_pages_set()
    # total_occurrences = word_score_1.word_occurrences()
    print("The app visited", len(all_pages), "pages.")
    # print("Total word score is: ", total_occurrences)

if __name__ == "__main__":
    main()
