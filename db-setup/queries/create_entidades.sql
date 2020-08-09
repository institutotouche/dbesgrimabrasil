CREATE TABLE IF NOT EXISTS Entidades(			-- Cada registro uma entidade, incluindo a CBE, federacoes, EDPs, e outras instituicoes
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	RegistroCBE BIGINT,							-- Numero de registro na CBE
	Nome VARCHAR(255) NOT NULL,					-- Nome da instituicao
	Localidade VARCHAR(255),					-- Cidade
	Endereco VARCHAR(255),						-- Endereco exato
	Sigla VARCHAR(10),							-- Sigla
	IndexFiliacao BIGINT,						-- Indice de referencia a federacao a qual a instituicao eh filiada (referencia na mesma tabela)
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
