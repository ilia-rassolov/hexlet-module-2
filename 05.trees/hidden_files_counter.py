import copy

from hexlet.fs import mkdir, mkfile, get_children, get_name, is_file

def get_hidden_files_count(node):
    name = get_name(node)
    if is_file(node):
        if name[0] == '.':
            return 1
    children = get_children(node)
    new_children = copy.deepcopy(children)
    quantity_hidden_files = list(map(get_hidden_files_count, new_children))
    return sum(quantity_hidden_files)

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.py.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])

print(get_hidden_files_count(tree))

