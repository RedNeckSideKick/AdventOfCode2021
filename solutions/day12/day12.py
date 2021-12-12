# ADVENT OF CODE 2021
# Challenge #12
# Ethan Kessel

import sys

SAMPLE_INPUT = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW\
"""

PT1_SAMPLE_ANS = 226

def pt1(input: str):
    input = input.splitlines()

    conns  = {}
    entries = []
    exits  = []

    for con in input:
        nodes = con.split("-")
        if nodes[0] == "start":
            entries.append(nodes[1])
        elif nodes[1] == "start":
            entries.append(nodes[0])
        elif nodes[1] == "end":
            exits.append(nodes[0])
        elif nodes[0] == "end":
            exits.append(nodes[1])
        else:
            if conns.get(nodes[0]) is None:
                conns[nodes[0]] = []
            if conns.get(nodes[1]) is None:
                conns[nodes[1]] = []
            conns[nodes[0]].append(nodes[1])
            conns[nodes[1]].append(nodes[0])

    paths = []

    def recurse_path(history):
        curr_node = history[-1]

        for next_node in conns[curr_node]:
            if next_node in history and next_node.islower():
                continue
            else:
                recurse_path(history + [next_node])

        if curr_node in exits:
            paths.append(history + ['end'])
            return

    for entry in entries:
        recurse_path(['start', entry])

    return len(paths)

PT2_SAMPLE_ANS = 3509

def pt2(input: str):
    # print(f"Recursion limit previously {sys.getrecursionlimit()}")
    # sys.setrecursionlimit(3000)
    # print(f"Increased to {sys.getrecursionlimit()}")

    input = input.splitlines()

    conns  = {}
    entries = []
    exits  = []

    for con in input:
        nodes = con.split("-")
        if nodes[0] == "start":
            entries.append(nodes[1])
        elif nodes[1] == "start":
            entries.append(nodes[0])
        elif nodes[1] == "end":
            exits.append(nodes[0])
        elif nodes[0] == "end":
            exits.append(nodes[1])
        else:
            if conns.get(nodes[0]) is None:
                conns[nodes[0]] = []
            if conns.get(nodes[1]) is None:
                conns[nodes[1]] = []
            conns[nodes[0]].append(nodes[1])
            conns[nodes[1]].append(nodes[0])

    paths = []
    paths_wip = []
    prev_parent_paths = []

    def recurse_path(history, double=False):
        curr_node = history[-1]

        for next_node in conns[curr_node]:
            if next_node in history and next_node.islower() and not double:
                recurse_path(history + [next_node], double=True)
            elif next_node in history and next_node.islower() and double:
                continue
            else:
                recurse_path(history + [next_node], double)

        if curr_node in exits:
            paths.append(history + ['end'])
            return

    for entry in entries:
        recurse_path(['start', entry])

    return len(paths)

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
    print("Challenge #12")
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
