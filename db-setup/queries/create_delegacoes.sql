CREATE TABLE IF NOT EXISTS Delegacoes(			-- Cada registro um individuo participando de um evento por uma entidade
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexEntidade BIGINT NOT NULL,						-- Referencia a entidade na tabela de entidade
	IndexEvento BIGINT NOT NULL,							-- Referencia ao evento
	IndexIndividuo BIGINT NOT NULL,						-- Referencia ao individuo
	Funcao VARCHAR(255),											-- Funcao assumida pelo individuo na delegacao (atleta, tecnico, diretor, massagista, etc)
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
