def extract_title(markdown_file):
	blocks = markdown_to_blocks(markdown_file)
	header_block = blocks[0]

	stripped_header = header_block.strip()
	if not (stripped_header[0] == "#" and stripped_header[1] == " "):
		raise Exception("content provided was not a h1 header")
	return stripped_header[2:]



def markdown_to_blocks(markdown):
	blocks = markdown.split("\n\n")
	cleaned_blocks = []


	for block in blocks:
		block = block.strip()
		if not block == "":
			cleaned_blocks.append(block)

	return cleaned_blocks


def block_to_block_type(block):
	lines = block.split("\n")


	hashtag_counter = 0
	for char in block:
		if char == "#":
			hashtag_counter += 1
		elif char == " ":
			if hashtag_counter >= 1 and hashtag_counter <= 6:
				if len(block) >= hashtag_counter + 2:
					return "heading"
			else:
				break
		else:
			break


	if len(block) >= 6 and block[0] == "`" and block[1] == "`" and block[2] == "`" and block[-1] == "`" and block[-2] == "`" and block[-3] == "`":
		return "code"

	
	good_lines_counter = 0
	for line in lines:
		if line[0] == ">":
			if good_lines_counter + 1 == len(lines):
				return "quote"
			good_lines_counter += 1
		else:
			break


	good_lines_counter = 0
	for line in lines:
		if (line[0] == "*" or line[0] == "-") and (line[1] == " "):
			if good_lines_counter + 1 == len(lines):
				return "unordered_list"
			good_lines_counter += 1
		else:
			break



	current_num = 1
	for line in lines:
		if line[0] == str(current_num) and line[1] == "." and line[2] == " ":
			if current_num == len(lines):
				return "ordered_list"
			current_num += 1
		else:
			break


	return "paragraph"







