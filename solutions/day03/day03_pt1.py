# ADVENT OF CODE 2021
# Challenge #03, part 1
# Ethan Kessel

import numpy as np

def main(input: str):
#     input = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""
    input = input.splitlines()
    binary = np.array([[c == '1' for c in l] for l in input])
    gamma = binary.sum(0) > (binary.shape[0] // 2)
    epsilon = ~gamma
    places = 1 << (np.arange(binary.shape[1], 0, -1) - 1)

    gamma_dec = gamma.dot(places)
    epsilon_dec = epsilon.dot(places)
    return gamma_dec * epsilon_dec

from os import path
import time
if __name__ == "__main__":
    print("Advent of Code 2021")
    print("Challenge #03, part 1")
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

    print(f"\nExecution time: {exec_time__us:.1f}us\n\n{result = }\n")
