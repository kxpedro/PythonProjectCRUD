from CarroBAL import CarroBAL
from CarroTO import CarroTO
import pymysql
import re


class CarroDAO():
    def conetar(self):
        db = pymysql.connect("localhost", "root", "", "projeto")
        return db

    def listar(self):
        db = self.conetar()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM carro;")

        rows = cursor.fetchall()
        return rows

    def inserir(self, marca, ano, valor, foto):
        db = self.conetar()
        cursor = db.cursor()

        funBAL = CarroBAL()
        funBAL.VerificaMarca(marca)
        funBAL.VerificaFoto(foto)
        ano = funBAL.VerificaAno(ano)
        funBAL.VerificaValor(valor)

        f = CarroTO(marca, ano, valor, foto)

        sql = "INSERT INTO carro (marca, ano, valor, foto) VALUES ('"
        sql += re.sub("^\s+|\s+$", "", f.getMarca(), flags=re.UNICODE)
        sql += "','"
        sql += f.getAno()
        sql += "','"
        sql += f.getValor()
        sql += "','"
        sql += (re.sub("^\s+|\s+$", "", f.getFoto(), flags=re.UNICODE))
        sql += "');"

        cursor.execute(sql)
        db.commit()
        db.close()

    def excluir(self, id):
        db = self.conetar()
        cursor = db.cursor()

        sql = "DELETE FROM carro WHERE id = '"
        sql += str(id)
        sql += "';"

        cursor.execute(sql)
        db.commit()
        db.close()

    def editar(self, id, marca, ano, valor, foto):
        db = self.conetar()
        cursor = db.cursor()

        funBAL = CarroBAL()
        funBAL.VerificaMarca(marca)
        funBAL.VerificaFoto(foto)
        ano = funBAL.VerificaAno(ano)
        funBAL.VerificaValor(valor)

        f = CarroTO(marca, ano, valor, foto)

        sql = "UPDATE carro SET marca = '"
        sql += f.getMarca()
        sql += "', ano = '"
        sql += f.getAno()
        sql += "', valor = '"
        sql += f.getValor()
        sql += "', foto = '"
        sql += f.getFoto()
        sql += "' WHERE id = '"
        sql += str(id)
        sql += "';"

        cursor.execute(sql)
        db.commit()
        db.close()
