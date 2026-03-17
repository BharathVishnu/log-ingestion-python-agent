import time
from engine import process_log

def run_test(file_path):

    total = 0
    llm_used = 0
    regex_used = 0

    start_time = time.time()

    with open(file_path) as f:

        for line in f:

            log = line.strip()
            if not log:
                continue

            total += 1

            result = process_log(log)

            if result and "event" not in result:
                regex_used += 1
            else:
                llm_used += 1

    end_time = time.time()

    print("\n===== TEST RESULTS =====")
    print(f"Total Logs       : {total}")
    print(f"Regex Used       : {regex_used}")
    print(f"LLM Used         : {llm_used}")
    print(f"Time Taken (sec) : {round(end_time - start_time, 2)}")
    print("========================")


if __name__ == "__main__":
    run_test("logs/sample.log")