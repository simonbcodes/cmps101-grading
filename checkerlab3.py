from subprocess import call
from shutil import copy
import os
import sys
import filecmp

root = "/home/simon/Desktop/grading"
requiredFiles = ["gettysburg.txt", "gettysburg-reversed.txt", "lab3-test.txt", "lab3-test-reversed.txt"]
wrong = 0

def gradeHW():
	os.chdir(sys.argv[1])
	fileExists("FileReverse.java")
	fileExists("Makefile")
	fileExists("README")
	os.chdir(root)
	copyFiles(sys.argv[1])
	print("navigating to " + sys.argv[1])
	os.chdir(sys.argv[1])
	print("running make")
	print("---")
	call(["make"])
	print("---")
	fileExists("FileReverse.jar")
	print("---")
	checkFile("gettysburg.txt", "gettysburg-reversed.txt", "FileReverse.jar")
	print("---")
	checkFile("lab3-test.txt", "lab3-test-reversed.txt", "FileReverse.jar")
	print("---")
	resultSummary()
	print("---")
	call(["make", "clean"])

def checkFile(testFile, solutionFile, jarName):
	print("checking " + jarName + " on lab3-test.txt")
	call(["java", "-jar", jarName, testFile, "out.txt"])
	print("---")
	if(os.path.exists("out.txt")):
		print("✓ [out.txt properly created]")
		call(["cat", "out.txt"])
	else:
		print("✗ [out.txt not properly created]")
		wrong += 1
	print("---")
	call(["cat", solutionFile])
	if(filecmp.cmp("out.txt", solutionFile)):
		print("✓ [" + solutionFile + " solutions match]")
	else:
		print("✗ [" + solutionFile + " solutions do not match]")
		wrong += 1
	call(["rm", "out.txt"])

def fileExists(testFile):
	if(os.path.exists(testFile)):
		print("✓ [" + testFile + " submitted]")
	else:
		print("✗ [" + testFile + " not submitted or improperly named]")
		wrong += 1

def copyFiles(directory):
	print("copying files into " + directory)
	for f in requiredFiles:
		copy(f, directory)

def resultSummary():
	if(wrong > 0):
		print(str(wrong) + " problems found in your code")
	else:
		print("No problems found. You're great, you know that?")

gradeHW();
