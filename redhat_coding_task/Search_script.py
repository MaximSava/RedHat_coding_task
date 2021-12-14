import re
import argparse
from colorama import Back, Style, init
import sys

# Colorama init
init()


def cmd_parser():
    # Cmd script menu options parser config
    parser = argparse.ArgumentParser(description='Script searches for lines matching regular expression.')
    parser.add_argument('-r', '--regex', dest='regex', nargs=1, type=str, help='Searches for lines matching regular '
                                                                               'expression')
    parser.add_argument('-f', '--files', dest='files', nargs='+', type=str, help='Files option')
    parser.add_argument('-u', '--underscore', dest='underscore', action='store_false',
                        help='Prints ^ under the matching text')
    parser.add_argument('-c', '--color', dest='color', action='store_false', help='Highlight matching text')
    parser.add_argument('-m', '--machine', dest='machine', action='store_false',
                        help='Generate machine readable output format: ''file_name:no_line'
                             ':start_pos:matched_text')
    parser_args = parser.parse_args()
    parser.print_help()
    return parser_args


def input_file(file=None):
    """
    STDIN if file/s option wasn’t provided.
    and checking if file encoding is
    """
    if file is None:
        file_input = input('Choose file:')
        return ascii_check(file_input)
    else:
        return ascii_check(file)


def ascii_check(file):
    # Check if non ASCII characters in file
    try:
        with open(file, 'r') as f:
            for entry in f:
                if entry.isascii() is False:
                    print(' ' * 5 + '\n' + 'Non ASCII character in file')
                    break
    except (TypeError, FileNotFoundError) as error:
        print(' ' * 5 + str(error))
        sys.exit(1)

    else:
        return file


def read_file(file, regex_string, color, underscore, machine_format):
    # Assume that input is ASCII
    file_input = input_file(file)
    # Open file and iterate line by line
    with open(file_input, 'r') as f:
        line_num = 1
        for line in f:
            if regex_string in line:
                print('regex')
                string = re.search(regex_string, line).string
                matched_text = re.search(regex_string, line).group()
                text_position = re.search(regex_string, line).span()
                start_pos = text_position[0]
                end_position = text_position[1]
                sum_characters = end_position - start_pos
                regex_search(f.name, line_num, string)

                if color is False:
                    text_highlight(string, start_pos, end_position)
                elif underscore is False:
                    print_underscore(start_pos, sum_characters)
                elif machine_format is False:
                    machine_output(f.name, line_num, start_pos, matched_text)

            line_num += 1


def regex_search(file_name, line_num, string):
    # Searches for lines matching regular expression
    print(file_name + ':' + str(line_num))
    print(string, end="")


def print_underscore(start_pos, sum_characters):
    """
    -u ( --underscore ) which prints '^' under the matching text
    """

    print(" " * start_pos + "^" * sum_characters)


def text_highlight(string, start_pos, end_position):
    """
    -c ( --color ) which highlight matching text [1]
    """
    print(string[:start_pos] + Back.GREEN + string[start_pos:end_position] + Style.RESET_ALL + string[end_position:])


def machine_output(file_name, line_num, start_pos, matched_text):
    """
    -m ( --machine ) which generate machine readable output
                  format: file_name:no_line:start_pos:matched_text
    """
    print(file_name + ':' + str(line_num) + ':' + str(start_pos) + ':' + matched_text)
    return


if __name__ == "__main__":
    print('start')
    cmd_args = cmd_parser()
    # check if -f option is none empty
    if cmd_args.files is None:
        cmd_args.files = []
        file_in = input('Enter file Name:')
        cmd_args.files.append(file_in)
        read_file(cmd_args.files[0], cmd_args.regex[0], cmd_args.color, cmd_args.underscore, cmd_args.machine)

    elif cmd_args.files:
        for i in range(len(cmd_args.files)):
            print('Field2')
            read_file(cmd_args.files[i], cmd_args.regex[0], cmd_args.color, cmd_args.underscore, cmd_args.machine)
