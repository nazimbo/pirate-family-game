-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 02 juil. 2023 à 21:41
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `pirate-family`
--

-- --------------------------------------------------------

--
-- Structure de la table `game_sessions`
--

DROP TABLE IF EXISTS `game_sessions`;
CREATE TABLE IF NOT EXISTS `game_sessions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `fk_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`fk_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `name`, `email`) VALUES
(1, 'francis', 'francis@email.com'),
(2, 'Francis Scaringella', 'francis@test.com'),
(3, 'Francis Scaringella', 'francis@test.com'),
(4, 'le jeux commence', 'mec@email.com'),
(5, 'ChatBot Python', 'jdelafontaine@email.com'),
(6, 'dsfsdf', 'sdfds@gmail.com'),
(7, 'fsdfsf', 'dfds@gmail.com'),
(8, 'Francis', 'Scar@gmail.com'),
(9, 'John Doe', 'johndoe@example.com'),
(10, 'sdfsd', 'sf@gmail.com'),
(11, 'John Doe', 'johndoe@example.com'),
(12, 'John Doe', 'johndoe@example.com'),
(13, 'John Doe', 'johndoe@example.com'),
(14, 'John Doe', 'johndoe@example.com'),
(15, 'John Doe', 'johndoe@example.com'),
(16, 'John Doe', 'johndoe@example.com'),
(17, 'John Doe', 'johndoe@example.com'),
(18, 'John Doe', 'johndoe@example.com'),
(19, 'John Doe', 'johndoe@example.com'),
(20, 'John Doe', 'johndoe@example.com'),
(21, 'John', 'john@example.com'),
(22, 'John', 'john@example.com'),
(23, 'dfdsf', 'sddsf@gmail.com'),
(24, 'John', 'john@example.com'),
(25, 'John', 'john@example.com'),
(26, 'John', 'john@example.com'),
(27, 'John', 'john@example.com'),
(28, 'John', 'john@example.com'),
(29, 'John', 'john@example.com'),
(30, 'Francis', 'jdelafontaine@email.com'),
(31, 'dffds', 'dsfdsf@gmail.com'),
(32, 'dfsdf', 'dsfsd@gmail.com'),
(33, 'Francis Scaringella', 'jdelafontaine@email.com'),
(34, 'oiuoiu', 'frfre@gmail.com'),
(35, 'John Doe', 'johndoe@example.com'),
(36, 'John', 'john@example.com'),
(37, 'dsf', 'dsfsfd@gmail.com'),
(38, 'dsfdsf', 'sdfdsf@gmail.com'),
(39, 'dsdfd', 'dfsdf@gmail.com'),
(40, 'John', 'john@example.com');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `game_sessions`
--
ALTER TABLE `game_sessions`
  ADD CONSTRAINT `game_sessions_ibfk_1` FOREIGN KEY (`fk_user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
