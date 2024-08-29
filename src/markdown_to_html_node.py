from md_and_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from inline import text_to_textnodes
from textnode import text_node_to_html_node


def type_of_block_to_tag(type_of_block):
	tags = {
		"quote": "blockquote",
		"unordered_list": "ul",
		"ordered_list": "ol",
		"code": "code",
		"paragraph": "p"
	}
	return tags.get(type_of_block, None)

def heading_type_to_tag(block):
	hashtag_counter = 0
	for char in block:
		if char == "#":
			hashtag_counter += 1
		else:
			break
	return f"h{hashtag_counter}"



def markdown_to_html_node(markdown_doc):
	blocks = markdown_to_blocks(markdown_doc)	
	all_nodes = []
	
	for block in blocks:
		type_of_block = block_to_block_type(block)

		if type_of_block == "heading":
			tag = heading_type_to_tag(block)
		else:
			tag = type_of_block_to_tag(type_of_block)

		content = block.lstrip('#').strip() if type_of_block == "heading" else block

		if tag in ["ol", "ul"]:
			li_nodes = []
			list_items = content.split("\n")
			for list_item in list_items:
				li_node = ParentNode("li", li_to_text(list_item), None)
				li_nodes.append(li_node)
			node = ParentNode(tag, li_nodes, None)
			all_nodes.append(node)
		else:
			node = ParentNode(tag, text_to_children(content), None)
			all_nodes.append(node)


	div_parent = ParentNode("div", all_nodes)
	return div_parent	




def li_to_text(li):
	if li[0] in ["*", "-"]:
		stripped_li = li[2:]
	else:
		stripped_li = li[3:]

	nodes = text_to_textnodes(stripped_li)
	html_nodes = []
	for node in nodes:
		html_nodes.append(text_node_to_html_node(node))

	return html_nodes


		
def text_to_children(text):
	nodes = text_to_textnodes(text)
	html_nodes = []
	for node in nodes:
		html_nodes.append(text_node_to_html_node(node))

	return html_nodes



		


# def __init__(self, tag=None, value=None, children=None, props=None):