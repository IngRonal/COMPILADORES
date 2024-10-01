import re

# Definición de las categorías de tokens mediante expresiones regulares, incluyendo Python y C++
TOKEN_REGEX = [
    ('COMMENT', r'#.*|//.*|/\*[\s\S]*?\*/'),  # Comentarios de Python y C++
    ('KEYWORD', r'\b(if|else|while|for|return|int|float|char|print|match|break|def|class|public|private|void|elif|switch|case|default|do|continue)\b'),  # Palabras clave comunes de Python y C++
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),  # Identificadores
    ('NUMBER', r'\b\d+(\.\d+)?\b'),  # Números enteros y decimales
    ('OPERATOR', r'[+\-*/%=<>!&|^~:.]+'),  # Operadores matemáticos y lógicos (agregué ':' y '.')
    ('DELIMITER', r'[;,\(\)\{\}\[\]]'),  # Delimitadores (eliminé ':' para evitar duplicación)
    ('STRING', r'\".*?\"|\'.*?\'',),  # Literales de cadena
    ('WHITESPACE', r'\s+'),  # Espacios en blanco (serán ignorados)
    ('UNKNOWN', r'.'),  # Cualquier otro carácter que no coincida con los anteriores
]

def tokenize(code):
    """
    Función que toma el código fuente como entrada y devuelve una lista de tokens en orden.
    Cada token es una tupla (token_type, token_value).
    """
    pos = 0
    tokens = []

    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_REGEX)
    pattern = re.compile(tok_regex)
    line_num = 1
    line_start = 0

    for mo in re.finditer(pattern, code):
        kind = mo.lastgroup
        value = mo.group(kind)

        if kind in {'COMMENT', 'WHITESPACE'}:
            pos = mo.end()
            continue  # Ignorar comentarios y espacios en blanco

        if kind == 'UNKNOWN':
            raise ValueError(f'Error: Caracter inesperado {value!r} en posición {pos}')

        tokens.append((kind, value))
        pos = mo.end()

    return tokens

if __name__ == "__main__":
    # Ejemplo de uso
    code = input("Ingrese el código fuente: ")
    try:
        tokens = tokenize(code)
        # Imprimir los tokens en orden
        for token_type, token_value in tokens:
            print(f"{token_type}: {token_value}")
    except ValueError as ve:
        print(ve)
