CREATE TABLE IF NOT EXISTS AlteracoesNomesEntidades (							-- Cada registro uma alteração no nome de uma entidade
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexEntidade BIGINT NOT NULL,						-- Referencia a entidade na tabela de entidade
	DataAlteracao DATE,									-- Data da alteracao
	NomeAnterior VARCHAR(255),							-- Nome da entidade antes da alteracao
	NomeFinal VARCHAR(255),									-- Nome da entidade apos a alteracao (caso seja a ultima alteracao, deve corresponder ao nome na tabela Entidade)
	IndexFonte BIGINT,									-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao

)
