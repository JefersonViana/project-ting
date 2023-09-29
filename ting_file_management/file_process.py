from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def file_exist_in_instance(array, path_file):
    for current in array:
        if current["nome_do_arquivo"] == path_file:
            return True
    return False


def process(path_file: str, instance: Queue):
    data = txt_importer(path_file)
    dict_obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    content = instance.read_instance()
    if not file_exist_in_instance(content, path_file):
        instance.enqueue(dict_obj)
        sys.stdout.write(str(dict_obj))


def remove(instance: Queue):
    if len(instance) < 1:
        sys.stdout.write("Não há elementos\n")
        return None
    response_dequeue = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {response_dequeue['nome_do_arquivo']} removido com sucesso\n"
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# project = Queue()
# process("statics/arquivo_teste.txt", project)
# remove(project)
# process("statics/nome_pedro.txt", project)
# print(process("statics/arquivo_teste.txt", project))
