import os
import shutil


def copy_contents(source, destination):
	if os.path.exists(destination) == False:
		print(os.path.abspath(destination))
		raise Exception("Path doesn't exist.")
	else:		
		shutil.rmtree(f'{destination}')
		os.mkdir(f"{destination}")

		contents_in_source = os.listdir(os.path.abspath(source))

		for content in contents_in_source:
			# print(content)
			source_path = f"{source}/{content}"

			if os.path.isfile(source_path):
				# print("I'm a file")
				shutil.copy(source_path, destination)
			else:
				# print("I'm not a file -> recursive call")
				os.mkdir(f"{destination}/{content}")

				new_destination = f"{destination}/{content}"
				copy_contents(source_path, new_destination)



copy_contents("static", "public")