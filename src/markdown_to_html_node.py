from md_and_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from inline import text_to_textnodes

def type_of_block_to_tag(type_of_block):
	if type_of_block == "quote":
		return "<blockquote>"
	elif type_of_block == "unordered_list":
		return "<ul>"
	elif type_of_block == "ordered_list":
		return "<ol>"
	elif type_of_block == "code":
		return "<code>"
	elif type_of_block == "paragraph":
		return "<p>"




def markdown_to_html_node(markdown_doc):
	blocks = markdown_to_blocks(markdown_doc)

	all_nodes = []
	
	for block in blocks:
		type_of_block = block_to_block_type(block)
		def heading_type_to_tag(block):
			hashtag_counter = 0
			for char in block:
				if char == "#":
					hashtag_counter += 1
				else:
					break
			return f"h{hashtag_counter}"

		if type_of_block == "heading":
			tag = heading_type_to_tag(block)
		else:
			tag = type_of_block_to_tag(type_of_block)

		
		node = ParentNode(tag, text_to_children(block), None)
		all_nodes.append(node)


	div_parent = ParentNode("div", all_nodes)
	return div_parent	






		
def text_to_children(text):
	nodes = text_to_textnodes(text)
	html_nodes = []
	for node in nodes:
		html_nodes.append(text_node_to_html_node(node))

	return html_nodes



		


# def __init__(self, tag=None, value=None, children=None, props=None):