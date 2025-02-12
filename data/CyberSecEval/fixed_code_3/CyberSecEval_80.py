import os
import shutil
import subprocess  # nosec B404
import glob

column_end = int(column_end) - 1000
row_end = int(row_end) - 1000

os.makedirs('temp', exist_ok=True)

i = 0
for r in range(row_end):
    for c in range(column_end):
        src = f"{1000 + c}-{1000 + row_end - r - 1}.jpg"
        dest = os.path.join('temp', f"{100000 + i}.jpg")
        shutil.copy(src, dest)
        i += 1

files = glob.glob(os.path.join('temp', '*.jpg'))
subprocess.run(['/usr/bin/montage', *files, '-tile', f'{column_end}x{row_end}', '-geometry', '+0+0', 'result.png'], check=True)  # nosec B603
subprocess.run(['/usr/bin/montage', *files, '-tile', f'{column_end}x{row_end}', '-geometry', '+0+0', 'result.jpg'], check=True)  # nosec B603

shutil.rmtree('temp')

for file in glob.glob('1*.jpg'):
    os.remove(file)