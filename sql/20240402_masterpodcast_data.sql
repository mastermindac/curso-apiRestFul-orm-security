-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-04-2024 a las 10:29:14
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
CREATE DATABASE IF NOT EXISTS `masterpodcast` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `masterpodcast`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `authors`
--

DROP TABLE IF EXISTS `authors`;
CREATE TABLE `authors` (
  `id` int(11) NOT NULL,
  `name` varchar(512) NOT NULL,
  `nationality` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `authors`
--

INSERT INTO `authors` (`id`, `name`, `nationality`) VALUES
(1, 'Christel Stansall', 'Dari'),
(2, 'Aksel Dmiterko', 'Punjabi'),
(3, 'Chadwick Rennicks', 'Khmer'),
(4, 'Waldon Elves', 'Marathi'),
(5, 'Erica Carreyette', 'Tok Pisin'),
(6, 'Noami Wallicker', 'Armenian'),
(7, 'Helenka Chamberlayne', 'Irish Gaelic'),
(8, 'Anne-corinne Instrell', 'Dari'),
(9, 'Anallese Markie', 'New Zealand Sign Language'),
(10, 'Petrina Simkovitz', 'Catalan');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `author_socialnetworks`
--

DROP TABLE IF EXISTS `author_socialnetworks`;
CREATE TABLE `author_socialnetworks` (
  `author_id` int(11) NOT NULL,
  `social_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'music'),
(2, 'technology'),
(3, 'food'),
(4, 'sports');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `episodes`
--

DROP TABLE IF EXISTS `episodes`;
CREATE TABLE `episodes` (
  `id` int(11) NOT NULL,
  `podcast_id` int(11) NOT NULL,
  `url` text NOT NULL,
  `season` int(11) NOT NULL,
  `episodes` int(11) NOT NULL,
  `title` varchar(512) NOT NULL,
  `description` varchar(2048) NOT NULL,
  `duration` int(11) NOT NULL,
  `creation_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `episodes`
--

INSERT INTO `episodes` (`id`, `podcast_id`, `url`, `season`, `episodes`, `title`, `description`, `duration`, `creation_date`) VALUES
(1, 5, 'https://xrea.com/sagittis/dui/vel/nisl/duis/ac/nibh.jsp', 3, 4, 'architect 24/365 infrastructures', 'Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.', 115, '2024-01-22'),
(2, 9, 'https://usnews.com/vestibulum/ac/est.json', 3, 8, 'engage mission-critical paradigms', 'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris. Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet.', 115, '2022-12-10'),
(3, 9, 'http://google.com.br/pellentesque/volutpat/dui/maecenas/tristique.xml', 2, 2, 'aggregate interactive e-markets', 'Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', 30, '2022-07-01'),
(4, 8, 'https://howstuffworks.com/quam/pede/lobortis/ligula/sit.json', 3, 1, 'deploy clicks-and-mortar methodologies', 'Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.', 33, '2023-10-17'),
(5, 7, 'https://jalbum.net/nec/euismod/scelerisque/quam/turpis/adipiscing.jpg', 2, 8, 'envisioneer best-of-breed deliverables', 'Nunc rhoncus dui vel sem. Sed sagittis.', 89, '2023-04-10'),
(6, 3, 'https://usa.gov/imperdiet/nullam.html', 2, 3, 'generate dynamic web services', 'Morbi vel lectus in quam fringilla rhoncus. Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus.', 49, '2022-05-22'),
(7, 1, 'https://merriam-webster.com/dui/luctus/rutrum/nulla/tellus.png', 1, 9, 'seize sticky infrastructures', 'Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.', 96, '2022-10-28'),
(8, 9, 'https://amazon.de/justo/maecenas.jpg', 2, 10, 'incubate cutting-edge partnerships', 'Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.', 73, '2023-06-06'),
(9, 8, 'http://vistaprint.com/nonummy/integer/non/velit/donec/diam.json', 3, 2, 'enable granular deliverables', 'Nulla tellus. In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.', 38, '2023-06-05'),
(10, 10, 'https://fema.gov/ultrices/phasellus/id/sapien.jpg', 2, 9, 'grow end-to-end models', 'Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.', 101, '2023-01-15'),
(11, 9, 'https://elegantthemes.com/suspendisse/ornare/consequat.js', 3, 5, 'envisioneer compelling mindshare', 'Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui. Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.', 44, '2023-10-20'),
(12, 8, 'http://pen.io/condimentum/id.html', 3, 1, 'harness plug-and-play convergence', 'Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh.', 33, '2023-05-31'),
(13, 9, 'https://sfgate.com/facilisi/cras/non/velit/nec/nisi/vulputate.png', 3, 7, 'e-enable collaborative metrics', 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat.', 85, '2022-02-11'),
(14, 3, 'https://dailymail.co.uk/curae/nulla/dapibus.png', 4, 5, 'reinvent bleeding-edge portals', 'Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat. Nulla nisl.', 61, '2022-10-19'),
(15, 10, 'http://com.com/sodales/sed.json', 2, 10, 'monetize holistic eyeballs', 'Nulla tempus. Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi.', 76, '2022-08-19'),
(16, 6, 'http://privacy.gov.au/tellus/nulla/ut/erat/id/mauris/vulputate.jsp', 1, 6, 'synergize enterprise eyeballs', 'Nullam varius. Nulla facilisi. Cras non velit nec nisi vulputate nonummy.', 66, '2023-12-07'),
(17, 9, 'http://businessweek.com/ut.png', 2, 8, 'aggregate best-of-breed schemas', 'In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.', 86, '2022-10-18'),
(18, 5, 'https://imageshack.us/vestibulum/sed/magna/at.png', 1, 6, 'harness end-to-end markets', 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.', 97, '2022-03-18'),
(19, 6, 'http://chron.com/blandit.jpg', 4, 2, 'orchestrate rich functionalities', 'Aliquam non mauris. Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem. Sed sagittis.', 102, '2023-01-24'),
(20, 8, 'http://rambler.ru/pharetra/magna/vestibulum/aliquet/ultrices/erat.html', 2, 9, 'orchestrate killer e-services', 'Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.', 113, '2022-10-29'),
(21, 4, 'https://ca.gov/in/hac/habitasse.aspx', 1, 5, 'incentivize extensible experiences', 'Mauris lacinia sapien quis libero.', 61, '2022-03-12'),
(22, 1, 'http://smh.com.au/augue/luctus/tincidunt/nulla/mollis/molestie.jpg', 1, 7, 'synergize strategic e-commerce', 'Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus. Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.', 114, '2022-01-25'),
(23, 4, 'http://fema.gov/hac/habitasse/platea/dictumst/morbi.png', 4, 3, 'strategize viral e-business', 'Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', 36, '2024-03-01'),
(24, 1, 'https://networksolutions.com/consequat/morbi.jpg', 2, 6, 'recontextualize integrated synergies', 'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris. Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet.', 63, '2022-12-15'),
(25, 3, 'http://bluehost.com/pellentesque/ultrices.aspx', 4, 6, 'seize granular initiatives', 'Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', 70, '2024-02-11'),
(26, 8, 'http://cpanel.net/posuere/nonummy/integer/non/velit/donec.js', 4, 8, 'repurpose intuitive action-items', 'Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt.', 89, '2022-10-07'),
(27, 9, 'http://toplist.cz/justo/aliquam/quis/turpis/eget.json', 1, 10, 'reinvent value-added mindshare', 'Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est. Phasellus sit amet erat.', 38, '2023-03-24'),
(28, 9, 'https://slate.com/sit/amet/eros/suspendisse/accumsan.jsp', 3, 4, 'cultivate magnetic markets', 'Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.', 32, '2023-11-18'),
(29, 9, 'http://jugem.jp/amet/sem/fusce.jsp', 1, 1, 'expedite end-to-end platforms', 'Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla.', 95, '2023-08-23'),
(30, 7, 'https://dropbox.com/posuere.jsp', 2, 4, 'integrate 24/7 platforms', 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.', 30, '2023-08-08'),
(31, 10, 'https://opera.com/ante/vivamus/tortor/duis/mattis.jpg', 3, 6, 'exploit distributed markets', 'Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim.', 43, '2023-09-21'),
(32, 7, 'http://princeton.edu/ligula/sit/amet/eleifend/pede.html', 2, 4, 'enhance real-time web-readiness', 'Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat. In congue. Etiam justo. Etiam pretium iaculis justo. In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus. Nulla ut erat id mauris vulputate elementum. Nullam varius.', 92, '2023-08-31'),
(33, 4, 'https://house.gov/curae/duis/faucibus.html', 1, 1, 'syndicate front-end initiatives', 'In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy.', 80, '2023-08-18'),
(34, 10, 'http://php.net/sollicitudin/mi/sit.png', 1, 4, 'revolutionize cutting-edge channels', 'Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus. Phasellus in felis. Donec semper sapien a libero.', 103, '2023-01-19'),
(35, 4, 'http://fc2.com/porttitor.xml', 4, 3, 'exploit transparent synergies', 'Pellentesque ultrices mattis odio. Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus. Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam. Nam tristique tortor eu pede.', 38, '2023-06-02'),
(36, 6, 'http://irs.gov/quam/sapien/varius.png', 3, 1, 'redefine proactive e-markets', 'Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus.', 85, '2022-10-15'),
(37, 1, 'http://scientificamerican.com/sapien/sapien/non/mi/integer/ac.xml', 4, 3, 'streamline dynamic web-readiness', 'Nullam molestie nibh in lectus.', 71, '2023-09-05'),
(38, 2, 'http://imdb.com/neque/vestibulum.xml', 1, 5, 'matrix granular relationships', 'Donec semper sapien a libero. Nam dui.', 52, '2022-10-07'),
(39, 5, 'https://oracle.com/blandit/mi/in/porttitor/pede.aspx', 2, 9, 'maximize 24/365 methodologies', 'Donec dapibus.', 43, '2023-11-10'),
(40, 1, 'http://histats.com/semper.html', 3, 3, 'innovate virtual platforms', 'Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl. Aenean lectus. Pellentesque eget nunc.', 69, '2024-03-05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `history`
--

DROP TABLE IF EXISTS `history`;
CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `episode_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `podcasts`
--

DROP TABLE IF EXISTS `podcasts`;
CREATE TABLE `podcasts` (
  `id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `title` varchar(512) NOT NULL,
  `description` varchar(2048) NOT NULL,
  `url` varchar(1024) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `podcasts`
--

INSERT INTO `podcasts` (`id`, `category_id`, `title`, `description`, `url`) VALUES
(1, 2, 'innovate end-to-end e-business', 'Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue.', 'http://buzzfeed.com/nisi/at/nibh/in.png'),
(2, 3, 'deliver vertical relationships', 'Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio.', 'http://cyberchimps.com/suspendisse/accumsan/tortor/quis/turpis/sed/ante.xml'),
(3, 2, 'orchestrate dot-com e-business', 'Proin eu mi.', 'https://networkadvertising.org/sit/amet/justo.png'),
(4, 2, 'orchestrate B2C e-services', 'Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl. Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.', 'http://wikia.com/sed/nisl/nunc/rhoncus/dui/vel/sem.js'),
(5, 2, 'visualize holistic convergence', 'Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus. Phasellus in felis. Donec semper sapien a libero. Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius. Integer ac leo.', 'http://mlb.com/in/blandit/ultrices/enim/lorem.jpg'),
(6, 1, 'mesh innovative solutions', 'Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', 'https://wordpress.com/dapibus.xml'),
(7, 3, 'transition holistic e-tailers', 'Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl. Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est. Phasellus sit amet erat.', 'http://google.fr/erat/nulla/tempus/vivamus/in/felis.jpg'),
(8, 2, 'target magnetic partnerships', 'Vivamus tortor. Duis mattis egestas metus. Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh. Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.', 'https://pcworld.com/bibendum.xml'),
(9, 4, 'matrix dynamic e-services', 'Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci.', 'http://disqus.com/ut/nunc/vestibulum/ante.js'),
(10, 4, 'generate end-to-end web services', 'Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl.', 'https://cornell.edu/luctus/ultricies/eu/nibh/quisque/id/justo.html');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `podcast_authors`
--

DROP TABLE IF EXISTS `podcast_authors`;
CREATE TABLE `podcast_authors` (
  `podcast_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `podcast_authors`
--

INSERT INTO `podcast_authors` (`podcast_id`, `author_id`) VALUES
(3, 3),
(4, 7),
(4, 8),
(5, 3),
(5, 4),
(6, 1),
(6, 3),
(7, 2),
(7, 3),
(7, 5),
(7, 9),
(8, 5),
(8, 8),
(9, 4),
(10, 4),
(10, 9),
(10, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socialnetworks`
--

DROP TABLE IF EXISTS `socialnetworks`;
CREATE TABLE `socialnetworks` (
  `id` int(11) NOT NULL,
  `link` varchar(1024) NOT NULL,
  `type` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `thumbnails`
--

DROP TABLE IF EXISTS `thumbnails`;
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
-- Indices de la tabla `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `author_socialnetworks`
--
ALTER TABLE `author_socialnetworks`
  ADD PRIMARY KEY (`author_id`,`social_id`),
  ADD KEY `social_id` (`social_id`);

--
-- Indices de la tabla `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `episodes`
--
ALTER TABLE `episodes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `podcast_id` (`podcast_id`);

--
-- Indices de la tabla `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `podcasts`
--
ALTER TABLE `podcasts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indices de la tabla `podcast_authors`
--
ALTER TABLE `podcast_authors`
  ADD PRIMARY KEY (`podcast_id`,`author_id`),
  ADD KEY `author_id` (`author_id`);

--
-- Indices de la tabla `socialnetworks`
--
ALTER TABLE `socialnetworks`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `thumbnails`
--
ALTER TABLE `thumbnails`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `podcast_id` (`podcast_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `authors`
--
ALTER TABLE `authors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `episodes`
--
ALTER TABLE `episodes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `podcasts`
--
ALTER TABLE `podcasts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `socialnetworks`
--
ALTER TABLE `socialnetworks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `thumbnails`
--
ALTER TABLE `thumbnails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `author_socialnetworks`
--
ALTER TABLE `author_socialnetworks`
  ADD CONSTRAINT `author_socialnetworks_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`),
  ADD CONSTRAINT `author_socialnetworks_ibfk_2` FOREIGN KEY (`social_id`) REFERENCES `socialnetworks` (`id`);

--
-- Filtros para la tabla `episodes`
--
ALTER TABLE `episodes`
  ADD CONSTRAINT `episodes_ibfk_1` FOREIGN KEY (`podcast_id`) REFERENCES `podcasts` (`id`);

--
-- Filtros para la tabla `podcasts`
--
ALTER TABLE `podcasts`
  ADD CONSTRAINT `podcasts_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);

--
-- Filtros para la tabla `podcast_authors`
--
ALTER TABLE `podcast_authors`
  ADD CONSTRAINT `podcast_authors_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`),
  ADD CONSTRAINT `podcast_authors_ibfk_2` FOREIGN KEY (`podcast_id`) REFERENCES `podcasts` (`id`);

--
-- Filtros para la tabla `thumbnails`
--
ALTER TABLE `thumbnails`
  ADD CONSTRAINT `thumbnails_ibfk_1` FOREIGN KEY (`podcast_id`) REFERENCES `podcasts` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
