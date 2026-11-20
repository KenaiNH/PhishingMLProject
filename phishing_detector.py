import argparse
from functools import lru_cache
from pathlib import Path
from project_common import clean_text, load_pickle


@lru_cache(maxsize=1)
def get_model():
    return load_pickle('final_phishing_model.pkl')


def classify_email(email_text):
    if not isinstance(email_text, str) or not clean_text(email_text):
        raise ValueError('Provide email text containing words, not just links or punctuation.')
    model = get_model()
    if model.named_steps['tfidf'].transform([email_text]).nnz == 0:
        raise ValueError('No words in this message match the trained vocabulary.')
    return 'Phishing Email' if int(model.predict([email_text])[0]) == 1 else 'Legitimate Email'


def main():
    parser = argparse.ArgumentParser(description='Classify email text using the final trained pipeline.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--text', help='Email text to classify')
    group.add_argument('--file', type=Path, help='UTF-8 text file, including multiline emails')
    args = parser.parse_args()
    if args.text is not None or args.file is not None:
        try:
            text = args.text if args.text is not None else args.file.read_text(encoding='utf-8')
            print(classify_email(text))
        except (ValueError, OSError) as error:
            parser.exit(2, str(error) + '\n')
        return
    print('Phishing Detection Tool. Type exit to quit; use --file for multiline emails.')
    while True:
        try:
            text = input('Enter email text: ')
        except (EOFError, KeyboardInterrupt):
            break
        if text.strip().lower() == 'exit':
            break
        try:
            print(classify_email(text))
        except ValueError as error:
            print(error)


if __name__ == '__main__':
    main()
