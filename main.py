from resources.classes.word_scorer import WordScorer

def main():
    print("Hello from word-score-app!")

    ### user inputs:
    page_url = "https://brochure.getpython.info/stories/cybo/using-python-to-serve-big-data-on-the-web-at-cybo-the-global-business-directory"
    word = "python"

    ### make the search:
    word_score_1 = WordScorer(page_url, word)
    all_pages = word_score_1.build_pages_set()

    # Calculate word occurrences and save the result in _word_occurrences
    word_score_1.calculate_word_occurrences() 

    total_occurrences = word_score_1._word_occurrences
    print("The app visited", len(all_pages), "pages.")
    print("Total word score is: ", total_occurrences)

if __name__ == "__main__":
    main()