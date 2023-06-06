import sys


def get_text(text_file):
    """ Extracts the text from the input file.
    """
    # Get text from file
    with open(text_file, 'r') as in_file:
        text = in_file.read().replace('\n', '').strip()

    # Add sentinel to the text
    # --> If not already attached
    if text[-1] != '$':
        text += '$'

    return text


def input_data():
    """ Gets the input args from the standard input.
    """
    # Inputs are processed immediately
    text = get_text(sys.argv[1])
    export_file = sys.argv[2]

    return text, export_file


def main():
    pass


if __name__ == '__main__':
    main()
