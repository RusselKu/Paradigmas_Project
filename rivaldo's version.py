from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario

    def describir(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

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


class Estudiante(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)
        self._prestamos = []

    def describir(self):
        print(f"El estudiante: {self._nombre}, ID: {self._id_usuario}, Préstamos: {len(self._prestamos)}")

    def agregar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)


class Profesor(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)
        self._prestamos = []

    def describir(self):
        print(f"El profesor: {self._nombre}, ID: {self._id_usuario}, Préstamos: {len(self._prestamos)}")

    def agregar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)


class Bibliotecario(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)

    def mostrar_info(self):
        print(f"Bibliotecario: {self._nombre}, ID: {self._id_usuario}")

    def gestionar_inventario(self, publicacion, accion, inventario):
        if accion == 'agregar':
            inventario.agregar_publicacion(publicacion)
        elif accion == 'eliminar':
            inventario.eliminar_publicacion(publicacion)


class Publicacion:
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


class Libro(Publicacion):
    pass


class Revista(Publicacion):
    pass


class Articulo(Publicacion):
    pass


class Prestamo:
    def __init__(self, usuario, publicacion):
        self.usuario = usuario
        self.publicacion = publicacion
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=7)

    def realizar_prestamo(self):
        if self.publicacion.consultar_disponibilidad():
            self.publicacion.marcar_no_disponible()
            self.usuario.agregar_prestamo(self)  # Almacenar el objeto Prestamo
            print(f"Préstamo realizado: {self.usuario.get_nombre()} ha tomado '{self.publicacion._titulo}'")
            print(f"Fecha de devolución: {self.fecha_devolucion.strftime('%Y-%m-%d')}")
            return self.fecha_devolucion
        else:
            print(f"El libro '{self.publicacion._titulo}' no está disponible.")
            return None


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


# Ejemplo de uso interactivo
def main():
    inventario = Inventario()
    usuarios = []

    while True:
        print("\nMenú:")
        print("1. Agregar publicación")
        print("2. Realizar préstamo")
        print("3. Mostrar inventario")
        print("4. Mostrar usuarios")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            tipo_publicacion = input("Ingrese el tipo de publicación (Libro, Revista, Artículo): ").strip().lower()
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")

            if tipo_publicacion == 'libro':
                publicacion = Libro(titulo, autor)
            elif tipo_publicacion == 'revista':
                publicacion = Revista(titulo, autor)
            elif tipo_publicacion == 'artículo':
                publicacion = Articulo(titulo, autor)
            else:
                print("Tipo de publicación no válido.")
                continue

            inventario.agregar_publicacion(publicacion)

        elif opcion == '2':
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            tipo_usuario = input("Ingrese el tipo de usuario (Estudiante, Profesor): ").strip().lower()

            # Verificar si el usuario ya existe
            usuario_existente = next((usr for usr in usuarios if usr.get_id_usuario() == id_usuario), None)

            if usuario_existente:
                usuario = usuario_existente
            else:
                if tipo_usuario == 'estudiante':
                    usuario = Estudiante(nombre_usuario, id_usuario)
                elif tipo_usuario == 'profesor':
                    usuario = Profesor(nombre_usuario, id_usuario)
                else:
                    print("Tipo de usuario no válido.")
                    continue
                usuarios.append(usuario)

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

        # Mostrar el estado actualizado después de cada acción
        print("\nEstado actualizado:")
        print("Inventario actual:")
        for pub in inventario.consultar_inventario():
            print(f"- {pub}")

        print("Usuarios registrados:")
        for usr in usuarios:
            usr.describir()

        # Mostrar fechas de devolución y autor
        print("Fechas de devolución de publicaciones:")
        for usr in usuarios:
            if isinstance(usr, Estudiante) or isinstance(usr, Profesor):
                for prestamo in usr._prestamos:
                    fecha_devolucion = prestamo.fecha_devolucion
                    dias_restantes = (fecha_devolucion - datetime.now()).days
                    print(f"Usuario: {usr.get_nombre()}, Publicación: '{prestamo.publicacion._titulo}', Autor: '{prestamo.publicacion._autor}', Fecha de devolución: {fecha_devolucion.strftime('%Y-%m-%d')}, Días restantes: {dias_restantes} días")

if __name__ == "__main__":
    main()

