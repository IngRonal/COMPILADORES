import re  # Importa el módulo de expresiones regulares para analizar el código fuente

# Definición de las categorías de tokens mediante expresiones regulares
TOKEN_REGEX = [
    ('PALABRA CLAVE', r'\b(if|else|while|for|return|int|float|char|true|false|null|print|break|continue|switch|case|default|def)\b'),
    ('IDENTIFICADOR', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    ('LITERAL NUMÉRICO', r'\b\d+(\.\d+)?\b'),
    ('LITERAL CADENA', r'\".*?\"|\'.*?\''),
    ('OPERADOR ARITMÉTICO', r'[+\-*/%]'),
    ('OPERADOR RELACIONAL', r'[<>]=?|==|!='),
    ('OPERADOR LÓGICO', r'&&|\|\||!'),
    ('OPERADOR DE ASIGNACIÓN', r'=\s?|[+\-*/%]=|\+=|\-=|\*=|\/=|\%='), 
    ('DELIMITADOR', r'[;,\(\)\[\]\{\}]'),
    ('COMENTARIO UNA LÍNEA', r'//.*'),
    ('COMENTARIO VARIAS LÍNEAS', r'/\*[\s\S]*?\*/'),
    ('SEPARADOR', r'\s+'),
    ('DESCONOCIDO', r'.'),
]

def tokenize(code):
    """
    Analiza el código fuente y lo divide en tokens.
    """
    pos = 0  
    tokens = {token_type: set() for token_type, _ in TOKEN_REGEX}  # Usamos sets para evitar duplicados

    while pos < len(code):  
        match = None  

        # Primero buscamos palabras clave
        for token_type, regex in TOKEN_REGEX:
            if token_type == 'PALABRA CLAVE':
                pattern = re.compile(regex)
                match = pattern.match(code, pos)
                if match:
                    tokens[token_type].add(match.group(0))
                    pos = match.end(0)
                    break

        # Luego buscamos identificadores y otros tokens si no se encontró una palabra clave
        if not match:
            for token_type, regex in TOKEN_REGEX:
                if token_type != 'PALABRA CLAVE':
                    pattern = re.compile(regex)
                    match = pattern.match(code, pos)
                    if match:
                        if token_type != 'SEPARADOR':
                            tokens[token_type].add(match.group(0))
                        pos = match.end(0)
                        break

        if not match:
            raise ValueError(f'Error: Caracter inesperado en posición {pos}')  

    return tokens  

def display_tokens(tokens):
    """
    Muestra los tokens encontrados agrupados por tipo, sin repetir y separados por comas, con guion al principio.
    """
    print("\nTokens encontrados:")
    for token_type, token_list in tokens.items():
        if token_list:  
            # Ordenamos los tokens y los mostramos con comas y precedidos por un guion
            print(f"{token_type}: - " + ", ".join(sorted(token_list)))

def menu():
    """
    Menú interactivo para seleccionar opciones.
    """
    while True:
        print("============================================")
        print("|          Analizador de Tokens            |")
        print("============================================")
        print("| 1. Analizar un código predefinido         |")
        print("| 2. Ingresar y analizar un código propio   |")
        print("| 3. Salir                                 |")
        print("============================================")
        
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            predefinido = '''
            float calcularPromedio(int[] numeros, int tamaño) {
                int suma = 0;
                for (int i = 0; i < tamaño; i++) {
                    suma += numeros[i];  
                }
                if (tamaño > 0) {
                    return suma / tamaño; 
                } else {
                    return 0;  
                }
            }
            print("El cálculo ha finalizado.");
            '''
            print("\n--- Análisis de código predefinido ---")
            tokens = tokenize(predefinido)
            display_tokens(tokens)
            input("\nPresiona Enter para volver al menú...")  

        elif opcion == "2":
            print("\nIngresa tu código (termina con una línea vacía):")
            code_lines = []
            while True:
                line = input()
                if line == '':
                    break
                code_lines.append(line)
            code = "\n".join(code_lines)
            try:
                tokens = tokenize(code)
                display_tokens(tokens)
            except ValueError as e:
                print(e)

            input("\nPresiona Enter para volver al menú...")  

        elif opcion == "3":
            print("\nSaliendo del programa...")
            break  

        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

# Llama al menú principal
menu()
