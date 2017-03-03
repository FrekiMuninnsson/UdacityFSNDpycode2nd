import os
def rename_files():
	# Get all the filenames from the folder in which the files reside.
	file_list = os.listdir(r"C:\Users\User\Desktop\Udacity FullStack Developer Nanodegree\Secret Message\to_be_renamed")
	print(file_list)
	saved_path = os.getcwd()
	print ("Current Working Directory is "+saved_path)
	os.chdir(r"C:\Users\User\Desktop\Udacity FullStack Developer Nanodegree\Secret Message\to_be_renamed")
	# For each file, rename it by removing the numbers from the filename.
	for file_name in file_list:
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
	
rename_files()
