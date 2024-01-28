import subprocess
import os
from tqdm import tqdm
import time

# file location
folder_path = "./assets/test_melanin"

# List all files in the folder
files = os.listdir(folder_path)

# Total number of iterations
total_iterations = len(files)

# Initialize the progress bar
progress_bar = tqdm(total=total_iterations, desc="Processing", unit="item")

# all img is 678
sec_index = 0
base_number = 3063
count_lose = 0
for file in files:
        print("Working on:",file)
        # First command
        inversion = "python src/inversion.py          --input_image \"assets/test_melanin/{}.jpg\"  --results_folder \"output/test_melanin\" ".format(int(file.replace('.jpg','')))
        result1 = subprocess.run(inversion, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Second command (will run after the first one finishes)   
        img2img = "python src/edit_real.py  --inversion \"output/test_melanin/inversion/{}.pt\" --prompt \"output/test_melanin/prompt/{}.txt\" --task_name \"b00012b0001\" --results_folder \"output/test_melanin/\" ".format(int(file.replace('.jpg','')),int(file.replace('.jpg','')))
        result2 = subprocess.run(img2img, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        #  Print results
        print("Command 1 Output:")
        print(result1.stdout)

        print("\nCommand 2 Output:")
        print(result2.stdout)
        
        # Update the progress bar
        progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# file_number = 0
# for number in range(677):
#     print("process on file number :",file_number+3063)
#     if (3063+file_number) != 3162 or (3063+file_number) != 3180 or (3063+file_number) != 3450 or (3063+file_number) != 3453 or (3063+file_number) != 3456 or (3063+file_number) != 3465 or (3063+file_number) != 3468 or (3063+file_number) != 3471 or (3063+file_number) != 3578:
#         # First command
#         inversion = "python src/inversion.py          --input_image \"assets/test_melanin/{}.jpg\"  --results_folder \"output/test_melanin\" ".format(3063+file_number)
#         result1 = subprocess.run(inversion, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#         # Second command (will run after the first one finishes)   
#         img2img = "python src/edit_real.py  --inversion \"output/test_melanin/inversion/{}.pt\" --prompt \"output/test_melanin/prompt/{}.txt\" --task_name \"b00012b0001\" --results_folder \"output/melanin/\" ".format(3063+number,3063+number)
#         result2 = subprocess.run(img2img, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#         #  Print results
#         print("Command 1 Output:")
#         print(result1.stdout)

#         print("\nCommand 2 Output:")
#         print(result2.stdout)
#     else :
#         print()    
#     file_number = file_number + 1
