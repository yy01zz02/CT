import os
import shutil
import subprocess
from glob import glob

column_end = int(column_end) - 1000
row_end = int(row_end) - 1000

os.makedirs('temp', exist_ok=True)

i = 0
for r in range(row_end):
    for c in range(column_end):
        file_to_move = f"{1000 + c}-{1000 + row_end - r - 1}.jpg"
        dest = os.path.join('temp', f"{100000 + i}.jpg")
        shutil.copy(file_to_move, dest)
        i += 1

jpg_files = sorted(glob(os.path.join('temp', '*.jpg')))
subprocess.run(['montage', '--'] + jpg_files + ['-tile', f'{column_end}x{row_end}', '-geometry', '+0+0', 'result.png'], check=True)
subprocess.run(['montage', '--'] + jpg_files + ['-tile', f'{column_end}x{row_end}', '-geometry', '+0+0', 'result.jpg'], check=True)

shutil.rmtree('temp')

for file in glob('1*.jpg'):
    os.remove(file)