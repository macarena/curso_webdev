--
-- Estrutura para tabela `produtos`
--

CREATE TABLE `produtos` (
  `nome` varchar(30) NOT NULL,
  `valor` int(6) DEFAULT NULL,
  `qnt` int(3) NOT NULL,
  `descricao` varchar(400) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Fazendo dump de dados para tabela `produtos`
--

INSERT INTO `produtos` (`nome`, `valor`, `qnt`, `descricao`) VALUES
('abacate', 500, 10, 'Deliciosa fruta do verão!'),
('mouse sem fio', NULL, 2, NULL),
('controle remoto', 1900, 5, 'liga a tv'),
('caneta', 200, 199, 'escreve colorido'),
('teclado', 19900, 35, 'digita tudo');
