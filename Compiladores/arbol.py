# arbol.py

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):
        indent = "    " * level
        if level == 0:
            result = f"{self.value}\n"
        else:
            connector = "├── " if self.is_not_last_child(level) else "└── "
            result = f"{indent}{connector}{self.value}\n"
        for i, child in enumerate(self.children):
            result += child.print_tree(level + 1)
        return result

    def is_not_last_child(self, level):
        # Esta función puede ser mejorada para manejar correctamente los conectores
        return True  # Simplificación para este ejemplo

def build_syntax_tree(tokens):
    """
    Construye un árbol sintáctico a partir de los tokens proporcionados.
    """
    root = Node('Programa')  # Nodo raíz
    stack = [root]  # Pila para manejar los nodos
    current_node = root

    i = 0
    while i < len(tokens):
        token_type, token_value = tokens[i]

        if token_type == "KEYWORD":
            if token_value in {"if", "for", "while"}:
                new_node = Node(token_value)
                current_node.add_child(new_node)
                stack.append(current_node)
                current_node = new_node
            elif token_value == "else":
                new_node = Node("else")
                current_node.add_child(new_node)
                stack.append(current_node)
                current_node = new_node
            else:
                # Otros keywords, como 'def', 'class', etc.
                new_node = Node(token_value)
                current_node.add_child(new_node)
                stack.append(current_node)
                current_node = new_node

        elif token_type == "IDENTIFIER":
            id_node = Node(f"{token_value}")
            current_node.add_child(id_node)

        elif token_type == "NUMBER":
            num_node = Node(f"{token_value}")
            current_node.add_child(num_node)

        elif token_type == "STRING":
            str_node = Node(f"{token_value}")
            current_node.add_child(str_node)

        elif token_type == "OPERATOR":
            op_node = Node(f"{token_value}")
            current_node.add_child(op_node)

        elif token_type == "DELIMITER":
            if token_value == '{':
                # Iniciar un nuevo bloque
                new_node = Node('Bloque')
                current_node.add_child(new_node)
                stack.append(current_node)
                current_node = new_node
            elif token_value == '}':
                # Cerrar el bloque actual
                if len(stack) > 0:
                    current_node = stack.pop()
            elif token_value == ';':
                # Fin de una instrucción, volver al nodo padre
                if len(stack) > 0:
                    current_node = stack.pop()
        else:
            # Manejar otros tipos de tokens si es necesario
            unknown_node = Node(f"Token desconocido: {token_value}")
            current_node.add_child(unknown_node)

        i += 1

    return root
