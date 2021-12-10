# ADVENT OF CODE 2021
# Challenge #09
# Ethan Kessel

import numpy as np
from numpy.core.numeric import zeros_like

SAMPLE_INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678\
"""

PT1_SAMPLE_ANS = 15

def pt1(input: str):
    input = input.splitlines()
    heightmap = np.array([list(line) for line in input], dtype=int)

    # Check gradient direction for decrease
    right   = np.pad(heightmap[:, 1:] < heightmap[:, :-1], ((0,0),(1,0)), constant_values=True)
    left    = np.pad(heightmap[:, :-1] < heightmap[:, 1:], ((0,0),(0,1)), constant_values=True)
    down    = np.pad(heightmap[1:,:] < heightmap[:-1,:], ((1,0),(0,0)), constant_values=True)
    up      = np.pad(heightmap[:-1,:] < heightmap[1:,:], ((0,1),(0,0)), constant_values=True)

    minima_mask = right & left & down & up
    local_minima = heightmap[minima_mask]

    return np.sum(local_minima + 1)

PT2_SAMPLE_ANS = 1134

def pt2(input: str):
    input = input.splitlines()
    heightmap = np.array([list(line) for line in input], dtype=int)

    basinmap = zeros_like(heightmap)

    # Check gradient direction for decrease
    right   = np.pad(heightmap[:, 1:] < heightmap[:, :-1], ((0,0),(1,0)), constant_values=True)
    left    = np.pad(heightmap[:, :-1] < heightmap[:, 1:], ((0,0),(0,1)), constant_values=True)
    down    = np.pad(heightmap[1:,:] < heightmap[:-1,:], ((1,0),(0,0)), constant_values=True)
    up      = np.pad(heightmap[:-1,:] < heightmap[1:,:], ((0,1),(0,0)), constant_values=True)

    minima_mask = right & left & down & up
    minima_coords = list(zip(*np.where(minima_mask)))

    # Recursive programming!
    def flood_fill(fill, start, direction):
        x, y = start
        dx_0, dy_0 = direction
        
        # Proceed in the relatibe forward, right, and left directions
        for dx, dy in [(dx_0, dy_0), (dy_0, -dx_0), (-dy_0, dx_0)]:
            # Check if adjacent tile in direction exists
            if x + dx in range(0, basinmap.shape[0]) and y + dy in range(0, basinmap.shape[1]):
                # Check for unmarked cell not at max height
                if basinmap[x+dx, y+dy] == 0 and heightmap[x+dx,y+dy] != 9:
                    # Fill and continue in that direction
                    basinmap[x+dx, y+dy] = fill
                    flood_fill(fill, (x+dx, y+dy), (dx,dy))

    for i, minimum in enumerate(minima_coords):
        basinmap[minimum] = i + 1
        flood_fill(i + 1, minimum, (1, 0))
        flood_fill(i + 1, minimum, (0, 1))
        flood_fill(i + 1, minimum, (-1, 0))
        flood_fill(i + 1, minimum, (0, -1))

    # Calculate counts of basin size
    basin_sizes = np.bincount(basinmap[basinmap != 0])
    basin_sizes.sort() # Sort the array to filter largest values to the end

    return np.prod(basin_sizes[-3:])

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
    print("Challenge #09")
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
