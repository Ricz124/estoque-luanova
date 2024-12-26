-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26/12/2024 às 16:29
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `produtos_db`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `produtos`
--

CREATE TABLE `produtos` (
  `prod_id` int(11) NOT NULL,
  `tipo_produto` varchar(100) DEFAULT NULL,
  `nome_produto` varchar(255) DEFAULT NULL,
  `medida` varchar(50) DEFAULT NULL,
  `revestimento` varchar(100) DEFAULT NULL,
  `cor_revestimento` varchar(50) DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `preco` float(10,2) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `observacao` text DEFAULT NULL,
  `prod_entrada` date DEFAULT NULL,
  `prod_saida` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `produtos`
--

INSERT INTO `produtos` (`prod_id`, `tipo_produto`, `nome_produto`, `medida`, `revestimento`, `cor_revestimento`, `quantidade`, `preco`, `estado`, `observacao`, `prod_entrada`, `prod_saida`) VALUES
(6, 'Colchão', 'LUCKSPUMA', '0.88m x 1.88m', '', '', 3, 175.00, 'Novo', '', '2024-12-26', NULL),
(7, 'Box', 'BOX FIXO', '0.88m x 1.88m', 'Suede', 'Cinza', 3, 145.00, 'Novo', '', '2024-12-26', NULL),
(8, 'Colchão', 'CASTOR', '1.88m x 2.40m', '', '', 1, 580.00, 'Novo', 'teste', '2024-12-26', NULL),
(9, 'Box', 'BOX BAU', '1.88m x 2.40m', 'Corino', 'Marrom', 4, 280.00, 'Novo', 'testestes', '2024-12-26', NULL),
(11, 'Cabiçeira', 'TAINA', '1.58m x 1.25m', 'Linhão', 'Branco', 1, 500.00, 'Mostruário', 'ndn', '2024-12-26', '2024-12-26');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`prod_id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `prod_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
