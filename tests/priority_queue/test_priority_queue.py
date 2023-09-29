from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_management import txt_importer
import pytest


def test_basic_priority_queueing():
    path_file = "statics/arquivo_teste.txt"
    data_high_priority = txt_importer(path_file)
    dict_obj_high_priority = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data_high_priority),
        "linhas_do_arquivo": data_high_priority
    }
    projetc = PriorityQueue()
    projetc.enqueue(dict_obj_high_priority)
    assert len(projetc) == 1

    projetc.dequeue()

    assert len(projetc) == 0

    path_file_regular_priority = "statics/novo_paradigma_globalizado-min.txt"
    data_regular_priority = txt_importer(path_file_regular_priority)
    dict_obj_regular_priority = {
        "nome_do_arquivo": path_file_regular_priority,
        "qtd_linhas": len(data_regular_priority),
        "linhas_do_arquivo": data_regular_priority
    }

    projetc.enqueue(dict_obj_regular_priority)
    projetc.enqueue(dict_obj_high_priority)

    assert len(projetc) == 2
    assert projetc.high_priority.read_instance()[0]["qtd_linhas"] == 3
    assert len(projetc.high_priority.read_instance()) == 1
    assert projetc.search(1)["qtd_linhas"] == 19
    assert projetc.search(0)["qtd_linhas"] == 3

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        projetc.search(2)
