CREATE TABLE IF NOT EXISTS Resultados(			-- Cada registro um atleta numa prova
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexProva BIGINT NOT NULL, 	-- Referencia a prova em que o resultado aconteceu
	IndexAtleta BIGINT,			-- Referencia ao individuo
	IndexEquipe BIGINT,			-- Referencia a equipe
	ColocacaoFinal INT NOT NULL,			-- Posicao final na prova
	CampeaoInvicto BOOLEAN,	-- TRUE se atleta/equipe tiver sido invicto(a)
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
