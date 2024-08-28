import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_props_to_html(self):
		my_prop = { "href": "https://www.google.com", "target": "_blank"}
		my_node = HTMLNode("p", "hello, world!", None, my_prop)

		expected_result = " href='https://www.google.com' target='_blank'"

		self.assertEqual(my_node.props_to_html(), expected_result)

		my_node2 = HTMLNode("p", "hello, world!", None, None)

		self.assertEqual(my_node2.props_to_html(), "")

	def test_repr(self):
		my_node = HTMLNode("p", "hello, world!", None, None)
		expected_result = "HTMLNode(p, hello, world!, None, None)"
		actual_result = repr(my_node)

		self.assertEqual(expected_result, actual_result)


class TestLeafNode(unittest.TestCase):
	def test_to_html(self):
		#Normal examples
		my_prop = {"href": "https://www.google.com"}
		my_node = LeafNode("a", "Click me!", my_prop)
		expected_result = "<a href='https://www.google.com'>Click me!</a>"
		self.assertEqual(expected_result, my_node.to_html())

		my_node2 = LeafNode("p", "This is a paragraph of text.")
		expected_result = "<p>This is a paragraph of text.</p>"
		self.assertEqual(expected_result, my_node2.to_html())

		#Tag being None
		my_node4 = LeafNode(None, "Click me!", my_prop)
		self.assertEqual("Click me!", my_node4.to_html())

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
