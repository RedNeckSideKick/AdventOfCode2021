# ADVENT OF CODE 2021
# Challenge #04
# Ethan Kessel

import numpy as np

SAMPLE_INPUT = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7\
"""

BOARD_DIM = 5

PT1_SAMPLE_ANS = 4512

def pt1(input: str):
    input = input.split('\n\n') # Separate draws and boards
    draws = np.array(input[0].split(','), dtype=int)
    boards = np.array([[y.split() for y in x.split('\n')] for x in input[1:]], dtype=int)
    marked = np.zeros_like(boards, dtype=bool)
    for draw in draws:
        marked[boards == draw] = True
        row_check = np.all(marked, axis=2)
        col_check = np.all(marked, axis=1)
        if (np.any(row_check) or np.any(col_check)):
            break
    
    if np.any(row_check):
        selector = np.any(row_check, axis=1)
    else:
        selector = np.any(col_check, axis=1)

    winning = boards[selector]
    mask = ~marked[selector]
    masksum = np.sum(winning[mask])
    
    return masksum * draw

PT2_SAMPLE_ANS = 1924

def pt2(input: str):
    input = input.split('\n\n') # Separate draws and boards
    draws = np.array(input[0].split(','), dtype=int)
    boards = np.array([[y.split() for y in x.split('\n')] for x in input[1:]], dtype=int)
    marked = np.zeros_like(boards, dtype=bool)
    solved = np.array([False] * boards.shape[0])
    for draw in draws:
        marked[boards == draw] = True
        row_check = np.all(marked, axis=2)
        col_check = np.all(marked, axis=1)
        # All boards just solved
        if (np.all(np.any(row_check, axis=1) | np.any(col_check, axis=1))):
            break
        # `Or` in the solve states of each board
        solved |= np.any(row_check, axis=1) | np.any(col_check, axis=1)
    
    selector = ~solved

    losing = boards[selector]
    mask = ~marked[selector]
    masksum = np.sum(losing[mask])
    
    return masksum * draw

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
    print("Challenge #04")
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
                print(f"Expected {sample_result}, produced:\n{Style.BRIGHT}{result}{Style.RESET_ALL}")


