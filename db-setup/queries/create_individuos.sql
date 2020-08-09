CREATE TABLE IF NOT EXISTS Individuos(			-- Cada registro um individuo
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	NumeroCBE BIGINT,							-- Numero de registro na CBE
	Nome VARCHAR(255) NOT NULL,					-- Nome do individuo
	DataNasc DATE,								-- Data de nascimento
 	DataInicioEsgrima DATE,				-- Data de inicio na esgrima em qualquer que tenha sido a primeira funcao
	NomeCombate VARCHAR(255),			-- Nome utilizado em competicao
	Sexo CHAR,										-- Sexo para competicao ('m' ou 'f')
	Nacionalidade VARCHAR(255),		-- Pais de nacionalidade
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
