CREATE TABLE IF NOT EXISTS PeriodosEPDs(			-- Cada registro um periodo em que uma EPD suportou a esgrima
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexEPD BIGINT NOT NULL,							-- Referencia a entidade
	Inicio DATE,				-- Data em que a institucao comecou a suportar esgrima
	Fim DATE,				-- Data em que instituicao deixou de suportar esgrima, NULL caso ainda suporte
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
