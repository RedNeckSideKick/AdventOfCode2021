# ADVENT OF CODE 2021
# Challenge #{day:02}, part {part}
# Ethan Kessel

def main(input: str):
    return input

from os import path
import time
if __name__ == "__main__":
    print("Advent of Code 2021")
    print("Challenge #{day:02}, part {part}")
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
