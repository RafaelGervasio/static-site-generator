import os
from markdown_to_html_node import markdown_to_html_node
from md_and_blocks import extract_title

def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	with open(from_path, "r") as md_file:
		md_doc = md_file.read()

	with open(template_path, "r") as template_file:
		template_doc = template_file.read()

	html_node = markdown_to_html_node(md_doc)
	html_content = html_node.to_html()
	page_title = extract_title(md_doc)

	
	# print(page_title)


	filled_template = template_doc.replace("{{ Title }}", page_title)
	filled_template = filled_template.replace("{{ Content }}", html_content)
	
	# print(filled_template)

	
	filename = "index.html"
	file_path = f"{dest_path}/{filename}"

	if os.path.exists(dest_path):
		with open(file_path, "w") as file:
			file.write(filled_template)

	else:
		os.makedirs(dest_path)
		with open(file_path, "w") as file:
			file.write(filled_template)





def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	if os.path.isfile(dir_path_content):
		generate_page(dir_path_content, template_path, dest_dir_path)
	else:
		if not os.path.exists(dest_dir_path):
			os.makedirs(dest_dir_path)

		# Process each item in the directory
		contents = os.listdir(dir_path_content)
		for content in contents:
			content_full_path = os.path.join(dir_path_content, content)
			dest_full_path = os.path.join(dest_dir_path, content)

			if os.path.isfile(content_full_path):
				generate_page(content_full_path, template_path, dest_dir_path)
			else:
				generate_pages_recursive(content_full_path, template_path, dest_full_path)

