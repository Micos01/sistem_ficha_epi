import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_main import Ui_MainWindow
from PySide6.QtCore import Qt
import openpyxl as pl
import shutil
import json
import sqlite3
from database import Database
from datetime import datetime
import xlwings as xw

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Ficha Epi')
        appIcons = QIcon(u"icon.png")
        self.setWindowIcon(appIcons)

        # Inicializar variáveis
        self.funcoes = {}
        self.funcao_map_config = {}

        # Conectar botões a métodos
        self.setup_connections()

        # Conectar botões de abrir e fechar o banco
        self.btn_abrir_banco.clicked.connect(self.abrir_banco)
        self.btn_fechar_banco.clicked.connect(self.fechar_banco)

        # Popula comboboxes da ficha
        self.populate_cb_ficha()

        # Gera o log das fichas EPI
        self.log_epi()

        # Configura as tabelas de configuração
        self.table_config()

    def setup_connections(self):
        """Conecta os botões aos métodos correspondentes."""
        self.btn_gerar_ficha_epi.clicked.connect(self.ficha_epi2)
        self.btn_refazer_ficha.clicked.connect(self.refazer_ficha)
        self.btn_pesquisar_colaborador.clicked.connect(self.pesquisar_ficha)
        self.btn_remover.clicked.connect(self.remover_ficha)
        self.btn_pesquisa_config.clicked.connect(self.pesquisar_uniforme)
        self.btn_pesquisa_config_2.clicked.connect(self.pesquisar_funcao)
        self.btn_pesquisa_setor_config.clicked.connect(self.pesquisar_setor)
        self.btn_add_item_config.clicked.connect(self.adicionar_item_funcao)
        self.btn_add_func_config_2.clicked.connect(self.adicionar_funcao_map)
        self.btn_add_setor_config.clicked.connect(self.adicionar_setor)
        self.btn_remover_config.clicked.connect(self.remover_item_funcao)
        self.btn_remover_config_2.clicked.connect(self.remover_funcao_map)
        self.btn_remover_setor_config.clicked.connect(self.remover_setor)
        

    
            
        
            



    def abrir_banco(self):
        """Abre a conexão com o banco de dados."""
        try:
            self.db = Database()
            if self.db.conecta():
                QMessageBox.information(self, "Sucesso", "Banco de dados aberto com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", "Não foi possível abrir o banco de dados.")
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Erro ao abrir o banco de dados: {e}")

    def fechar_banco(self):
        """Fecha a conexão com o banco de dados."""
        try:
            if hasattr(self, 'db'):
                self.db.close_connection()
                QMessageBox.information(self, "Sucesso", "Banco de dados fechado com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", "A conexão com o banco de dados já está fechada.")
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Erro ao fechar o banco de dados: {e}")

    def populate_cb_ficha(self):
        """Popula os comboboxes com os dados de funções e setores do banco de dados."""
        try:
            db = Database()
            db.conecta()
            tipo = ["CPF", "NOME"]

            self.cb_revazer_ficha.addItems(tipo)

            # Consulta para obter as funções e suas descrições
            cursor = db.connection.cursor()
            cursor.execute("SELECT DISTINCT funcao FROM itens_funcao")
            funcoes = cursor.fetchall()

            # Consulta para obter os setores
            cursor.execute("SELECT DISTINCT setor FROM setores")
            setores = cursor.fetchall()

            # Mapeamento de funções
            cursor.execute("SELECT funcao_original, funcao_mapeada FROM funcao_map")
            funcao_map = cursor.fetchall()

            # Populando os comboboxes
            self.cb_funcao.addItems([funcao[0] for funcao in funcoes])
            self.cb_select_func_config.addItems([funcao[0] for funcao in funcoes])
            self.cb_setor.addItems([setor[0] for setor in setores])

            # Salvando o mapeamento de funções localmente
            self.funcoes = {funcao[0]: [] for funcao in funcoes}
            self.funcao_map_config = {mapa[0]: mapa[1] for mapa in funcao_map}

        except sqlite3.Error as e:
            QMessageBox.warning(self, "Erro", f"Erro ao carregar dados do banco: {e}")
        finally:
            db.close_connection()

    def ficha_epi2(self):
        """Preenche a ficha de EPI e preserva as imagens no arquivo Excel."""
        try:
            # Coletar dados dos campos
            data_admissao = self.le_admissao.text()
            data_int = self.le_integracao.text()
            nome = self.line_nome.text().upper()
            tam_uniforme = self.line_tam_uniforme.text()
            tam_sapato = self.line_tam_sapato.text()
            cpf = self.line_cpf.text()
            setor = self.cb_setor.currentText()
            funcao = self.cb_funcao.currentText()

            # Caminho do arquivo original e do destino
            origem = "files//ficha_epi.xlsx"
            destino = f"FICHAS//{data_admissao.replace('/', '_')}_{nome}.xlsx"

            shutil.copyfile(origem, destino)

            # Abrir o arquivo Excel com xlwings
            app = xw.App(visible=False)
            workbook = app.books.open(destino)
            sheet = workbook.sheets[0]

            # Preencher os campos da planilha
            sheet['H5'].value = nome
            sheet['AH5'].value = data_admissao
            sheet['W5'].value = cpf
            sheet['U6'].value = setor
            sheet['V25'].value = tam_uniforme
            sheet['V26'].value = tam_sapato
            sheet['E6'].value = self.funcao_map_config.get(funcao, funcao.upper())

            # Buscar os itens de uniforme para a função selecionada
            db = Database()
            db.conecta()
            cursor = db.connection.cursor()
            cursor.execute("SELECT descricao FROM itens_funcao WHERE funcao = ?", (funcao,))
            itens_uniforme = cursor.fetchall()

            # Preencher os itens de uniforme nas células F25 a F31
            for index, item in enumerate(itens_uniforme, start=25):
                sheet[f'F{index}'].value = item[0]
                sheet[f'B{index}'].value = data_int
                sheet[f'X{index}'].value = 2 if index == 25 else 1

            # Salvar o arquivo Excel modificado preservando imagens
            workbook.save(destino)
            workbook.close()
            app.quit()

            # Limpar campos e mostrar mensagem de sucesso
            self.line_nome.clear()
            self.line_tam_uniforme.clear()
            self.line_tam_sapato.clear()
            self.line_cpf.clear()
            self.le_admissao.clear()
            self.le_integracao.clear()
            QMessageBox.information(self, "Sucesso", "Ficha realizada com sucesso!")

            # Inserir no log do banco de dados
            data_realizacao = datetime.today().strftime("%d/%m/%Y %H:%M")

            db.insert_epi_log(data_realizacao, nome, cpf, funcao, tam_sapato, tam_uniforme, setor, data_admissao, data_int)
            self.model.select()

        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Não foi possível confeccionar a ficha: {e}")
        finally:
            db.close_connection()
    def pesquisar_ficha(self):
        """Filtra a tabela por CPF ou nome"""
        
        self.cb_revazer_ficha
        pesquisa = self.cb_revazer_ficha.currentText()
        user = self.line_pesquisa_ficha.text()

        if pesquisa == "CPF":
            filtro = f"CPF LIKE '%{user}%'"
        else:
            filtro = f"Colaborador LIKE '%{user}%'"

        self.model.setFilter(filtro)
        self.model.select()
        

    def refazer_ficha(self):
        """Carrega os dados para refazer a ficha de EPI mantendo as imagens."""
        try:
            index = self.tw_historico_fichas.currentIndex()
            if index.isValid():
                row = index.row()
                nome = self.model.index(row, 2).data()
                cpf = self.model.index(row, 3).data()
                funcao = self.model.index(row, 4).data()
                tam_sapato = self.model.index(row, 5).data()
                tam_uniforme = self.model.index(row, 6).data()
                setor = self.model.index(row, 7).data()
                data_admissao = self.model.index(row, 8).data()
                data_int = self.model.index(row, 9).data()

                 # Caminho do arquivo original e do destino
                origem = "files//ficha_epi.xlsx"
                destino = f"{self.diretorio}/{data_admissao.replace('/', '_')}_{nome}.xlsx"

                shutil.copyfile(origem, destino)

                # Abrir o arquivo Excel com xlwings
                app = xw.App(visible=False)
                workbook = app.books.open(destino)
                sheet = workbook.sheets[0]

                # Preencher os campos da planilha
                sheet['H5'].value = nome
                sheet['AH5'].value = data_admissao
                sheet['W5'].value = cpf
                sheet['U6'].value = setor
                sheet['V25'].value = tam_uniforme
                sheet['V26'].value = tam_sapato
                sheet['E6'].value = self.funcao_map_config.get(funcao, funcao.upper())


                # Buscar itens de uniforme no banco de dados
                db = Database()
                db.conecta()
                cursor = db.connection.cursor()
                cursor.execute("SELECT descricao FROM itens_funcao WHERE funcao = ?", (funcao,))
                itens_uniforme = cursor.fetchall()

                # Preencher as células com os itens de uniforme e EPI
                for index, item in enumerate(itens_uniforme, start=25):
                    sheet[f'F{index}'].value = item[0]
                    sheet[f'B{index}'].value = data_int
                    sheet[f'X{index}'].value = 2 if index == 25 else 1
                # Salvar o arquivo modificado
                workbook.save(destino)
                workbook.close()
                app.quit()

                QMessageBox.information(self, "Sucesso", "Ficha refeita com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", "Nenhuma ficha selecionada.")

        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Não foi possível refazer a ficha: {e}")

    def log_epi(self):
        """Carrega o log de fichas EPI no QSqlTableModel."""
        # Evitar uso de conexões duplicadas
        if QSqlDatabase.contains("ficha_epi_db"):
            db = QSqlDatabase.database("ficha_epi_db")
        else:
            db = QSqlDatabase.addDatabase('QSQLITE', 'ficha_epi_db')

        # Definir o caminho correto do banco de dados
        db.setDatabaseName("files\\system.db")

        if not db.isOpen():
            if not db.open():
                QMessageBox.warning(self, "Erro", f"Erro ao abrir o banco de dados: {db.lastError().text()}")
                return

        self.model = QSqlTableModel(db=db)
        self.model.setTable("log_epi")
        self.tw_historico_fichas.setModel(self.model)

        # Definir cabeçalhos
        headers = ["ID", "Data Realização", "Colaborador", "CPF", "Função", "Sapato", "Uniforme", "Setor", "Data de Admissão", "Data Integração"]
        for index, header in enumerate(headers):
            self.model.setHeaderData(index, Qt.Horizontal, header)
        self.model.select()

        self.tw_historico_fichas.resizeColumnsToContents()

    def table_config(self):
        """Carrega as configurações de tabelas no QSqlTableModel."""
        # Evitar uso de conexões duplicadas
        if QSqlDatabase.contains("ficha_epi_db"):
            db = QSqlDatabase.database("ficha_epi_db")
        else:
            db = QSqlDatabase.addDatabase('QSQLITE', 'ficha_epi_db')

        db.setDatabaseName("files\\system.db")

        if not db.isOpen():
            if not db.open():
                QMessageBox.warning(self, "Erro", f"Erro ao abrir o banco de dados: {db.lastError().text()}")
                return

        # Modelos de tabela
        self.model_uniforme = QSqlTableModel(db=db)
        self.model_uniforme.setTable("itens_funcao")
        self.tv_funcao.setModel(self.model_uniforme)
        self.model_uniforme.select()

        # Definir cabeçalhos
        headers_uniforme = ['ID', 'Função', "Descrição"]
        for index, header in enumerate(headers_uniforme):
            self.model_uniforme.setHeaderData(index, Qt.Horizontal, header)

        self.model_funcao_map = QSqlTableModel(db=db)
        self.model_funcao_map.setTable("funcao_map")
        self.tv_funcao_2.setModel(self.model_funcao_map)
        self.model_funcao_map.select()

        # Definir cabeçalhos
        headers_funcao_map = ['ID', 'Função Original', "Função Mapeada"]
        for index, header in enumerate(headers_funcao_map):
            self.model_funcao_map.setHeaderData(index, Qt.Horizontal, header)

        self.model_setor = QSqlTableModel(db=db)
        self.model_setor.setTable("setores")
        self.tv_setor.setModel(self.model_setor)
        self.model_setor.select()

        # Definir cabeçalhos
        headers_setor = ['ID', 'Setor']
        for index, header in enumerate(headers_setor):
            self.model_setor.setHeaderData(index, Qt.Horizontal, header)

        self.tv_funcao_2.resizeColumnsToContents()
        self.tv_funcao.resizeColumnsToContents()
        self.tv_setor.resizeColumnsToContents()

    def pesquisar_uniforme(self):
        """Filtra a tabela por Função para o uniforme."""
        uniforme = self.le_pesquisa_config.text()
        filtro = f"funcao LIKE '%{uniforme}%'"
        self.model_uniforme.setFilter(filtro)
        self.model_uniforme.select()

    def pesquisar_funcao(self):
        """Filtra a tabela por função para o mapeamento."""
        funcao = self.le_pesquisa_config_2.text()
        filtro = f"funcao_original LIKE '%{funcao}%'"
        self.model_funcao_map.setFilter(filtro)
        self.model_funcao_map.select()

    def pesquisar_setor(self):
        """Filtra a tabela por setor."""
        setor = self.le_pesquisa_setor_config.text()
        filtro = f"setor LIKE '%{setor}%'"
        self.model_setor.setFilter(filtro)
        self.model_setor.select()

    def adicionar_item_funcao(self):
        """Adiciona um novo item à tabela itens_funcao."""
        funcao = self.le_add_func_config.text() or self.cb_select_func_config.currentText()
        descricao = self.le_add_uniforme_config.text()

        if funcao and descricao:
            db = Database()
            db.conecta()
            db.insert_itens_funcao(funcao, descricao)
            db.close_connection()

            # Atualiza a tabela
            self.model_uniforme.select()
            QMessageBox.information(self, "Sucesso", "Item adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos para adicionar o item.")

    def adicionar_setor(self):
        """Adiciona um novo setor à tabela setores."""
        setor = self.le_add_Setor_config.text()

        if setor:
            db = Database()
            db.conecta()
            db.insert_setores(setor)
            db.close_connection()

            # Atualiza a tabela
            self.model_setor.select()
            QMessageBox.information(self, "Sucesso", "Setor adicionado com sucesso!")
            self.le_add_Setor_config.clear()
        else:
            QMessageBox.warning(self, "Erro", "Preencha o campo para adicionar um setor.")

    def adicionar_funcao_map(self):
        """Adiciona uma nova função mapeada à tabela funcao_map."""
        funcao_original = self.le_funcao_original_config.text()
        funcao_map = self.le_funcao_ficha_config.text()
        if funcao_original and funcao_map:
            db = Database()
            db.conecta()
            db.insert_funcao_map(funcao_original, funcao_map)
            db.close_connection()

            self.model_funcao_map.select()
            self.le_funcao_original_config.clear()
            self.le_funcao_ficha_config.clear()
            QMessageBox.information(self, "Sucesso", "Adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Preencha os dois campos para adicionar.")

    def remover_item_funcao(self):
        """Remove o item selecionado da tabela itens_funcao."""
        index = self.tv_funcao.currentIndex()

        if index.isValid():
            row = index.row()
            funcao = self.model_uniforme.index(row, 1).data()
            descricao = self.model_uniforme.index(row, 2).data()

            if funcao and descricao:
                db = Database()
                db.conecta()
                cursor = db.connection.cursor()
                cursor.execute("DELETE FROM itens_funcao WHERE funcao = ? AND descricao = ?", (funcao, descricao))
                db.connection.commit()
                db.close_connection()

                # Atualiza a tabela
                self.model_uniforme.select()
                QMessageBox.information(self, "Sucesso", "Item removido com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", "Função ou descrição inválida.")
        else:
            QMessageBox.warning(self, "Erro", "Nenhum item selecionado.")

    def remover_funcao_map(self):
        """Remove item da tabela funcao_map."""
        index = self.tv_funcao_2.currentIndex()

        if index.isValid():
            row = index.row()
            funcao_original = self.model_funcao_map.index(row, 1).data()
            funcao_map = self.model_funcao_map.index(row, 2).data()

            if funcao_original and funcao_map:
                db = Database()
                db.conecta()
                cursor = db.connection.cursor()
                cursor.execute("DELETE FROM funcao_map WHERE funcao_original = ? AND funcao_mapeada = ?", (funcao_original, funcao_map))
                db.connection.commit()
                db.close_connection()

                self.model_funcao_map.select()
                QMessageBox.information(self, "Sucesso", "Função mapeada removida com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", "Função original ou mapeada inválida.")
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma função selecionada.")

 

    def remover_setor(self):
        """Remove o setor selecionado da tabela setores."""
        index = self.tv_setor.currentIndex()

        if index.isValid():
            row = index.row()
            setor = self.model_setor.index(row, 1).data()

            if setor:
                db = Database()
                db.conecta()
                cursor = db.connection.cursor()
                cursor.execute("DELETE FROM setores WHERE setor = ?", (setor,))
                db.connection.commit()
                db.close_connection()

                # Atualiza a tabela
                self.model_setor.select()
                QMessageBox.information(self, "Sucesso", "Setor removido com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", "Setor inválido.")
        else:
            QMessageBox.warning(self, "Erro", "Nenhum setor selecionado.")

    def remover_ficha(self):
        """Remove o item selecionado da tabela log_epi."""
        index = self.tw_historico_fichas.currentIndex()

        if index.isValid():
            row = index.row()
            id = self.model.index(row, 0).data()

            db = Database()
            db.conecta()
            cursor = db.connection.cursor()
            cursor.execute("DELETE FROM log_epi WHERE id = ?", (id,))
            db.connection.commit()
            db.close_connection()

            # Atualiza a tabela
            self.model.select()
            QMessageBox.information(self, "Sucesso", "Ficha removida com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Nenhum item selecionado.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())