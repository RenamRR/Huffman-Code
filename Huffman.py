from queue import PriorityQueue

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(symbols, frequencies):
    pq = PriorityQueue()
    for i in range(len(symbols)):
        pq.put(Node(symbols[i], frequencies[i]))

    while pq.qsize() > 1:
        left = pq.get()
        right = pq.get()
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        pq.put(parent)

    return pq.get()

def huffman_codes(root, code, huffman_codes_dict):
    if root is None:
        return

    if root.symbol is not None:
        huffman_codes_dict[root.symbol] = code
        return

    huffman_codes(root.left, code + '0', huffman_codes_dict)
    huffman_codes(root.right, code + '1', huffman_codes_dict)

def huffman_encoding(symbols, frequencies):
    root = build_huffman_tree(symbols, frequencies)
    huffman_codes_dict = {}
    huffman_codes(root, "", huffman_codes_dict)
    encoded_data = ""
    for symbol in symbols:
        encoded_data += huffman_codes_dict[symbol]
    return encoded_data, huffman_codes_dict

#Exemplo de uso
symbols = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]
encoded_data, huffman_codes_dict = huffman_encoding(symbols, frequencies)
print("Códigos de Huffman:", huffman_codes_dict)
print("Texto codificado:", encoded_data)
