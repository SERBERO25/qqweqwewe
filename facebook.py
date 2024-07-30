import sqlite3
import datetime

conn = sqlite3.connect('facebook.db')

conn.execute('''CREATE TABLE IF NOT EXISTS usuarios
				 (id INTEGER PRIMARY KEY AUTOINCREMENT,
				 nombre TEXT NOT NULL,
				 apellido TEXT NOT NULL,
				 correo TEXT NOT NULL,
				 contrasena TEXT NOT NULL,
				 fecha_registro DATETIME NOT NULL)''')

conn.execute('''CREATE TABLE IF NOT EXISTS publicaciones
				 (id INTEGER PRIMARY KEY AUTOINCREMENT,
				 usuario_id INTEGER NOT NULL,
				 contenido TEXT NOT NULL,
				 fecha_publicacion DATETIME NOT NULL,
				 FOREIGN KEY(usuario_id) REFERENCES usuarios(id))''')

conn.execute('''CREATE TABLE IF NOT EXISTS amigos
				 (id INTEGER PRIMARY KEY AUTOINCREMENT,
				 usuario_id INTEGER NOT NULL,
				 amigo_id INTEGER NOT NULL,
				 fecha_amistad DATETIME NOT NULL,
				 FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
				 FOREIGN KEY(amigo_id) REFERENCES usuarios(id))''')

def registrar_usuario(nombre, apellido, correo, contrasena):
	fecha_registro = datetime.datetime.now()
	conn.execute('''INSERT INTO usuarios(nombre, apellido, correo, contrasena, fecha_registro)
					VALUES(?, ?, ?, ?, ?)''', (nombre, apellido, correo, contrasena, fecha_registro))
	conn.commit()

def publicar(usuario_id, contenido):
	fecha_publicacion = datetime.datetime.now()
	conn.execute('''INSERT INTO publicaciones(usuario_id, contenido, fecha_publicacion)
					VALUES(?, ?, ?)''', (usuario_id, contenido, fecha_publicacion))
	conn.commit()


def agregar_amigo(usuario_id, amigo_id):
	fecha_amistad = datetime.datetime.now()
	conn.execute('''INSERT INTO amigos(usuario_id, amigo_id, fecha_amistad)
					VALUES(?, ?, ?)''', (usuario_id, amigo_id, fecha_amistad))
	conn.commit()

def obtener_amigos(usuario_id):
	cursor = conn.execute('''SELECT * FROM amigos WHERE usuario_id = ?''', (usuario_id,))
	return cursor.fetchall()

def obtener_publicaciones(usuario_id):
	cursor = conn.execute('''SELECT * FROM publicaciones WHERE usuario_id = ?''', (usuario_id,))
	return cursor.fetchall()


conn.close()
