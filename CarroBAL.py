import datetime


class CarroBAL:

    def VerificaMarca(self, marca):
        if not marca:
            raise SystemExit("Marca é Obrigatório.")

        elif len(marca) < 3:
            raise SystemExit("Marca tem que ter pelo menos 3 caracteres.")

        elif len(marca) > 100:
            raise SystemExit("Marca tem que ter menos que 100 caraceteres.")

    def VerificaFoto(self, foto):
        if not foto:
            raise SystemExit("Foto é Obrigatória.")

        elif len(foto) < 3:
            raise SystemExit("Foto tem que ter pelo menos 3 caracteres.")

        elif len(foto) > 100:
            raise SystemExit("Foto tem que ter menos que 100 caraceteres.")

    def VerificaAno(self, ano):
        ano = datetime.datetime.strptime(ano, "%d-%m-%Y").strftime("%Y-%m-%d")

        if not ano:
            raise SystemExit("Ano é Obrigatória.")

        elif ano > str(datetime.datetime.now()):
            raise SystemExit("Ano não pode ser maior que a data de hoje.")

        elif ano < "1900-01-01":
            raise SystemExit("Ano invalida.")

        return ano

    def VerificaValor(self, valor):
        if len(valor) < 1:
            raise SystemExit("Valor Invalido.")
