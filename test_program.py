from compress import compress
from decompress import decompress
from compress_broken import compress as compress_broken
import os

def main():
    source_path = ["exemplos", "originais"]
    compress_path = ["exemplos", "compressoes"]
    decompress_path = ["exemplos", "decompressoes"]
    text_ext = ".txt"
    compress_ext = ".z78"

    files = [
        "alice",
        "constituicao1988",
        "dom_casmurro",
        "example",
        "lupin",
        "metamorfose",
        "os_lusiadas",
        "pride",
        "two-cities",
        "物语系列__04卷_伪物语（上）"
    ]

    for f in files:
        in_file = os.path.join("exemplos", "originais", f + text_ext)
        out_file = os.path.join("exemplos", "compressoes", f + compress_ext)

        compress(in_file, out_file)

    for f in files:
        in_file = os.path.join("exemplos", "compressoes", f + compress_ext)
        out_file = os.path.join("exemplos", "decompressoes", f + text_ext)

        decompress(in_file, out_file)

    for f in files:
        in_file = os.path.join("exemplos", "originais", f + text_ext)
        out_file = os.path.join("exemplos", "compressoes_quebradas", f + compress_ext)

        compress_broken(in_file, out_file)
    

if __name__ == "__main__":
    main()
