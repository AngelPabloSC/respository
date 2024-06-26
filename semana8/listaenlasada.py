class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cursor = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:  # Lista vacía
            self.cabeza = self.cola = nuevo_nodo
            self.cursor = nuevo_nodo  # El cursor ahora apunta al nuevo nodo
        else:
            if not self.cursor:  # Cursor no está definido, insertar al final
                self.cola.siguiente = nuevo_nodo
                nuevo_nodo.anterior = self.cola
                self.cola = nuevo_nodo
                self.cursor = nuevo_nodo  # El cursor ahora apunta al nuevo nodo
            else:
                # Insertar en la posición del cursor
                nuevo_nodo.siguiente = self.cursor
                nuevo_nodo.anterior = self.cursor.anterior
                if self.cursor.anterior:
                    self.cursor.anterior.siguiente = nuevo_nodo
                self.cursor.anterior = nuevo_nodo
                if self.cursor == self.cabeza:
                    self.cabeza = nuevo_nodo
                self.cursor = nuevo_nodo  # El cursor ahora apunta al nuevo nodo

    def eliminar(self):
        if not self.cursor:  # Cursor no definido, nada que eliminar
            return
        if self.cursor == self.cabeza:  # Eliminar la cabeza
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            if self.cursor == self.cola:  # Si solo había un elemento
                self.cola = None
            self.cursor = self.cabeza
        elif self.cursor == self.cola:  # Eliminar la cola
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            self.cursor = self.cola
        else:  # Eliminar en la posición del cursor
            self.cursor.anterior.siguiente = self.cursor.siguiente
            self.cursor.siguiente.anterior = self.cursor.anterior
            self.cursor = self.cursor.siguiente

    def mover_cursor_izquierda(self):
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior

    def mover_cursor_derecha(self):
        if self.cursor and self.cursor.siguiente:
            self.cursor = self.cursor.siguiente

    def mostrar_lista(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def mostrar_texto(self):
        actual = self.cabeza
        texto = ""
        while actual:
            texto += actual.dato
            actual = actual.siguiente
        return texto

class EditorTexto:
    def __init__(self):
        self.lista = ListaDoblementeEnlazada()

    def insertar(self, caracter):
        self.lista.insertar(caracter)

    def eliminar(self):
        self.lista.eliminar()

    def mover_cursor_izquierda(self):
        self.lista.mover_cursor_izquierda()

    def mover_cursor_derecha(self):
        self.lista.mover_cursor_derecha()

    def mostrar_texto(self):
        return self.lista.mostrar_texto()

# Ejemplos de uso
editor = EditorTexto()

# Insertar caracteres
editor.insertar('a')
editor.insertar('l')
editor.insertar('o')
editor.insertar('h')
print(editor.mostrar_texto())  # Output: Hola

# Mover cursor y eliminar
editor.mover_cursor_izquierda()
editor.mover_cursor_izquierda()
editor.eliminar()
print(editor.mostrar_texto())  # Output: ola

# Insertar un carácter
editor.insertar('h')
print(editor.mostrar_texto())  # Output: Hola