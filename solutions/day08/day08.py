# ADVENT OF CODE 2021
# Challenge #08
# Ethan Kessel

# SAMPLE_INPUT = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
SAMPLE_INPUT = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\
"""

PT1_SAMPLE_ANS = 26

def pt1(input: str):
    input = input.splitlines()

    counter = 0

    for line in input:
        numbers = line.split("|")[1].split()
        for num in numbers:
            if len(num) in (2, 3, 4, 7): # digits 2, 7, 4, 8
                counter += 1

    return counter

PT2_SAMPLE_ANS = 61229

def pt2(input: str):
    input = input.splitlines()

    accumulator = 0

    for line in input:
        lineparts = line.split("|")
        # Sort the patterns for uniformity
        patterns = ["".join(sorted(pat)) for pat in lineparts[0].split()]
        displayed = ["".join(sorted(pat)) for pat in lineparts[1].split()]

        pattern_to_digit = {pat: None for pat in patterns}
        digit_to_patern = {x: None for x in range(10)}

        while not all(digit_to_patern.values()):
            for pat in pattern_to_digit:
                if pattern_to_digit[pat] is not None:
                    continue

                dig = None
                match len(pat):
                    case 2: # digit 1
                        dig = 1
                    case 3: # digit 7
                        dig = 7
                    case 4: # digit 4
                        dig = 4
                    case 7: # digit 8
                        dig = 8
                    case 5: # digits 2, 3, 5
                        # 3 is just extended 7
                        if digit_to_patern[7] is not None and all((c in pat for c in digit_to_patern[7])):
                            dig = 3
                        # 5 contains parts from 4 minus parts from 7
                        elif digit_to_patern[4] is not None and digit_to_patern[7] is not None and all((
                            c in pat for c in (s for s in digit_to_patern[4] if s not in digit_to_patern[7])
                        )):
                            dig = 5
                        # 2 must be remaining
                        elif digit_to_patern[3] is not None and digit_to_patern[5] is not None:
                            dig = 2
                    case 6: # digits 0, 6, 9
                        # 9 is just extended 4
                        if digit_to_patern[4] is not None and all((c in pat for c in digit_to_patern[4])):
                            dig = 9
                        # 6 is just extended 5
                        elif digit_to_patern[5] is not None and all((c in pat for c in digit_to_patern[5])):
                            dig = 6
                        # 0 must be remaining
                        elif digit_to_patern[6] is not None and digit_to_patern[9] is not None:
                            dig = 0

                if dig is not None:
                    pattern_to_digit[pat] = dig
                    digit_to_patern[dig] = pat

        number = int("".join(str(pattern_to_digit[pat]) for pat in displayed))
        accumulator += number

    return accumulator

# ==============================================================================

import typing
import time
from os import path
from colorama import init as colr_init, Fore, Back, Style

# Runs the given solution with the input
def run_with_input(func: typing.Callable[[str], typing.Any], input: str) -> tuple[typing.Any, float]:
    start_time__ns = time.perf_counter_ns()
    result = func(input)
    end_time__ns = time.perf_counter_ns()
    exec_time__us = (end_time__ns - start_time__ns) / 1000.0
    return result, exec_time__us

# Check result and ignore any errors with truth value of numpy arrays
def check_result(result: typing.Any, expected: int):
    try:
        return bool(result == expected)
    except:
        return False

if __name__ == "__main__":
    colr_init()
    print(f"{Back.WHITE}{Fore.BLACK} -* Advent of Code 2021 *- {Style.RESET_ALL}")
    print("Challenge #08")
    print("Ethan Kessel")
    print(Style.DIM + "-" * 24 + Style.RESET_ALL)

    pwd = path.dirname(__file__)
    with open(path.join(pwd, "input.txt")) as input_file:
        prob_input = input_file.read()
        print(f"{Style.DIM}Loaded input file\n{input_file.name}{Style.NORMAL}")
        print(Style.DIM + "-" * 24 + Style.RESET_ALL)

        for part, soln_func, sample_result in zip((1,2), (pt1, pt2), (PT1_SAMPLE_ANS, PT2_SAMPLE_ANS)):
            print(f"\nRunning part {part}...")

            # Run and check sample
            result, exec_time__us = run_with_input(soln_func, SAMPLE_INPUT)
            print(f"Part {part} sample (exec time {exec_time__us:.1f}us): ", end="")
            # Type comparison to short-circuit before invalid equality comparison
            if check_result(result, sample_result):
                print(f"{Back.GREEN}{Fore.BLACK} PASSED {Style.RESET_ALL}")

                # Run full input
                result, exec_time__us = run_with_input(soln_func, prob_input)
                print(f"Part {part} (exec time {exec_time__us:.1f}us) result: {Style.BRIGHT}{result}{Style.RESET_ALL}")
            else:
                print(f"{Back.RED}{Fore.BLACK} FAILED {Style.RESET_ALL}")
                print(f"Expected {sample_result}, produced:\n{Style.BRIGHT}{result}{Style.RESET_ALL}")
