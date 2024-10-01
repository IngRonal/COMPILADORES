from compiladores import tokenize
from arbol import build_syntax_tree

def main():
    while True:
        print("Seleccione una opción:")
        print("1. Analizar código")
        print("2. Generar árbol sintáctico")
        print("3. Salir")

        choice = input("Ingrese su elección: ")

        if choice == '1':
            print("Ingrese su código (dos Enter para terminar):")
            code = []
            empty_count = 0  # Contador para controlar cuántos Enter seguidos se presionan
            while True:
                line = input()
                if line == "":
                    empty_count += 1  # Contamos si la línea está vacía
                    if empty_count == 2:  # Si se presionan dos Enter, termina la entrada
                        break
                else:
                    empty_count = 0  # Resetea el contador si se ingresa algo
                    code.append(line)

            code = "\n".join(code)  # Combina todas las líneas en una sola cadena
            tokens = tokenize(code)  # Tokeniza el código
            print("Tokens encontrados:")
            for token_type, token_value in tokens:
                print(f"{token_type}: {token_value}")

        elif choice == '2':
            print("Ingrese su código para generar el árbol sintáctico (dos Enter para terminar):")
            code = []
            empty_count = 0  # Contador para detectar dos líneas vacías consecutivas
            while True:
                line = input()
                if line == "":
                    empty_count += 1  # Incrementa el contador en caso de línea vacía
                    if empty_count == 2:  # Si hay dos Enter seguidos, se detiene la entrada
                        break
                else:
                    empty_count = 0  # Reinicia el contador si la línea no está vacía
                    code.append(line)

            if not code:
                print("No se ingresó ningún código.")
                continue

            code = "\n".join(code)  # Combina todas las líneas en una sola cadena

            # Tokenizar el código ingresado
            tokens = tokenize(code)

            # Generar el árbol sintáctico
            syntax_tree = build_syntax_tree(tokens)
            print("\nÁrbol sintáctico:")
            print(syntax_tree.print_tree())  # Asegúrate de que esta función esté implementada

        elif choice == '3':
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
