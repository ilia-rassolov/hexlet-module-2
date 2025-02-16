import os

from hexlet.fs import flatten, get_children, get_name, is_file, mkdir, mkfile

def find_files_by_name(tree, substring):
    def walk(node, path_node):
        name = get_name(node)
        children = get_children(node)
        ancestry = os.path.join(path_node, name)
        if is_file(node):
            if substring in name:
                return ancestry
            return []
        output = list(map(lambda child: walk(child, ancestry), children))
        return flatten(output)
    return walk(tree, '')

tree = mkdir('/', [
            mkfile('dataresoslve', {'size': 1000}),
            mkfile('hosts', {'size': 3500}),
            mkdir('etc', [
                mkdir('apache', [
                    mkfile('nginx1.conf', {'size': 800}),
                ]),
                mkdir('nginx', [
                    mkfile('nginx.conf', {'size': 800}),
                ]),
                mkdir('consul', [
                    mkfile('config.py.json'),
                    mkfile('dagtaos'),
                    mkfile('data1'),
                ]),
            ]),


        ])


print(find_files_by_name(tree, 'os'))

