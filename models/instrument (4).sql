-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 20 sep. 2019 à 23:54
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `mypython`
--

-- --------------------------------------------------------

--
-- Structure de la table `instrument`
--

DROP TABLE IF EXISTS `instrument`;
CREATE TABLE IF NOT EXISTS `instrument` (
  `ref` int(11) NOT NULL,
  `nominstr` varchar(50) NOT NULL,
  `prix` int(11) NOT NULL,
  `lieufab` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `nbvente` int(11) NOT NULL,
  `quantiteinit` int(11) NOT NULL,
  `sound` varchar(50) NOT NULL,
  PRIMARY KEY (`ref`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `instrument`
--

INSERT INTO `instrument` (`ref`, `nominstr`, `prix`, `lieufab`, `image`, `nbvente`, `quantiteinit`, `sound`) VALUES
(1256874, 'oud ', 700, 'maison de zeryeb', '2', 3, 50, '1'),
(1359875, 'oud', 500, 'dar oud korba', '1', 12, 80, '4'),
(1478469, 'oud', 3500, 'turkie', '3', 60, 100, '5'),
(2264857, 'piano', 8000, 'france', '4', 15, 30, '4'),
(3569874, 'piano', 10000, 'france', '1', 2, 10, '1'),
(4752145, 'violon', 250, 'italie', '1', 2, 27, ''),
(5471289, 'percussion', 60, 'tunisie', '1', 50, 150, '1'),
(6352417, 'percussion', 150, 'maroc', '2', 15, 160, ''),
(7788944, 'violon', 120, 'tunisie', '3', 70, 120, '2'),
(7862142, 'violon', 550, 'tunisie', '2', 5, 50, '1'),
(7896541, 'piano', 20000, 'france', '2', 1, 8, '2'),
(9638527, 'piano', 7500, 'france', '3', 20, 60, '3');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
