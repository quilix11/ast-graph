import ast
from reader import file_readers

def parser():
    files_data = file_readers()
    trees = {}

    for path, code in files_data.items():
            try:
                tree = ast.parse(code, filename=path)
                trees[path] = ast.dump(tree, indent=2)
            except SyntaxError as e:
                trees[path] = e
                
    return trees
