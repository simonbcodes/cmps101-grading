from subprocess import call
from shutil import copy
import os
import sys
import filecmp

def gradeHW():
	wrong = 0
	print("copying files into " + sys.argv[1])
	copy("check_attack.txt", sys.argv[1])
	copy("check_attack_solution.txt", sys.argv[1])
	copy("check_king_validity.txt", sys.argv[1])
	copy("check_king_validity_solution.txt", sys.argv[1])
	copy("check_piece_position.txt", sys.argv[1])
	copy("check_piece_position_solution.txt", sys.argv[1])
	copy("test-input.txt", sys.argv[1])
	copy("test-output.txt", sys.argv[1])
	copy("more-input.txt", sys.argv[1])
	copy("more-output.txt", sys.argv[1])
	print("---")
	print("navigating to " + sys.argv[1])
	os.chdir(sys.argv[1])
	print("running make")
	print("---")
	call(["make"])

	print("---")
	if(os.path.exists("ChessBoard.jar")):
		print("✓ [ChessBoard.jar properly created]")
	else:
		print("✗ [ChessBoard.jar not properly created]")
		wrong += 1;

	print("checking attacks")
	call(["java", "-jar", "ChessBoard.jar", "check_attack.txt", "out.txt"])
	print("---")
	if(os.path.exists("out.txt")):
		print("✓ [out.txt properly created]")
		call(["cat", "out.txt"])
	else:
		print("✗ [out.txt not properly created]")
		wrong += 1;
	print("---")
	call(["cat", "check_attack_solution.txt"])
	if(filecmp.cmp("out.txt", "check_attack_solution.txt")):
		print("✓ [check_attack_solution.txt solutions match]")
	else:
		print("✗ [check_attack_solution.txt solutions do not match]")
		wrong += 1;
	call(["rm", "out.txt"])

	print("checking king validity")
	call(["java", "-jar", "ChessBoard.jar", "check_king_validity.txt", "out.txt"])
	print("---")
	if(os.path.exists("out.txt")):
		print("✓ [out.txt properly created]")
		call(["cat", "out.txt"])
	else:
		print("✗ [out.txt not properly created]")
		wrong += 1;
	print("---")
	call(["cat", "check_king_validity_solution.txt"])
	if(filecmp.cmp("out.txt", "check_king_validity_solution.txt")):
		print("✓ [check_king_validity_solution.txt solutions match]")
	else:
		print("✗ [check_king_validity_solution.txt solutions do not match]")
		wrong += 1;
	call(["rm", "out.txt"])

	print("checking piece positions")
	call(["java", "-jar", "ChessBoard.jar", "check_piece_position.txt", "out.txt"])
	print("---")
	if(os.path.exists("out.txt")):
		print("✓ [out.txt properly created]")
		call(["cat", "out.txt"])
	else:
		print("✗ [out.txt not properly created]")
		wrong += 1;
	print("---")
	call(["cat", "check_piece_position_solution.txt"])
	if(filecmp.cmp("out.txt", "check_piece_position_solution.txt")):
		print("✓ [check_piece_position_solution.txt solutions match]")
	else:
		print("✗ [check_piece_position_solution.txt solutions do not match]")
		wrong += 1;
	call(["rm", "out.txt"])

	call(["java", "-jar", "ChessBoard.jar", "test-input.txt", "test-out.txt"])
	print("---")
	if(os.path.exists("test-out.txt")):
		print("✓ [test-out.txt properly created]")
		call(["cat", "test-out.txt"])
	else:
		print("✗ [test-out.txt not properly created]")
		wrong += 1;
	print("---")
	call(["cat", "test-output.txt"])
	if(filecmp.cmp("test-out.txt", "test-output.txt")):
		print("✓ [test-output.txt solutions match]")
	else:
		print("✗ [test-output.txt solutions do not match]")
		wrong += 1;
	call(["rm", "test-out.txt"])

	call(["java", "-jar", "ChessBoard.jar", "more-input.txt", "more-out.txt"])
	print("---")
	if(os.path.exists("more-out.txt")):
		print("✓ [more-out.txt properly created]")
		call(["cat", "more-out.txt"])
	else:
		print("✗ [more-out.txt not properly created]")
		wrong += 1
	print("---")
	call(["cat", "more-output.txt"])
	if(filecmp.cmp("more-out.txt", "more-output.txt")):
		print("✓ [more-output.txt solutions match]")
	else:
		print("✗ [more-output.txt solutions do not match]")
		wrong += 1;
	call(["rm", "more-out.txt"])
	print("---")

	if(os.path.exists("README")):
		print("✓ [README exists]")
		call(["cat", "README"])
	else:
		print("✗ [README does not exist]")
		wrong += 1

	print("\n---")
	print("cleaning out test files")
	call(["rm", "check_attack.txt"])
	call(["rm", "check_attack_solution.txt"])
	call(["rm", "check_king_validity.txt"])
	call(["rm", "check_king_validity_solution.txt"])
	call(["rm", "check_piece_position.txt"])
	call(["rm", "check_piece_position_solution.txt"])
	call(["rm", "test-input.txt"])
	call(["rm", "test-output.txt"])
	call(["rm", "more-input.txt"])
	call(["rm", "more-output.txt"])
	print("---")
	print("cleaning out with make")
	call(["make", "clean"])
	print("---")
	if(wrong > 0):
		print(str(wrong) + " problems found in your code")
	else:
		print("No problems found. You're literally my favorite person right now")

gradeHW()
