CREATE TABLE IF NOT EXISTS Ranking(			-- Cada registro um atleta numa publicacao de ranking
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	DataPublicacao DATE,		-- Data de publicacao do ranking
	IndexAtleta BIGINT NOT NULL,						-- Referencia ao individuo
	Arma VARCHAR(255),		-- Espada / Florete / Sabre
	CategoriaIdade VARCHAR(255),	-- Livre / Cadete / Veterano, etc
	CategoriaCadeiraDeRodas VARCHAR(255),	-- A / B / C (NULL se não cadeirante)
	Sexo CHAR,		-- Sexo para combate, 'm' ou 'f'
	Pontos FLOAT,		-- Pontuacao do atleta no ranking publicado
	Ranking INT,		-- Posicao do atleta no ranking publicado
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
