
# coding: utf-8

# # Huffman Encoding and Decoding
# 
# by Youn-Long Lin, Department of Computer Science, National Tsing Hua University

# In[2]:

# Key for sorting a list of tuples
def getKey(item):
    return item[0]

# Construct a huffman tree according to the frequency of chars of the text
def gen_huffman_tree(text):
    text_list = [c for c in text]
    alphabet = set(text_list)
    h_tree = [ (text_list.count(c), (c, ) ) for c in alphabet ]
    while len(h_tree) >= 2:
        h_tree = sorted(h_tree, key=getKey)
        h_tree = [ (h_tree[0][0] + h_tree[1][0], (h_tree[0], h_tree[1])) ] + h_tree[2:]
    return h_tree

# Build Huffman dictionary out of a Huffman tree
def gen_huffman_dict(h_tree_node, code, h_dict):
    if len(h_tree_node[1]) == 1:
        h_dict[h_tree_node[1][0]] = code
    else:
        gen_huffman_dict(h_tree_node[1][0], code+'0', h_dict)
        gen_huffman_dict(h_tree_node[1][1], code+'1', h_dict)
    return

# Encode a text message according to a Huffman dictionary
def huffman_enc(h_dict, text):
    h_code = ''
    for c in text:
        h_code = h_code + h_dict[c]
    return h_code

# Decode a bit stream following a Huffman tree
def huffman_dec(h_tree, h_code):
    dec_text = ''
    i = 0
    while i < len(h_code):
        cur_node = h_tree[0]
        while len(cur_node[1]) == 2:
            cur_node = cur_node[1][0] if h_code[i] == '0' else cur_node[1][1]
            i += 1
        dec_text = dec_text + cur_node[1][0]           
    return dec_text

# Decode a bit stream following a Huffman tree
# Output a list
def huffman_dec_list(h_tree, h_code):
    dec_list = []
    i = 0
    while i < len(h_code):
        cur_node = h_tree[0]
        while len(cur_node[1]) == 2:
            cur_node = cur_node[1][0] if h_code[i] == '0' else cur_node[1][1]
            i += 1
        dec_list.append(cur_node[1][0])           
    return dec_list


