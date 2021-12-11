# ADVENT OF CODE 2021
# Challenge #11
# Ethan Kessel

import numpy as np

# SAMPLE_INPUT = """\
# 11111
# 19991
# 19191
# 19991
# 11111\
# """
SAMPLE_INPUT = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526\
"""

PT1_SAMPLE_ANS = 1656

def pt1(input: str):
    NUM_STEPS = 100

    energy = np.array([list(line) for line in input.splitlines()], dtype=int)

    num_flashes = 0
    for stp in range(NUM_STEPS):
        energy += 1
        while np.any(energy > 9):
            flashing = energy > 9
            num_flashes += np.sum(flashing)

            dissipation = np.zeros_like(energy)

            # Use slicing to dissipate flash energy to the 8 adjacent cells
            # Location in comment is location of cell energy dissipated into
            dissipation[:-1,:-1]    += flashing[1:,1:]      # top-left
            dissipation[:,:-1]      += flashing[:,1:]       # left
            dissipation[1:,:-1]     += flashing[:-1,1:]     # bottom-left
            dissipation[1:,:]       += flashing[:-1,:]      # bottom
            dissipation[1:,1:]      += flashing[:-1,:-1]    # bottom-right
            dissipation[:,1:]       += flashing[:,:-1]      # right
            dissipation[:-1,1:]     += flashing[1:,:-1]     # top-right
            dissipation[:-1,:]      += flashing[1:,:]       # top

            energy += dissipation
            energy[flashing] = -999999999 # Prevent cells that have already flashed from re-flashing

        energy[energy < 0] = 0 # Reset flashed cells

        # if stp % 10 == 9 or stp in range(10):
        #     print(f"After step #{stp + 1}, {num_flashes=}")
        #     print(energy)

    return num_flashes

PT2_SAMPLE_ANS = 195

def pt2(input: str):

    energy = np.array([list(line) for line in input.splitlines()], dtype=int)

    num_steps = 0
    while not np.all(energy == 0):
        energy += 1
        while np.any(energy > 9):
            flashing = energy > 9

            dissipation = np.zeros_like(energy)

            # Use slicing to dissipate flash energy to the 8 adjacent cells
            # Location in comment is location of cell energy dissipated into
            dissipation[:-1,:-1]    += flashing[1:,1:]      # top-left
            dissipation[:,:-1]      += flashing[:,1:]       # left
            dissipation[1:,:-1]     += flashing[:-1,1:]     # bottom-left
            dissipation[1:,:]       += flashing[:-1,:]      # bottom
            dissipation[1:,1:]      += flashing[:-1,:-1]    # bottom-right
            dissipation[:,1:]       += flashing[:,:-1]      # right
            dissipation[:-1,1:]     += flashing[1:,:-1]     # top-right
            dissipation[:-1,:]      += flashing[1:,:]       # top

            energy += dissipation
            energy[flashing] = -999999999 # Prevent cells that have already flashed from re-flashing

        energy[energy < 0] = 0 # Reset flashed cells
        num_steps += 1

    return num_steps

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
    print("Challenge #11")
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
