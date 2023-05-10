import numpy as np

def decompress(in_file, out_file):
    out = ""
    with open(in_file, "rb") as f:
        num_of_codes = np.fromfile(f, np.uint64, 1)[0]
        if num_of_codes < 256:
            my_type = np.uint8
        elif num_of_codes < 65536:
            my_type = np.uint16
        elif num_of_codes < 4294967296:
            my_type = np.uint32
        else:
            my_type = np.uint64

        buffer = [[0, None, ""]] + [[0]for i in range(1, num_of_codes)]
        # por_velho = 0            
        for i in range(num_of_codes):
            # por = round(i * 100 /num_of_codes)
            # if por != por_velho:
            #     print(f"{por}%")
            #     por_velho = por
            try:
                code = np.fromfile(f, my_type, 1)[0]
                prev_code = np.fromfile(f, my_type, 1)[0]
                letter = bytes(f.read(4)).decode(encoding="utf-16")
            except IndexError:
                break
            buffer[code] = [code, prev_code, letter]
            def get_string(codigo):
                if (codigo == None):
                    return ""
                else:
                    ret = get_string(buffer[codigo][1]) + buffer[codigo][2]
                    return ret
            out += get_string(prev_code) + letter

    with open(out_file, "w", encoding="utf-16") as f:
        f.write(out)