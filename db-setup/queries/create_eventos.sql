CREATE TABLE IF NOT EXISTS Eventos (					-- Cada registro um evento
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	Nome VARCHAR(255) NOT NULL,		-- Nome do evento
	TipoEvento VARCHAR(255),		-- Classificacao do evento (Campeonato, Torneio, Olimpíadas, "jogos")
	IndexEntidadeSede BIGINT,	-- Referencia a entidade que sediou o evento
	`Data` DATE,		-- Data de inicio do evento
	URL_fotos VARCHAR(255),	-- link para acesso a fotos do evento
	Formula VARCHAR(255),	-- Detalhes sobre a formula do evento quando disponivel / pertinente
	IndexFonte BIGINT,									-- Indice de referencia da ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
