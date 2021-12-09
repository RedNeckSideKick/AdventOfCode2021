# ADVENT OF CODE 2021
# Challenge #05
# Ethan Kessel

import re # Regular expressions to help with splitting
import numpy as np

SAMPLE_INPUT = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2\
"""

PT1_SAMPLE_ANS = 5

def pt1(input: str):
    input = input.splitlines()
    lines = np.array([re.split(",| -> ", line) for line in input], dtype=int).reshape((len(input), 2, 2))
    grid = np.zeros([lines.max() + 1] * 2, dtype=int)

    for line in lines:
        # Filter on horizontal and vertical lines only
        if line[0,0] == line[1,0]: # vertical y-axis line
            start = min(line[:,1])
            end = max(line[:,1])
            grid[start : end + 1, line[0,0]] += 1
        elif line[0,1] == line[1,1]: # horizontal x-axis line
            start = min(line[:,0])
            end = max(line[:,0])
            grid[line[0,1], start : end + 1] += 1

    targets = grid >= 2

    return np.sum(targets)

PT2_SAMPLE_ANS = 12

def pt2(input: str):
    input = input.splitlines()
    lines = np.array([re.split(",| -> ", line) for line in input], dtype=int).reshape((len(input), 2, 2))
    grid = np.zeros([lines.max() + 1] * 2, dtype=int)

    for line in lines:
        if line[0,0] == line[1,0]: # vertical y-axis line
            start = min(line[:,1])
            end = max(line[:,1])
            grid[start : end + 1, line[0,0]] += 1
        elif line[0,1] == line[1,1]: # horizontal x-axis line
            start = min(line[:,0])
            end = max(line[:,0])
            grid[line[0,1], start : end + 1] += 1
        else: # must be 45-degree diagonal
            for x, y in zip(np.linspace(line[0,0], line[1,0], abs(line[1,0] - line[0,0]) + 1, dtype=int),
                            np.linspace(line[0,1], line[1,1], abs(line[1,1] - line[0,1]) + 1, dtype=int)):
                grid[y,x] += 1

    targets = grid >= 2

    return np.sum(targets)

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
    print("Challenge #05")
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
