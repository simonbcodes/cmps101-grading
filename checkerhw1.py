from subprocess import call
import os
import sys
import filecmp

def gradeHW():
	wrong = 0;
	print("navigating to " + sys.argv[1])
	os.chdir(sys.argv[1])
	print("running make")
	print("---")
	call(["make"])
	print("---")

	if(os.path.exists("NQueens.jar")):
		print("✓ [NQueens.jar properly created]")
	else:
		print("✗ [NQueens.jar not properly created]")
		wrong += 1;
		#raise Warning("NQueens.jar not found after running make")
	print("---")
	print("running NQueens.jar")
	call(["java", "-jar", "NQueens.jar", "in.txt", "solution.txt"])
	print("---")
	if(os.path.exists("solution.txt")):
		print("✓ [solution.txt properly created]")
		call(["cat", "solution.txt"])
	else:
		print("✗ [solution.txt not properly created]")
		wrong += 1;
		#raise Warning("solution.txt not properly created after running NQueens.jar")
	print("---")
	print("running NQueens.jar with test-input.txt")
	call(["java", "-jar", "NQueens.jar", "test-input.txt", "test-output1.txt"])
	print("--test-output.txt--")
	call(["cat", "test-output.txt"])
	print("--test-output1.txt--")
	call(["cat", "test-output1.txt"])
	if(filecmp.cmp("test-output.txt", "test-output1.txt")):
		print("✓ [test-input.txt solutions match]")
	else:
		print("✗ [test-input.txt solutions do not match]")
		wrong += 1;
		#raise Warning("test-input.txt solutions do not match")
	call(["rm", "test-output1.txt"])
	print("---")
	print("running NQueens.jar with more-input.txt")
	call(["java", "-jar", "NQueens.jar", "more-input.txt", "more-output1.txt"])
	print("--more-output.txt--")
	call(["cat", "more-output.txt"])
	print("--more-output1.txt--")
	call(["cat", "more-output1.txt"])
	if(filecmp.cmp("more-output.txt", "more-output1.txt")):
		print("✓ [more-input.txt solutions match]")
	else:
		print("✗ more-input.txt solutions do not match")
		wrong += 1;
		#raise Warning("more-input.txt solutions do not match")
	call(["rm", "more-output1.txt"])
	print("---")
	if(wrong > 0):
		print(str(wrong) + " problems found in your code")
	else:
		print("No problems found. Good job!")
	print("---")
	call(["make", "clean"])
	print("---")
	os.chdir("/home/simon/Desktop/grading")
	with open("grades.txt", "a") as grades:
		ids = sys.argv[1].split("/")
		grades.write(ids[1] + " " + str(wrong) + "\n")

gradeHW()
