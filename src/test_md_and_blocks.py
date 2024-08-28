import unittest

from md_and_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_base_case(self):
        string = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected_result = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.assertEqual(expected_result, markdown_to_blocks(string))

    def test_white_spaces(self):
        string = "  # This is a heading\n\n  This is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected_result = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.assertEqual(expected_result, markdown_to_blocks(string))

    def test_extra_white_lines(self):
        string = "  # This is a heading\n\n\n  This is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected_result = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.assertEqual(expected_result, markdown_to_blocks(string))

    def test_extra_2_white_lines(self):
        string = "  # This is a heading\n\n\n\n  This is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected_result = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.assertEqual(expected_result, markdown_to_blocks(string))


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        valid_results = [
            "# Hello world",
            "## Hello world",
            "### Hello world",
            "#### Hello world",
            "##### Hello world",
            "###### Hello world",
        ]
        for result in valid_results:
            self.assertEqual(block_to_block_type(result), "heading")

        invalid_results = [
            "####### Hello world",
            "#Hello world",
            "# ",
        ]
        for result in invalid_results:
            self.assertEqual(block_to_block_type(result), "paragraph")

    def test_code(self):
        valid_results = [
            "```code```",
            "```hello world!```",
            "`````````", #still starts and ends with 3
            "``````", #still starts and ends with 3
            "``` hello ` world````"
        ]
        for result in valid_results:
            self.assertEqual(block_to_block_type(result), "code")

        invalid_results = [
            "```code``",
            "``code```",
            "` code `",
            "`````", #only 5 total
        ]
        for result in invalid_results:
            self.assertEqual(block_to_block_type(result), "paragraph")

    def test_quote(self):
        valid_results = [
            ">hello world",
            ">hello world\n>another line",
            ">hello world\n>another line\n>3lines",
            ">"
            ">   "
        ]
        for result in valid_results:
            self.assertEqual(block_to_block_type(result), "quote")

        invalid_results = [
            "not a quote",
            " >",
            ">hello\n>world\nquote"
        ]
        for result in invalid_results:
            self.assertEqual(block_to_block_type(result), "paragraph")

    def test_unordered_list(self):
        valid_results = [
            "* Item 1",
            "- Item 1",
            "* Item 1\n* Item 2",
            "- Item 1\n- Item 2\n- Item 3",
            "* Item 1\n* Item 2\n* Item 3\n* Item 4",
        ]
        for result in valid_results:
            self.assertEqual(block_to_block_type(result), "unordered_list")

        invalid_results = [
            "*Item 1",  # Missing space after asterisk
            "-Item 1",  # Missing space after dash
            "* Item 1\nNot a list item",  # Non-list item in the middle
            "  * Item 1",  # Indented asterisk
        ]
        for result in invalid_results:
        	self.assertEqual(block_to_block_type(result), "paragraph")

    def test_ordered_list(self):
        valid_results = [
            "1. Item 1",
            "1. Item 1\n2. Item 2",
            "1. Item 1\n2. Item 2\n3. Item 3",
            "1. Item 1\n2. Item 2\n3. Item 3\n4. Item 4",
        ]
        for result in valid_results:
            self.assertEqual(block_to_block_type(result), "ordered_list")

        invalid_results = [
            "1.Item 1",  # Missing space after period
            "1. Item 1\n3. Item 2",  # Non-sequential numbering
            "1. Item 1\n2. Item 2\nNot a list item",  # Non-list item in the middle
            " 1. Item 1",  # Indented number
            "01. Item 1",  # Leading zero
        ]
        for result in invalid_results:
            self.assertEqual(block_to_block_type(result), "paragraph")
