# ADVENT OF CODE 2021
# Challenge #03, part 2
# Ethan Kessel

import numpy as np

def main(input: str):
    input = input.splitlines()
    binary = np.array([[c == '1' for c in l] for l in input], dtype=int)

    bin_oxy = binary.copy()
    bin_co2 = binary.copy()
    for col in range(binary.shape[1]):
        if bin_oxy.shape[0] > 1:
            target = bin_oxy[:, col].sum() * 2 >= bin_oxy.shape[0]
            bin_oxy = bin_oxy[bin_oxy[:, col] == target]
        if bin_co2.shape[0] > 1:
            target = not (bin_co2[:, col].sum() * 2 >= bin_co2.shape[0])
            bin_co2 = bin_co2[bin_co2[:, col] == target]

    places = 1 << (np.arange(binary.shape[1], 0, -1) - 1)

    oxy_dec = bin_oxy[0].dot(places)
    co2_dec = bin_co2[0].dot(places)
    return oxy_dec * co2_dec

from os import path
import time
if __name__ == "__main__":
    print("Advent of Code 2021")
    print("Challenge #03, part 2")
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
