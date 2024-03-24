import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
        
    def test_to_leaf(self):
        node = LeafNode(
            "p",
            "This is a paragraph of text.",
        )
        self.assertEqual(
            repr(node),
            '"p", "This is a paragraph of text."',
        )


    # def test_eq_false(self):
    #     node = HTMLNode("This is a text node", text_type_text)
    #     node2 = HTMLNode("This is a text node", text_type_bold)
    #     self.assertNotEqual(node, node2)

    # def test_eq_false2(self):
    #     node = HTMLNode("This is a text node", text_type_text)
    #     node2 = HTMLNode("This is a text node2", text_type_text)
    #     self.assertNotEqual(node, node2)

    # def test_eq_url(self):
    #     node = HTMLNode("This is a text node", text_type_italic, "https://www.boot.dev")
    #     node2 = HTMLNode(
    #         "This is a text node", text_type_italic, "https://www.boot.dev"
    #     )
    #     self.assertEqual(node, node2)

    # def test_repr(self):
    #     node = HTMLNode("This is a text node", text_type_text, "https://www.boot.dev")
    #     self.assertEqual(
    #         "HTMLNode(This is a text node, text, https://www.boot.dev)", repr(node)
    #     )


if __name__ == "__main__":
    unittest.main()

        