import subprocess
import time
import os

test_cases = [
    ("3input1.txt", "3output1.txt", 4),
    ("3input2.txt", "3output2.txt", 4),
    ("3input3.txt", "3output3.txt", 4),
    ("3input4.txt", "3output4.txt", 4),
    ("3input5.txt", "3output5.txt", 4),
    ("3input6.txt", "3output6.txt", 4),
    ("3input7.txt", "3output7.txt", 4),
    ("3input8.txt", "3output8.txt", 4),
    ("3input9.txt", "3output9.txt", 4),
    ("3input10.txt", "3output10.txt", 4),
]

solution_file = None
for file in os.listdir("."):
    if file.endswith(".py") or file.endswith(".java") or file.endswith(".cpp"):
        solution_file = file
        break

if not solution_file:
    print("❌ No valid solution file found (.py, .java, .cpp)")
    exit(1)

if solution_file.endswith(".py"):
    run_command = ["python3", solution_file]
elif solution_file.endswith(".java"):
    compile_command = ["javac", solution_file]
    run_command = ["java", solution_file.replace(".java", "")]
elif solution_file.endswith(".cpp"):
    compiled_file = "solution.out"
    compile_command = ["g++", solution_file, "-o", compiled_file]
    run_command = ["./" + compiled_file]
else:
    print("❌ Unsupported language")
    exit(1)

if solution_file.endswith((".java", ".cpp")):
    compile_result = subprocess.run(compile_command, capture_output=True, text=True)
    if compile_result.returncode != 0:
        print(f"❌ Compilation failed:\n{compile_result.stderr}")
        exit(1)

def run_test_case(input_file, expected_output_file, time_limit):
    start_time = time.time()

    try:
        result = subprocess.run(
            run_command,
            stdin=open(input_file, "r"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=time_limit,
            text=True
        )
    except subprocess.TimeoutExpired:
        print(f"❌ Time limit exceeded for {input_file}")
        return False

    execution_time = time.time() - start_time
    expected_output = open(expected_output_file).read().strip()
    actual_output = result.stdout.strip()

    if actual_output == expected_output:
        print(f"✅ Passed {input_file} in {execution_time:.2f} seconds")
        return True
    else:
        print(f"❌ Failed {input_file}. Expected {expected_output}, but got {actual_output}")
        return False

all_passed = all(run_test_case(tc[0], tc[1], tc[2]) for tc in test_cases)

if not all_passed:
    exit(1)
