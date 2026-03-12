
"""
Text Processing and Word Frequency Analysis

Original file is located at
    https://colab.research.google.com/drive/1FProNdsZ1wprFuOkvgnEu-k1PObyHbfj


We will fetch the first two chapters of Jane Austen's Pride and Prejudice from [Project Gutenberg](https://www.gutenberg.org/ebooks/1342)
"""

import operator
import spacy


# Function to fetch data
def fetch_text(raw_url):
    """
    Fetch text content from a URL and cache it locally.

    This function downloads text from the provided URL and stores it in a local
    cache directory so that repeated requests do not re-download the file.

    Parameters:
        raw_url (str): The URL pointing to the raw text file.

    Returns:
        str: The fetched text content as a string. Returns an empty string if
        the fetch fails.
    """
    import requests
    from pathlib import Path
    import hashlib

    CACHE_DIR = Path("cs_110_content/text_cache")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    def _url_to_filename(url):
        url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
        return CACHE_DIR / f"{url_hash}.txt"

    cache_path = _url_to_filename(raw_url)

    SUCCESS_MSG = "✅ Text fetched."
    FAILURE_MSG = "❌ Failed to fetch text."

    try:
        if not cache_path.exists():
            response = requests.get(raw_url, timeout=10)
            response.raise_for_status()
            cache_path.write_text(response.text, encoding="utf-8")

        print(SUCCESS_MSG)
        return cache_path.read_text(encoding="utf-8")

    except Exception as e:
        print(FAILURE_MSG)
        print(f"Error: {e}")
        return ""


# Save the URL in a variable
PRIDE_PREJUDICE_URL = (
    "https://gist.githubusercontent.com/goodbadwolf/"
    "8514e63776c1e9717d844ea4ee407739/raw/"
    "fdc87a64fd18e6ddb01ce8d758f8f2de8d03e163/"
    "pride_prejudice_excerpt.txt"
)

# Fetch the text
pride_prejudice_text = fetch_text(PRIDE_PREJUDICE_URL)


def print_text_stats(text):
    """
    Print basic statistics about the provided text.

    This function calculates and prints the number of characters,
    lines, and words in the given text.

    Parameters:
        text (str): The text to analyze.

    Returns:
        None
    """
    num_chars = len(text)
    lines = text.splitlines()
    num_lines = len(lines)

    num_words = 0
    for line in lines:
        num_words += len(line.split())

    print(f"Number of characters: {num_chars}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")


def get_word_counts(text):
    """
    Count the frequency of each word in the text using basic string processing.

    Words are converted to lowercase but punctuation and stop words are not removed.

    Parameters:
        text (str): The input text.

    Returns:
        dict: A dictionary mapping words to their frequency counts.
    """
    word_counts = {}
    lines = text.splitlines()

    for line in lines:
        for word in line.split():
            word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_top_10_frequent_words(text):
    """
    Print the top 10 most frequent words in the text.

    This function uses basic word counting and displays the
    10 words with the highest frequencies.

    Parameters:
        text (str): The input text.

    Returns:
        None
    """
    word_counts = get_word_counts(text)
    sorted_word_counts = dict(
        sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    )

    top_10_words = list(sorted_word_counts.items())[:10]
    for word, count in top_10_words:
        print(f"{word}: {count}")


# Print text statistics and top 10 words
print_text_stats(pride_prejudice_text)
print_top_10_frequent_words(pride_prejudice_text)


# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def word_tokenization_normalization(text):
    """
    Tokenize and normalize text using spaCy.

    This function lowercases the text, removes stop words,
    punctuation, numbers, short tokens, and lemmatizes words.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of cleaned, lemmatized words.
    """
    text = text.lower()
    doc = nlp(text)

    words_normalized = []
    for word in doc:
        if (
            word.text != "\n"
            and not word.is_stop
            and not word.is_punct
            and not word.like_num
            and len(word.text.strip()) > 2
        ):
            words_normalized.append(word.lemma_)

    return words_normalized


def word_count(word_list):
    """
    Count word frequencies from a list of words.

    Parameters:
        word_list (list): A list of words.

    Returns:
        dict: A dictionary mapping words to their frequency counts.
    """
    word_counts = {}
    for word in word_list:
        word = word.lower()
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def print_top_15_frequent_words(word_counts):
    """
    Print the top 15 most frequent words from a word count dictionary.

    Parameters:
        word_counts (dict): A dictionary mapping words to frequency counts.

    Returns:
        None
    """
    sorted_word_counts = dict(
        sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    )

    top_15_words = list(sorted_word_counts.items())[:15]
    for word, count in top_15_words:
        print(f"{word}: {count}")


# Advanced text processing results
doc_tokenized = word_tokenization_normalization(pride_prejudice_text)
new_counts = word_count(doc_tokenized)
print_top_15_frequent_words(new_counts)


"""
Comparative Analysis

Using this basic get_word_counts() function, the top 10 most frequent words are
mostly common words such as “the,” “and,” “to,” and “of.” These words appear so
often because the basic method only changes words to lowercase and splits the
text by spaces. It does not remove common words or punctuation, so these filler
words show up the most.

After using spaCy’s word_tokenization_normalization(), the top 15 words are more
useful for understanding the text. This list includes words related to people,
relationships, and social topics. The results are different because spaCy
removes common words, punctuation, numbers, and very short words. It also
combines different forms of the same word into one.

The spaCy method gives better results because it removes words that do not add
much meaning. This makes important ideas stand out more clearly. Based on the
top 15 words, the excerpt from *Pride and Prejudice* focuses on marriage, social
class, and personal relationships. Removing common words helps show what the
text is really showing.
"""