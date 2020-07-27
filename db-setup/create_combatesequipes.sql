CREATE TABLE IF NOT EXISTS CombatesEquipes (					-- Cada registro um combate de 2 atletas num encontro entre equipes
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexProva BIGINT NOT NULL, 	-- Referencia a prova em que o combate aconteceu
	Rodada VARCHAR(255), 					-- Rodada da prova (Final, semi, Q8, Q16, poule, etc)
	Parcial INT,									-- Qual parcial do encontro corresponde o combate (número de 1 a 9 em encontros normais por equipes a 45 pontos)
	IndexEquipe1 BIGINT NOT NULL,	-- Referencia a equipe 1
	IndexEquipe2 BIGINT NOT NULL,	-- Referencia a equipe 2
	IndexAtleta1 BIGINT,	-- Referencia atleta da equipe 1
	IndexAtleta2 BIGINT,	-- Referencia atleta da equipe 2
	PontosEquipe1 INT,		-- Pontuacao da equipe 1 ao final desse combate
	PontosEquipe2 INT,		-- Pontuacao da equipe 2 ao final desse combate
	IndexArbitro BIGINT,	-- Referencia ao arbitro do combate
	IndexStatus BIGINT,		-- Referencia ao status final do combate
	IndexFonte BIGINT,									-- Indice de referencia da ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
