CREATE TABLE IF NOT EXISTS FiliacaoTecnicos(			-- Cada registro um ano em que um tecnico foi filiado a uma entidade
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexIndividuo BIGINT NOT NULL,						-- Referencia ao tecnico na tabela de individuos
	IndexEntidade BIGINT NOT NULL,						-- Referencia a entidade na tabela de entidade
	Ano INT,																	-- Ano de filiacao
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
