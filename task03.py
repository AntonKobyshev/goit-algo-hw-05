import timeit
from pathlib import Path
from helpers.algorytms.knuth_morris_pratt import knuth_morris_pratt
from helpers.algorytms.boyer_moore import boyer_moore
from helpers.algorytms.rabin_karp import rabin_karp
from helpers.markdown_template import (
    mgs_FileNotFound,
    mgs_WrongEncoding,
    output_head,
    fastest_result,
)

# Constants
PATH_TEXT_1 = Path.cwd().joinpath("db/article1.txt")
PATH_TEXT_2 = Path.cwd().joinpath("db/article2.txt")
PATTERN_RESULT = "Література"
PATTERN_NO_RESULT = "Помʼятий"
NUM_ITERATIONS = 100

# Function to perform benchmarking
def benchmark(text, pattern):
    results = {}
    for key, algorithm in algorithms.items():
        execution_time = timeit.timeit(
            lambda: algorithm(text, pattern), number=NUM_ITERATIONS
        )
        results[key] = round(execution_time, 5)
    return results

if __name__ == "__main__":
    try:
        # Read text from files
        with open(PATH_TEXT_1, "r", encoding="utf-8") as file_path:
            test_text_1 = file_path.read()
        with open(PATH_TEXT_2, "r", encoding="utf-8") as file_path:
            test_text_2 = file_path.read()

        algorithms = {
            "knuth_morris_pratt": knuth_morris_pratt,
            "boyer_moore": boyer_moore,
            "rabin_karp": rabin_karp,
        }

        # Benchmark approach 1
        print("APPROACH 1")
        results_1 = benchmark(test_text_1, PATTERN_RESULT)
        fastest_algorithm_1, fastest_time_1 = min(results_1.items(), key=lambda x: x[1])
        benchmark_res_1 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results_1.items()
        )
        print(output_head, benchmark_res_1, end="\n")
        print(fastest_result.format(fastest_algorithm_1, fastest_time_1))

        # Benchmark approach 1 with pattern_no_result
        results_1 = benchmark(test_text_1, PATTERN_NO_RESULT)
        fastest_algorithm_1, fastest_time_1 = min(results_1.items(), key=lambda x: x[1])
        benchmark_res_1 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results_1.items()
        )
        print(output_head, benchmark_res_1, end="\n")
        print(fastest_result.format(fastest_algorithm_1, fastest_time_1))

        # Benchmark approach 2
        print("APPROACH 2")
        results_2 = benchmark(test_text_2, PATTERN_RESULT)
        fastest_algorithm_2, fastest_time_2 = min(results_2.items(), key=lambda x: x[1])
        benchmark_res_2 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results_2.items()
        )
        print(output_head, benchmark_res_2, end="\n")
        print(fastest_result.format(fastest_algorithm_2, fastest_time_2))

        # Benchmark approach 2 with pattern_no_result
        results_2 = benchmark(test_text_2, PATTERN_NO_RESULT)
        fastest_algorithm_2, fastest_time_2 = min(results_2.items(), key=lambda x: x[1])
        benchmark_res_2 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results_2.items()
        )
        print(output_head, benchmark_res_2, end="\n")
        print(fastest_result.format(fastest_algorithm_2, fastest_time_2))

    except FileNotFoundError as error:
        print(mgs_FileNotFound.format(type(error).__name__))
    except UnicodeDecodeError as error:
        print(mgs_WrongEncoding.format(type(error).__name__))
