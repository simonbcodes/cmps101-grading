from subprocess import call
from shutil import copy
import os
import sys
import filecmp

root = "/home/simon/Desktop/grading"
requiredFiles = ["more-input.txt", "more-output.txt", "test-input.txt", "test-output.txt"]
students = ["abnewcom", "aguizaro", "airparke", "anacampo", "bmungoza", "bxwong", "catlle", "corymart", "cyang52", "ddrichar", "dgkronen", "djhui", "gmcneill", "gmein", "gvandesa", "hyuan3", "ivanstee", "jesales", "kajemart", "lbattell", "liluu", "mhshinne", "mrkumar", "rxiao3", "swoolled", "vsanfeli"]
wrong = 0

def grade(flag):
	if "-s" in flag:
		if len(sys.argv) > 2:
			paths = lookForDirectory("hw3/" + sys.argv[2], "hw3")
			print(paths[0])
			gradeStudent(paths[0])
		else:
			print("Usage: checkerhw3.py -s hw3/studentDirectory")

def gradeAll():
	global wrong
	F = open("gradeshw3.txt", "w")
	paths = lookForDirectory("hw3", "hw3")
	for student in paths:
		if student != "hw3":
			print(student.split("/")[1])
			gradeStudent(student)
			F.write(student.split("/")[1] + " " + str(wrong) + "\n")
			wrong = 0

def lookForDirectory(startDirectory, name):
	paths = []
	for directory in os.walk(startDirectory):
		#print(directory)
		if directory[0][-3:].lower() == name:
			paths.append(directory[0])
	return paths

def gradeStudent(path):
	global wrong
	os.chdir(path)
	if fileExists("Makefile") and fileExists("README"):
		os.chdir(root)
		copyFiles(path)
		print("navigating to " + path)
		os.chdir(path)
		call(["make", "clean"])
		print("running make")
		print("---")
		call(["make"])
		print("---")
		if fileExists("Balanced.jar"):
			print("---")
			checkFile("more-input.txt", "more-output.txt", "Balanced.jar")
			print("---")
			checkFile("test-input.txt", "test-output.txt", "Balanced.jar")
			print("---")
			resultSummary()
			print("---")
			call(["make", "clean"])
	os.chdir(root)

def checkFile(testFile, solutionFile, jarName):
	global wrong
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
	global wrong
	if(os.path.exists(testFile)):
		print("✓ [" + testFile + " submitted]")
	else:
		print("✗ [" + testFile + " not submitted or improperly named]")
		wrong += 1
	return os.path.exists(testFile)

def copyFiles(directory):
	print("copying files into " + directory)
	for f in requiredFiles:
		copy(f, directory)

def resultSummary():
	global wrong
	if(wrong > 0):
		print(str(wrong) + " problems found in your code")
	else:
		print("No problems found. You're great, you know that?")

grade(sys.argv[1])
