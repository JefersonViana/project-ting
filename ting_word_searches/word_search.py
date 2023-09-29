from ting_file_management.queue import Queue


def exists_word_aux(word, instance: Queue):
    data = instance.read_instance()
    dicts = list([])
    for file in data:
        ocorrencias = list([])
        for index in range(1, len(file["linhas_do_arquivo"]) + 1):
            linha = file["linhas_do_arquivo"][index - 1]
            if word in linha.lower():
                ocorrencias.append({"linha": index, "conteudo": linha})
        if len(ocorrencias) > 0:
            dicts.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            })
    return dicts


def exists_word(word, instance: Queue):
    data = exists_word_aux(word, instance)
    for file in data:
        file["ocorrencias"] = [
            {"linha": xablau["linha"]} for xablau in file["ocorrencias"]
        ]
    return data


def search_by_word(word, instance: Queue):
    return exists_word_aux(word, instance)
