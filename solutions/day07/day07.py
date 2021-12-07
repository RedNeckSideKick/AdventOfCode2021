# ADVENT OF CODE 2021
# Challenge #07
# Ethan Kessel

import numpy as np

SAMPLE_INPUT = """\
16,1,2,0,4,2,7,1,2,14\
"""

PT1_SAMPLE_ANS = 37

def pt1(input: str):
    starting_pos = np.array(input.split(','), dtype=int)
    alignments = np.tile(np.arange(starting_pos.min(), starting_pos.max() + 1), (len(starting_pos), 1)).T
    movements = alignments - starting_pos
    return min(abs(movements).sum(axis=1))

PT2_SAMPLE_ANS = 168

def pt2(input: str):
    starting_pos = np.array(input.split(','), dtype=int)
    alignments = np.tile(np.arange(starting_pos.min(), starting_pos.max() + 1), (len(starting_pos), 1)).T
    movements = abs(alignments - starting_pos)
    fuel = (movements * (movements + 1)) // 2
    return min(abs(fuel).sum(axis=1))

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

if __name__ == "__main__":
    colr_init()
    print(f"{Back.WHITE}{Fore.BLACK} -* Advent of Code 2021 *- {Style.RESET_ALL}")
    print("Challenge #07")
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
            if (result == sample_result):
                print(f"{Back.GREEN}{Fore.BLACK} PASSED {Style.RESET_ALL}")

                # Run full input
                result, exec_time__us = run_with_input(soln_func, prob_input)
                print(f"Part {part} (exec time {exec_time__us:.1f}us) result: {Style.BRIGHT}{result}{Style.RESET_ALL}")
            else:
                print(f"{Back.RED}{Fore.BLACK} FAILED {Style.RESET_ALL}")
                print(f"Expected {SAMPLE_INPUT}, produced:\n{Style.BRIGHT}{result}{Style.RESET_ALL}")


