from subprocess import call
from shutil import copy
import os
import sys
import filecmp

root = "/home/simon/Desktop/grading"
requiredFiles = ["input.txt", "correct_analysis.txt", "Shakespeare.txt"]
students = ["abnewcom", "aguizaro", "airparke", "anacampo", "bmungoza", "bxwong", "catlle", "corymart", "cyang52", "ddrichar", "dgkronen", "djhui", "gmcneill", "gmein", "gvandesa", "hyuan3", "ivanstee", "jesales", "kajemart", "lbattell", "liluu", "mhshinne", "mrkumar", "rxiao3", "swoolled", "vsanfeli"]
wrong = 0

def grade(flag, assignment):
	if "-s" in flag:
		if len(sys.argv) > 2:
			paths = lookForDirectory(assignment + "/" + sys.argv[2], assignment)
			print(assignment + "/" + sys.argv[2])
			print(paths[0])
			gradeStudent(paths[0])
		else:
			print("Usage: checker" + assignment + ".py -s " + assignment +"/studentDirectory")

def gradeAll():
	global wrong
	F = open("gradeslab4.txt", "w")
	paths = lookForDirectory("lab4", "lab4")
	for student in paths:
		if student != "lab4":
			print(student.split("/")[1])
			gradeStudent(student)
			F.write(student.split("/")[1] + " " + str(wrong) + "\n")
			wrong = 0

def lookForDirectory(startDirectory, name):
	paths = []
	for directory in os.walk(startDirectory):
		#print(directory)
		if directory[0][-len(name):].lower() == name:
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
		if fileExists("Bard.jar"):
			print("---")
			checkJavaFile("input.txt", "correct_analysis.txt", "Bard.jar")
			print("---")
			resultSummary()
			print("---")
			call(["make", "clean"])
	os.chdir(root)

def checkCFile(testFile, solutionFile, cExecName):
	global wrong
	print("checking " + cExecName + " on " + testFile)
	call(["./" + cExecName, testFile, "out.txt"])
	print("---")
	if(os.path.exists("analysis.txt")):
		print("✓ [analysis.txt properly created]")
		call(["cat", "analysis.txt"])
	else:
		print("✗ [out.txt not properly created]")
		wrong += 1
	print("---")
	call(["cat", solutionFile])
	if(filecmp.cmp("analysis.txt", solutionFile)):
		print("✓ [" + solutionFile + " solutions match]")
	else:
		print("✗ [" + solutionFile + " solutions do not match]")
		# call(["diff", solutionFile, "out.txt"])
		wrong += 1
	call(["rm", "analysis.txt"])

def checkJavaFile(testFile, solutionFile, jarName):
	global wrong
	print("checking " + jarName + " on " + testFile)
	call(["java", "-jar", jarName, testFile, "analysis.txt"])
	print("---")
	if(os.path.exists("analysis.txt")):
		print("✓ [analysis.txt properly created]")
		call(["cat", "analysis.txt"])
	else:
		print("✗ [analysis.txt not properly created]")
		wrong += 1
	print("---")
	if(filecmp.cmp("analysis.txt", solutionFile)):
		print("✓ [" + solutionFile + " solutions match]")
	else:
		print("✗ [" + solutionFile + " solutions do not match]")
		call(["cat", solutionFile])
		print("---")
		call(["diff", "analysis.txt", solutionFile])
		wrong += 1
	call(["rm", "analysis.txt"])

def memCheck(exec, inputFile, outputFile):
	call(["valgrind", "--leak-check=full", exec, inputFile, outputFile])

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
	if(wrong > 1):
		print(str(wrong) + " problems found in your code")
	elif(wrong == 1):
		print(str(wrong) + " problem found in your code")
	else:
		print("You're a wizard, my god")

grade(sys.argv[1], "hw5")
