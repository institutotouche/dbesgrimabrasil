CREATE TABLE IF NOT EXISTS FontesInformacao(			-- Cada registro uma fonte de informacao que colaborou com o banco
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	Fonte VARCHAR(255) NOT NULL,					-- Nome / descrição da fonte
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
