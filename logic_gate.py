#! /usr/bin/python
import sys

try:
	print '''--------------------------------------------------------
|    _                 _        _____       _          |
|   | |               (_)      |  __ \     | |         |
|   | |     ___   __ _ _  ___  | |  \/ __ _| |_ ___    |
|   | |    / _ \ / _` | |/ __| | | __ / _` | __/ _ \   | 
|   | |___| (_) | (_| | | (__  | |_\ \ (_| | ||  __/   |
|   \_____/\___/ \__, |_|\___|  \____/\__,_|\__\___|   |
|                 __/ |                                |
|                |___/               Created by DS     |
|                                                      |
--------------------------------------------------------'''
 	# Awal
 	print("|-   Logic Gate Math   -|")
 	print("-------------------------")
 	print("1. AND\n2. OR\n3. NOT\n4. NAND\n5. NOR\n6. XOR\n7. NXOR")
 	print("-------------------------")
 	logicgate = raw_input("Pilih Gerbang Logika : ")
 	print("-------------------------")
 	# Input number A and B
 	a = raw_input("Input angka A : ")
 	b = raw_input("Input angka B : ")
 	print("-------------------------")

 	# Check Logic Gate
 	if logicgate.isdigit():
 		# AND
 		if logicgate == "1":
 			# Calculating
 			if (a.isdigit() and b.isdigit()):
 				if (a == "1" and b == "1"):
 					hasil = "1"
 				else:
 					hasil = "0"
 				print("Hasil : "+hasil)
 				print("---------------------")
 			else:
 				print("A or B is not number")
 				print("---------------------")
 		# OR
 		elif logicgate == "2":
 			# Calculating
 			if (a.isdigit() and b.isdigit()):
 				if (a == "1" or b == "1"):
 					hasil = "1"
 				else:
 					hasil = "0"
 				print("Hasil : "+hasil)
 				print("---------------------")
 			else:
 				print("A or B is not number")
 				print("---------------------")
 		# NOT
 		elif logicgate == "3":
 			# Calculating
 			if (a.isdigit() or b.isdigit()):
 				if (a == "1" or b == "1"):
 					hasil = "0"
 				else:
 					hasil = "1"
 				print("Hasil : "+hasil)
 				print("---------------------")
 			else:
 				print("A or B is not number")
 				print("---------------------")
 		# NAND
 		elif logicgate == "4":
 			# Calculating
 			if (a.isdigit() and b.isdigit()):
 				if (a == "1" and b == "1"):
 					hasil = "0"
 				else:
 					hasil = "1"
 				print("Hasil : "+hasil)
 				print("---------------------")
 			else:
 				print("A or B is not number")
 				print("---------------------")
 		# NOR
 		elif logicgate == "5":
 			# Calculating
 			if (a.isdigit() and b.isdigit()):
 				if (a == "1" or b == "1"):
 					hasil = "0"
 				else:
 					hasil = "1"
 				print("Hasil : "+hasil)
 				print("---------------------")
 			else:
 				print("A or B is not number")
 				print("---------------------")
 		# XOR
 		elif logicgate == "6":
 			# Calculating
 			if (a.isdigit() and b.isdigit()):
 				if (a == "1" and b == "1" or a == "0" and b == "0"):
 					hasil = "0"
 				else:
 					hasil = "1"
 				print("Hasil : "+hasil)
 				print("---------------------")
 			else:
 				print("A or B is not number")
 				print("---------------------")
 		# NXOR
 		elif logicgate == "7":
 			# Calculating
 			if (a.isdigit() and b.isdigit()):
 				if (a == "1" and b == "1" or a == "0" and b == "0"):
 					hasil = "1"
 				else:
 					hasil = "0"
 				print("Hasil : "+hasil)
 				print("---------------------")
 			else:
 				print("A or B is not number")
 				print("---------------------")
 		elif logicgate < 1:
 			print("Choose number 1 - 7 Logic Gate")
 		elif logicgate > 7:
 			print("Choose number 1 - 7 Logic Gate")
 	else:
 		print("Choose Logic Gate with number")
except KeyboardInterrupt:
	print("Exit now ...")
	sys.exit()