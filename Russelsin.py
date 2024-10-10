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
        print(f"El estudiante: {self._nombre}, ID: {self._id_usuario}, Préstamos: {self._prestamos}")
 
    def agregar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)
 
 
class Profesor(Usuario):
    def __init__(self, nombre, id_usuario):
        super().__init__(nombre, id_usuario)
        self._prestamos = []
 
    def describir(self):
        print(f"El profesor: {self._nombre}, ID: {self._id_usuario}, Préstamos: {self._prestamos}")
 
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

class Manga(Publicacion):
    pass
 
 
class Prestamo:
    def __init__(self, usuario, publicacion):
        self.usuario = usuario
        self.publicacion = publicacion
 
    def realizar_prestamo(self):
        if self.publicacion.consultar_disponibilidad():
            self.publicacion.marcar_no_disponible()
            self.usuario.agregar_prestamo(self.publicacion._titulo)
            print(f"Préstamo realizado: {self.usuario.get_nombre()} ha tomado '{self.publicacion._titulo}'")
        else:
            print(f"El libro '{self.publicacion._titulo}' no está disponible.")
 
 
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
 
 
class Notificacion:
    def enviar_notificacion(self, mensaje):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
 
 
class NotificacionEmail(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por email: {mensaje}")
 
 
class NotificacionSMS(Notificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por SMS: {mensaje}")
 
 
# Modifying the main function to preload books and mangas and ask if user is new
def main():
    inventario = Inventario()
    
    # Pre-load books and mangas into the inventory
    preloaded_books = [
        Libro("Cien años de soledad", "Gabriel García Márquez"),
        Libro("Don Quijote", "Miguel de Cervantes")
    ]
    
    preloaded_mangas = [
        Manga("Jujutsu Kaisen", "Gege Akutami"),
        Manga("Naruto", "Masashi Kishimoto"),
        Manga("Dragon Ball Z", "Akira Toriyama"),
        Manga("One Piece", "Eiichiro Oda"),
        Manga("Dorohedoro", "Q Hayashida"),
        Manga("One Punch Man", "ONE")
    ]
    
    # Add books and mangas to the inventory
    for book in preloaded_books:
        inventario.agregar_publicacion(book)
    
    for manga in preloaded_mangas:
        inventario.agregar_publicacion(manga)
    
    usuarios = []
    
    # Pregunta si es un usuario nuevo
    nuevo_usuario = input("¿Eres un usuario nuevo? (si/no): ").strip().lower()
    
    if nuevo_usuario == 'si':
        nombre_usuario = input("Ingrese el nombre del nuevo usuario: ")
        id_usuario = input("Ingrese el ID del nuevo usuario: ")
        tipo_usuario = input("Ingrese el tipo de usuario (Estudiante, Profesor): ").strip().lower()
        
        if tipo_usuario == 'estudiante':
            nuevo_usuario = Estudiante(nombre_usuario, id_usuario)
        elif tipo_usuario == 'profesor':
            nuevo_usuario = Profesor(nombre_usuario, id_usuario)
        else:
            print("Tipo de usuario no válido.")
            return
        
        usuarios.append(nuevo_usuario)
        print(f"Usuario {nuevo_usuario.get_nombre()} creado con éxito.")
    
    # Menú de opciones normal
    while True:
        print("\nMenú:")
        print("1. Agregar publicación")
        print("2. Realizar préstamo")
        print("3. Mostrar inventario")
        print("4. Mostrar usuarios")
        print("5. Salir")
 
        opcion = input("Selecciona una opción: ")
 
        if opcion == '1':
            tipo_publicacion = input("Ingrese el tipo de publicación (Libro, Revista, Artículo, Manga): ").strip().lower()
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")
 
            if tipo_publicacion == 'libro':
                publicacion = Libro(titulo, autor)
            elif tipo_publicacion == 'revista':
                publicacion = Revista(titulo, autor)
            elif tipo_publicacion == 'artículo':
                publicacion = Articulo(titulo, autor)
            elif tipo_publicacion == 'manga':
                publicacion = Manga(titulo, autor)
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
            publicacion = next((pub for pub in inventario.publicaciones if pub._titulo == titulo_publicacion), None)
 
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
 
if __name__ == "__main__":
    main()
