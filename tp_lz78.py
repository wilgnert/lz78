from sys import argv
from compress import compress
from decompress import decompress

def main():
    try:
        op = argv[1]
        input_file = argv[2]
    except IndexError:
        print("Poucos argumentos na chamada")
        show_help()
        exit()
    try:
        output_file = argv[4]
    except IndexError:
        output_file = input_file.rpartition(".")[0] + (".z78" if op == "-c" else ".txt")

    if op == "-c":
        compress(input_file, output_file)
    elif op == "-x":
        decompress(input_file, output_file)
    else:
        print(f"""Falha em reconhecer o comando './python {' '.join(argv)}'""")
        show_help()
        exit()
        

def show_help():
    print("Exemplos de chamadas válidas:")
    print("\tCompressão:\n\t\t./python tp_lz78.py -c <arquivo_entrada> [-o <arquivo_saida>]")
    print("\tDecompressão:\n\t\t./python tp_lz78.py -x <arquivo_entrada> [-o <arquivo_saida>]")

if __name__ == "__main__":
    main()
