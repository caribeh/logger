import os, getpass
from datetime import datetime
class Logger:
    def __init__(self,arquivo):
        self.logfile = arquivo
        self.data_e_hora_atuais = datetime.now()
        self.hora_atual = self.data_e_hora_atuais.strftime("%H:%M")
        self.data_atual = self.data_e_hora_atuais.strftime("%d/%m/%Y")
        self.rotacionar(self.logfile)
        
    def rotacionar(self, logfile):
        logfile = logfile
        
        if os.path.exists(logfile):
            #arquivo de log existe
            data_criacao_arquivo = datetime.fromtimestamp(os.path.getctime(logfile))
            nome_criacao_arquivo = data_criacao_arquivo.strftime("%d%m%Y")
            data_criacao_arquivo = data_criacao_arquivo.strftime("%d/%m/%Y")
            if data_criacao_arquivo != self.data_atual:
                #arquivo tem data diferente da data de hoje
                self.escrever("Rotacionando arquivo de log")
                log_rotado = logfile+"-"+nome_criacao_arquivo
                if os.path.exists(log_rotado):
                    #arquivo de log com a data existe
                    contador = 1
                    log_rotado_contado = log_rotado+"."+str(contador)
                    while True:
                        if os.path.exists(log_rotado_contado):
                            #arquivo de log com contador existe
                            contador += 1
                            log_rotado_contado = log_rotado+"."+str(contador)
                        else:
                            os.rename(self.logfile, log_rotado_contado)
                            break
                else:
                    os.rename(self.logfile, log_rotado)

    def escrever(self, mensagem):
        
        with open(self.logfile, "a") as arquivo:
            arquivo.write(self.data_atual)
            arquivo.write(" ")
            arquivo.write(self.hora_atual)
            arquivo.write(" - ")
            arquivo.write("USER: ")
            arquivo.write(getpass.getuser())
            arquivo.write(" - ")
            arquivo.write(mensagem)
            arquivo.write("\n")