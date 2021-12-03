# Command-line utility for quickly creating solution files from templates

import argparse
import os
from os import path
import string

# Wrapper class for formatting strings but passing through missing keys
# https://stackoverflow.com/a/35667660
class SafeFormatter(string.Formatter):
    def vformat(self, format_string, args, kwargs):
        args_len = len(args)  # for checking IndexError
        tokens = []
        for (lit, name, spec, conv) in self.parse(format_string):
            # re-escape braces that parse() unescaped
            lit = lit.replace('{', '{{').replace('}', '}}')
            # only lit is non-None at the end of the string
            if name is None:
                tokens.append(lit)
            else:
                # but conv and spec are None if unused
                conv = '!' + conv if conv else ''
                spec = ':' + spec if spec else ''
                # name includes indexing ([blah]) and attributes (.blah)
                # so get just the first part
                fp = name.split('[')[0].split('.')[0]
                # treat as normal if fp is empty (an implicit
                # positional arg), a digit (an explicit positional
                # arg) or if it is in kwargs
                if not fp or fp.isdigit() or fp in kwargs:
                    tokens.extend([lit, '{', name, conv, spec, '}'])
                # otherwise escape the braces
                else:
                    tokens.extend([lit, '{{', name, conv, spec, '}}'])
        format_string = ''.join(tokens)  # put the string back together
        # finally call the default formatter
        return string.Formatter.vformat(self, format_string, args, kwargs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates Advent of Code solution files from a template.")
    parser.add_argument("day", type=int, choices=range(1, 26), metavar="day", help="Challenge day, 1-25")
    parser.add_argument("--force", default="x", action="store_const", const="w", help="Force file creation if exists")

    args = parser.parse_args()
    print(f"Creating solution files for day {args.day}")

    mod_path = path.dirname(__file__)
    with open(path.join(mod_path, "template", "soln_template.py")) as template_file:
        # Open the template and replace the challenge info sections
        # F-strings are used in other places, so the special formatter is needed
        # to pass them through without errors
        template = template_file.read()
        template = SafeFormatter().format(template, day=args.day)

        # Make the folder for the solution files (ok if they already exist)
        solution_dir = path.join(os.getcwd(), "solutions", f"day{args.day:02}")
        os.makedirs(solution_dir, exist_ok=True)
        # Create the solution file from the template (stop if already exists and no --force)
        solution_fname = path.join(solution_dir, f"day{args.day:02}.py")
        try:
            with open(solution_fname, args.force) as solution_file:
                solution_file.write(template)
                os.system(f"code {solution_file.name}")
        except FileExistsError as e:
            print(e)
            print("File already exists, use `--force` to force file overwrite")
            os.system(f"code {solution_fname}")
        
        # Open up the file for the input
        os.system(f"code {path.join(solution_dir, 'input.txt')}")
