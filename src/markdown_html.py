from htmlnode import ParentNode, LeafNode
from markdown_block import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in text_nodes]


def paragraph_to_html_node(block):
    lines = block.split("\n")
    text = " ".join(line.strip() for line in lines)
    return ParentNode("p", text_to_children(text))


def heading_to_html_node(block):
    level = 0
    for ch in block:
        if ch == "#":
            level += 1
        else:
            break
    text = block[level + 1:]
    return ParentNode(f"h{level}", text_to_children(text))


def code_to_html_node(block):
    lines = block.split("\n")
    content = "\n".join(lines[1:-1]) + "\n"
    code_node = LeafNode("code", content)
    return ParentNode("pre", [code_node])


def quote_to_html_node(block):
    lines = block.split("\n")
    stripped = []
    for line in lines:
        if line.startswith("> "):
            stripped.append(line[2:])
        elif line.startswith(">"):
            stripped.append(line[1:])
        else:
            stripped.append(line)
    text = " ".join(stripped)
    return ParentNode("blockquote", text_to_children(text))


def ulist_to_html_node(block):
    items = []
    for line in block.split("\n"):
        items.append(ParentNode("li", text_to_children(line[2:])))
    return ParentNode("ul", items)


def olist_to_html_node(block):
    items = []
    for i, line in enumerate(block.split("\n"), 1):
        text = line[len(f"{i}. "):]
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", items)


def block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    raise ValueError(f"unknown block type: {block_type}")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = [block_to_html_node(b, block_to_block_type(b)) for b in blocks]
    return ParentNode("div", block_nodes)
