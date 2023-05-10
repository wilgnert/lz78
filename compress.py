from trie import Trie
import numpy as np

def compress(in_file, out_file):
    with open(in_file, "r", encoding="utf-16") as f:
        text = f.read()
    string = ""
    out:list[tuple[np.uint64, str]] = []
    num_of_codes = np.uint64(1)
    t = Trie()
    with open(out_file, "bw+") as f:
        
        for char in text:
            node = t.find(string + char)
            if node != None:
               string += char
            else:
                t.insert(string + char)
                num_of_codes += np.uint64(1)
                node = t.find(string + char)
                out.append([node.pattern_code, node.previous_pattern_code, node.value])
                string = ""

        num_of_codes.tofile(f)

        if num_of_codes < 256:
            my_type = np.uint8
        elif num_of_codes < 65536:
            my_type = np.uint16
        elif num_of_codes < 4294967296:
            my_type = np.uint32
        elif num_of_codes < 18446744073709551616:
            my_type = np.uint64

        for c, k, v in out:
            my_type(c).tofile(f)
            my_type(k).tofile(f)
            f.write(bytes(v, encoding="utf-16"))