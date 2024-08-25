import subprocess
import time

def run_exe_in_loop(exe_path, loop_delay):

    for iter in range(0, 30):
        try:
            print("Calling" + exe_path)
            subprocess.run(exe_path + " args=arg1", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running the executable: {e}")
        except KeyboardInterrupt:
            print("Exiting the loop.")
            break

        if loop_delay > 0 :
            time.sleep(loop_delay)

if __name__ == "__main__":
    exe_path = "test.exe"  # Replace with the path to your executable file
    loop_delay = 1  # Adjust the delay (in seconds) between each execution of the executable
    run_exe_in_loop(exe_path, loop_delay)