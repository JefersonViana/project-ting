import sys


def txt_importer(path_file):
    if path_file.split(".")[-1] != "txt":
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file, mode="r") as file:
            return [string.split("\n")[0] for string in file.readlines()]
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
