from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Clase abstracta Usuario
class Usuario(ABC):
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario

    @abstractmethod
    def describir(self):
        pass

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if len(nombre) > 0:
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío")

    def get_id_usuario(self):
        return self._id_usuario

    def set_id_usuario(self, id_usuario):
        if len(id_usuario) > 0:
            self._id_usuario = id_usuario
        else:
            raise ValueError("El ID de usuario no puede estar vacío")

# Clase abstracta Notificacion
class Notificacion(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje):
        pass

# Subclase Estudiante
class Estudiante(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)
        self._prestamos = []

    def describir(self):
        print(f"Estudiante: {self._nombre}, ID: {self._id_usuario}, Préstamos: {self._prestamos}")

    def agregar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)

# Subclase Profesor
class Profesor(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)
        self._prestamos = []

    def describir(self):
        print(f"Profesor: {self._nombre}, ID: {self._id_usuario}, Préstamos: {self._prestamos}")

    def agregar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)

# Subclase Libro
class Libro(Notificacion):
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponibilidad = True

    def consultar_disponibilidad(self):
        return self._disponibilidad

    def marcar_no_disponible(self):
        self._disponibilidad = False

    def marcar_disponible(self):
        self._disponibilidad = True

    def enviar_notificacion(self, mensaje):
        print(f"Notificación de Libro '{self._titulo}': {mensaje}")

# Subclase Revista
class Revista(Notificacion):
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponibilidad = True

    def consultar_disponibilidad(self):
        return self._disponibilidad

    def marcar_no_disponible(self):
        self._disponibilidad = False

    def marcar_disponible(self):
        self._disponibilidad = True

    def enviar_notificacion(self, mensaje):
        print(f"Notificación de Revista '{self._titulo}': {mensaje}")

# Subclase Manga
class Manga(Notificacion):
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponibilidad = True

    def consultar_disponibilidad(self):
        return self._disponibilidad

    def marcar_no_disponible(self):
        self._disponibilidad = False

    def marcar_disponible(self):
        self._disponibilidad = True

    def enviar_notificacion(self, mensaje):
        print(f"Notificación de Manga '{self._titulo}': {mensaje}")

# Clase Prestamo
class Prestamo:
    def __init__(self, usuario, publicacion):
        self.usuario = usuario
        self.publicacion = publicacion
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=5)

    def realizar_prestamo(self):
        if self.publicacion.consultar_disponibilidad():
            self.publicacion.marcar_no_disponible()
            self.usuario.agregar_prestamo(self.publicacion._titulo)
            print(f"Préstamo realizado: {self.usuario.get_nombre()} ha tomado '{self.publicacion._titulo}'")
            print(f"Fecha de préstamo: {self.fecha_prestamo}")
            print(f"Fecha límite de devolución: {self.fecha_devolucion}")
        else:
            print(f"El libro '{self.publicacion._titulo}' no está disponible.")

# Clase Inventario
class Inventario:
    def __init__(self):
        self.publicaciones = []

    def agregar_publicacion(self, publicacion):
        self.publicaciones.append(publicacion)
        print(f"Publicación '{publicacion._titulo}' agregada al inventario.")

    def eliminar_publicacion(self, publicacion):
        self.publicaciones.remove(publicacion)
        print(f"Publicación '{publicacion._titulo}' eliminada del inventario.")

    def consultar_inventario(self):
        return [pub._titulo for pub in self.publicaciones]

# Clase NotificacionPrestamo (nueva clase para manejar notificaciones)
class NotificacionPrestamo(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Notificación de Préstamo: {mensaje}")

# Función principal (main)
def main():
    inventario = Inventario()

    # Pre-cargar libros y mangas al inventario
    preloaded_books = [
        Libro("Cien años de soledad", "Gabriel García Márquez"),
        Libro("Don Quijote", "Miguel de Cervantes")
    ]

    preloaded_mangas = [
        Manga("Naruto", "Masashi Kishimoto"),
        Manga("Dragon Ball Z", "Akira Toriyama")
    ]

    # Agregar libros y mangas al inventario
    for book in preloaded_books:
        inventario.agregar_publicacion(book)

    for manga in preloaded_mangas:
        inventario.agregar_publicacion(manga)

    usuarios = []

    # Menú de opciones
    while True:
        print("\nMenú:")
        print("1. Agregar publicación")
        print("2. Realizar préstamo")
        print("3. Mostrar inventario")
        print("4. Mostrar usuarios")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            tipo_publicacion = input("Ingrese el tipo de publicación (Libro, Revista, Manga): ").strip().lower()
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")

            if tipo_publicacion == 'libro':
                publicacion = Libro(titulo, autor)
            elif tipo_publicacion == 'revista':
                publicacion = Revista(titulo, autor)
            elif tipo_publicacion == 'manga':
                publicacion = Manga(titulo, autor)
            else:
                print("Tipo de publicación no válido.")
                continue

            inventario.agregar_publicacion(publicacion)

        elif opcion == '2':
            id_usuario = input("Ingrese el ID del usuario: ")

            # Verificar si el usuario ya existe
            usuario = next((usr for usr in usuarios if usr.get_id_usuario() == id_usuario), None)

            if not usuario:
                print("Usuario no encontrado. Creando nuevo usuario.")
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                tipo_usuario = input("Ingrese el tipo de usuario (Estudiante o Profesor): ").strip().lower()

                if tipo_usuario == 'estudiante':
                    usuario = Estudiante(nombre_usuario, id_usuario)
                elif tipo_usuario == 'profesor':
                    usuario = Profesor(nombre_usuario, id_usuario)
                else:
                    print("Tipo de usuario no válido.")
                    continue

                usuarios.append(usuario)
                print(f"Usuario {nombre_usuario} creado correctamente.")

            titulo_publicacion = input("Ingrese el título de la publicación a prestar: ")
            publicacion = next((pub for pub in inventario.publicaciones if pub._titulo.lower() == titulo_publicacion.lower()), None)

            if publicacion:
                prestamo = Prestamo(usuario, publicacion)
                prestamo.realizar_prestamo()
            else:
                print("La publicación no se encontró.")

        elif opcion == '3':
            print("Inventario actual:")
            for pub in inventario.consultar_inventario():
                print(f"- {pub}")

        elif opcion == '4':
            print("Usuarios registrados:")
            for usr in usuarios:
                usr.describir()

        elif opcion == '5':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
