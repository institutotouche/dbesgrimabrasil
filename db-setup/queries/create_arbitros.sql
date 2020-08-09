CREATE TABLE IF NOT EXISTS Arbitros(			-- Cada registro um individuo, certificado como arbitro ou que tenha arbitrado uma prova
	`Index` BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,	-- Indice primario da tabela
	IndexIndividuo BIGINT NOT NULL,						-- Referencia ao individuo
	CertifEspada DATE,							-- Data em que individuo foi certificado como arbitro de espada
	CertifFlorete DATE,							-- Data em que individuo foi certificado como arbitro de florete
	CertifSabre DATE,							-- Data em que individuo foi certificado como arbitro de sabre
	CertifEspadaCadeiraRodas DATE,							-- Data em que individuo foi certificado como arbitro de espada em cadeira de rodas
	CertifFloreteCadeiraRodas DATE,							-- Data em que individuo foi certificado como arbitro de florete em cadeira de rodas
	CertifSabreCadeiraRodas DATE,							-- Data em que individuo foi certificado como arbitro de sabre em cadeira de rodas
	IndexFonte BIGINT,							-- Indice de referencia a ultima fonte de informacao
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- Momento da ultima atualizacao
)
