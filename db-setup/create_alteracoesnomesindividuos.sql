CREATE TABLE IF NOT EXISTS AlteracoesNomesIndividuos (					-- Cada registro uma alteracao no nome de um individuo
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexIndividuo BIGINT NOT NULL,						-- Referencia ao individuo
	DataAlteracao DATE,									-- Data da alteracao
	NomeAnterior VARCHAR(255),							-- Nome do individuo antes da alteracao
	NomeFinal VARCHAR,									-- Nome do individuo apos a alteracao (caso seja a ultima alteracao, deve corresponder ao nome na tabela Individuos)
	IndexFonte BIGINT,									-- Indice de referencia da ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
