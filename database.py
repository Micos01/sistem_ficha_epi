import sqlite3

class Database:
    def __init__(self, name="files//system.db"):
        self.name = name
        self.connection = None

    def conecta(self):
        """Estabelece a conexão com o Banco de Dados apenas se não estiver aberta."""
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.name)
            except sqlite3.Error as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                return False
        return True

    def close_connection(self):
        """Fecha a conexão com o Banco de Dados, se estiver aberta."""
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
            except sqlite3.Error as e:
                print(f"Erro ao fechar a conexão: {e}")

    def create_itens_funcao(self):
        """Cria a tabela de itens para a função fardamento, se não existir."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS itens_funcao (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        funcao TEXT,
                        descricao TEXT
                    )
                """)
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela itens_funcao: {e}")
            finally:
                self.close_connection()

    def create_setores(self):
        """Cria a tabela de setores, se não existir."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS setores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        setor TEXT
                    )
                """)
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela setores: {e}")
            finally:
                self.close_connection()

    def insert_setores(self, setor):
        """Insere um novo setor na tabela setores."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    INSERT INTO setores (setor) VALUES (?)
                """, (setor,))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir dados na tabela setores: {e}")
            finally:
                self.close_connection()

    def insert_itens_funcao(self, funcao, descricao):
        """Insere um novo item de função na tabela itens_funcao."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    INSERT INTO itens_funcao (funcao, descricao) VALUES (?, ?)
                """, (funcao, descricao))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir dados na tabela itens_funcao: {e}")
            finally:
                self.close_connection()

    def create_funcao_map(self):
        """Cria a tabela funcao_map, se não existir."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS funcao_map (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        funcao_original TEXT, 
                        funcao_mapeada TEXT
                    )
                """)
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela funcao_map: {e}")
            finally:
                self.close_connection()

    def insert_funcao_map(self, funcao_original, funcao_mapeada):
        """Insere uma nova função mapeada na tabela funcao_map."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    INSERT INTO funcao_map (funcao_original, funcao_mapeada) VALUES(?, ?)
                """, (funcao_original, funcao_mapeada))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir dados na tabela funcao_map: {e}")
            finally:
                self.close_connection()

    def create_log_epi(self):
        """Cria a tabela de log de fichas de EPI, se não existir."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS log_epi (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data_realizacao TEXT NOT NULL,
                        colaborador TEXT NOT NULL,
                        cpf TEXT NOT NULL,            
                        funcao TEXT NOT NULL,
                        tam_sapato TEXT NOT NULL,
                        tam_uniforme TEXT NOT NULL,
                        setor TEXT NOT NULL,
                        data_admissao TEXT NOT NULL,
                        data_integracao TEXT NOT NULL
                    )
                """)
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela log_epi: {e}")
            finally:
                self.close_connection()

    def insert_epi_log(self, data_realizacao, colaborador, cpf, funcao, tam_sapato, tam_uniforme, setor, data_admissao, data_integracao):
        """Insere um novo log de EPI na tabela log_epi."""
        if self.conecta():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    INSERT INTO log_epi (data_realizacao, colaborador, cpf, funcao, tam_sapato, tam_uniforme, setor, data_admissao, data_integracao)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (data_realizacao, colaborador, cpf, funcao, tam_sapato, tam_uniforme, setor, data_admissao, data_integracao))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Erro ao inserir dados na tabela log_epi: {e}")
            finally:
                self.close_connection()


if __name__ == "__main__":
    db = Database()
    db.conecta()
    db.create_log_epi()
    db.create_itens_funcao()
    db.create_funcao_map()
    db.create_setores()
    db.close_connection()