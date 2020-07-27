CREATE TABLE IF NOT EXISTS StatusCombates(			-- Cada registro um possivel status final de combate
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	Status VARCHAR(255) NOT NULL,					-- descricao do status final do combate (finalizado / cartao preto / lesao / WO / etc)
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
);

INSERT INTO
	StatusCombates(Status)
VALUES
	("Finalizado"),
	("Lesao atleta 1"),
	("Lesao atleta 2"),
	("WO atleta 1"),
	("WO atleta 2"),
	("Cartao preto atleta 1"),
	("Cartao preto atleta 2")
;
