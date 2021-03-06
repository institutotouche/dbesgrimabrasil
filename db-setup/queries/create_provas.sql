CREATE TABLE IF NOT EXISTS Provas (					-- Cada registro uma prova dentro de um evento
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexEvento BIGINT NOT NULL,	-- Referencia ao evento
	Inicio_datetime DATETIME,		-- Horario de inicio
	Arma VARCHAR(15),		-- Espada / Florete / Sabre
	CategoriaIdade VARCHAR(50),	-- Livre / Cadete / Veterano, etc
	CategoriaCadeiraDeRodas CHAR,	-- A / B / C (NULL se não cadeirante)
	Sexo CHAR,		-- Sexo da prova, 'm' ou 'f'
	EquipeOuIndividual VARCHAR(15),	-- Equipe / Individual
	IndexFonte BIGINT,									-- Indice de referencia da ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
