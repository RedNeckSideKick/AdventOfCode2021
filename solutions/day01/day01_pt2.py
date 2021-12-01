# ADVENT OF CODE 2021
# Challenge #01, part 2
# Ethan Kessel

def main(input: str):
    # input = """
    #     199
    #     200
    #     208
    #     210
    #     200
    #     207
    #     240
    #     269
    #     260
    #     263
    # """
    depths = list(map(int, input.split()))
    # print(depths, len(depths))
    increasing = 0
    for idx in range(3, len(depths)):
        slice0 = depths[idx - 3 : idx]
        slice1 = depths[idx - 2 : idx + 1]
        # print(idx, slice0, slice1)
        if sum(slice1) > sum(slice0):
            increasing += 1
    return increasing

from os import path
import time
if __name__ == "__main__":
    print("Advent of Code 2021")
    print("Challenge #01, part 2")
    print("Ethan Kessel")
    print("-" * 24)

    pwd = path.dirname(__file__)
    with open(path.join(pwd, "input.txt")) as input_file:
        print(f"Executing on input file\n{input_file.name}")
        print("-" * 24)

        start_time__ns = time.perf_counter_ns()
        result = main(input_file.read())
        end_time__ns = time.perf_counter_ns()
        exec_time__us = (end_time__ns - start_time__ns) / 1000.0

    print(f"\nExecution time: {exec_time__us:.1f}us\n\n{result=}\n")
