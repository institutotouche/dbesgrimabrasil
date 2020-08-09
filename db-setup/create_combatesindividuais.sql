CREATE TABLE IF NOT EXISTS CombatesIndividuais (					-- Cada registro um combate entre 2 atletas
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexProva BIGINT NOT NULL, 	-- Referencia a prova em que o combate aconteceu
	Rodada VARCHAR(255), 					-- Rodada da prova (Final, semi, Q8, Q16, poule, etc)
	IndexAtleta1 BIGINT,	-- Referencia atleta 1
	IndexAtleta2 BIGINT,	-- Referencia atleta 2
	PontosAtleta1 INT,		-- Pontuacao atleta 1 ao final desse combate
	PontosAtleta2 INT,		-- Pontuacao atleta 2 ao final desse combate
	IndexArbitro BIGINT,	-- Referencia ao arbitro do combate
	IndexStatus BIGINT DEFAULT 0,		-- Referencia ao status final do combate (por padrao, assume combate finalizado)
	IndexFonte BIGINT,									-- Indice de referencia da ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Momento da ultima atualizacao
)
