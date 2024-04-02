-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-03-2024 a las 12:13:48
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `masterpodcast`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `thumbnails`
--

CREATE TABLE `thumbnails` (
  `id` int(11) NOT NULL,
  `podcast_id` int(11) NOT NULL,
  `url` varchar(1024) NOT NULL,
  `type` varchar(128) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `thumbnails`
--
ALTER TABLE `thumbnails`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `podcast_id` (`podcast_id`),
  ADD UNIQUE KEY `podcast_id_2` (`podcast_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `thumbnails`
--
ALTER TABLE `thumbnails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `thumbnails`
--
ALTER TABLE `thumbnails`
  ADD CONSTRAINT `thumbnails_ibfk_1` FOREIGN KEY (`podcast_id`) REFERENCES `podcasts` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
