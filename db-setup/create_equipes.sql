CREATE TABLE IF NOT EXISTS Equipes (					-- Cada registro uma equipe de uma entidade em uma prova
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexEntidade BIGINT NOT NULL,						-- Referencia a entidade na tabela de entidade
	IndexProva BIGINT NOT NULL, 	-- Referencia a prova em que o combate aconteceu
	IndexAtleta1 BIGINT,	-- Referencia atleta 1
	IndexAtleta2 BIGINT,	-- Referencia atleta 2
	IndexAtleta3 BIGINT,	-- Referencia atleta 3, caso exista
	IndexAtleta4 BIGINT,	-- Referencia atleta 4, caso exista
	IndexFonte BIGINT,									-- Indice de referencia da ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
