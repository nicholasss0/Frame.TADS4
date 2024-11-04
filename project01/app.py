import os
from tqdm import tqdm
import time


directory = os.listdir(r"C:\Users\nicho\OneDrive\Área de Trabalho\BDIgreja\pages")

print(directory)

# for item in tqdm(directory):
#     print(item)
#     time.sleep(2)

count = 0

while count < len(directory):
    print(directory[count])
    time.sleep(2)

    count += 1

    if count == len(tqdm(directory)) - 1:
        count = 0


