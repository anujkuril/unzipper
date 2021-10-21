#!/usr/bin/python3

import os
import zipfile


password = str(input("input if any password:"))
directory = str(input("directory of zip files:"))
cwd = os.getcwd()
files_list = os.listdir(directory)
# password = "crackmes.one"

def ext():


	print('[+]files names')
	for item in files_list:
		print(item)

	print('\n')

	print("[+]creating destination folder")
	dir_name = "unzipedFiles"
	os.mkdir(directory+dir_name)
	print(f"[+]directory created: {dir_name}")

	print("\n")

	print("[+]extracting files.....")

	print('\n')

	for item in files_list:
	
		if zipfile.is_zipfile(item)==True:
			try:	
				with zipfile.ZipFile(item,"r") as z:
					output_path = os.path.join(cwd,"unzipedFiles")
					print(f"[+]extracting:{item}")
					z.setpassword(pwd = bytes(password, 'utf-8'))
					z.extractall("unzipedFiles")
					print(z.infolist())
					print(f"[+]extracted:{item}")
					print('\n')
			except zipfile.BadZipfile:
				print(f"cannot extract{item}: not a valid zip")
				print('\n')


	print('\n')

	path = os.path.join(cwd,"unzipedFiles")
	unzipped_files_list = os.listdir(path)
	no_of_files = len(unzipped_files_list)
	print(f"[+]number of extracted files: {no_of_files}")
	print("[+]list of extracted items")
	for item in unzipped_files_list:
		print(item)

ext()