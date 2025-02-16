from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name, is_file

def du(tree):
    meta = get_meta(tree)
    children = get_children(tree)

    def get_size_node(node):
        if is_file(node):
            return get_meta(node)['size']
        return sum(list(map(get_size_node, get_children(node))))

    result = list(map(lambda child: (get_name(child), get_size_node(child)), children))

    result.append((get_name(tree), get_size_node(tree)))
    def key(x):
        return - x[1]
    result.sort(key=key)
    return result

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.py.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])

print(du(tree))







