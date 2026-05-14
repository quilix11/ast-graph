import ast
from src.services.ast_logic.reader import file_readers

def parser():
    files_data = file_readers()
    project_structure = {}

    for path, code in files_data.items():
        try:
            tree = ast.parse(code, filename=path)
            imports = []
            functions = []

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for n in node.names:
                        imports.append(n.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
                elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
                    functions.append(node.name)

            project_structure[str(path)] = {
                "imports": imports,
                "functions_and_classes": functions
            }
        except SyntaxError as e:
            project_structure[str(path)] = {"error": str(e)}
                
    return project_structure