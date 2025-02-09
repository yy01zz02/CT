second_last_file = p.readline();
last_file = p.readline();

column_end = last_file[0:4]
row_end = second_last_file[5:9]

print column_end
print row_end

os.system('rm ' + column_end + '*');
os.system('rm *-' + row_end + '.jpg');

column_end = int(column_end) - 1000;
row_end = int(row_end) - 1000;

os.system('mkdir temp')

i = 0;
for r in range(0, row_end):
	for c in range(0, column_end):