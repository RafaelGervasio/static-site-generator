class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("Not implemented yet")

	def props_to_html(self):
		final_string = ""

		if self.props is None:
			return final_string

		for key, value in self.props.items():
			final_string += " " + key + "=" + "'" + value + "'"
		return final_string

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None):
		super().__init__(tag=tag, value=value, children=None, props=props)

	def to_html(self):
		if self.value == None:
			raise ValueError("Leaf node has no value")
		if self.tag == None:
			return self.value

		return f'<{self.tag}' + f"{self.props_to_html()}" + ">" + f"{self.value}" + f"</{self.tag}>"


class ParentNode(HTMLNode):
	def __init__(self, tag=None, children=None, props=None):
		super().__init__(tag=tag, value=None, children=children, props=props)

	def to_html(self):
		if self.tag == None:
			raise ValueError("Parent node has no tag")
		if self.children is None:
			raise ValueError("Parent node has no children")

		html_output = f'<{self.tag}' + f"{self.props_to_html()}" + ">"
		
		html_of_children = ""
		for child in self.children:
			html_of_children += child.to_html()

		html_output += html_of_children + f"</{self.tag}>"

		return html_output



