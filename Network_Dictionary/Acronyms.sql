-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 02, 2022 at 07:38 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Acronyms`
--

-- --------------------------------------------------------

--
-- Table structure for table `acronyms_en`
--

CREATE TABLE `acronyms_en` (
  `acronym` varchar(512) NOT NULL,
  `description` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `acronyms_en`
--

INSERT INTO `acronyms_en` (`acronym`, `description`) VALUES
('DNS', 'Domain Name Server is where the IP directions of the web are stored and matched with the name of the web.'),
('FTP', 'File Transfer Protocol its a protocol to send files between devices on a TCP network.'),
('HTTP', 'HyperText Transfer Protocol its a protocol to send hipermedia files, like HTML files.'),
('ICMP', 'Internet Control Message Protocol is a network layer protocol that detect errors in the network communication.'),
('IP', 'Internet Protocol is a protocol useful to enroute and redirect data packages.'),
('LAN', 'Its a group of computers connected to each other in a specific area, the connection can be wired or wireless.'),
('MAN', 'It connects al computers of an metropolitan network.'),
('OSI', 'It defines different communication layers between systems, and each layer has a specific function.'),
('PAN', 'Connects electronic devices close to the user, like a smartphone and a Bluetooth headset. '),
('QUIC', 'Quick UDP Internet Connections is a protocol created by Google and its like the UDP protocol but secure.'),
('SAN', 'Are networks dedicated to move large files with the objective of don\'t collapse the main network.'),
('TCP', 'Transmision Control Protocol its a slow transport protocol that tells the destination of the data package, what makes it secure.'),
('TCP/IP', 'It is a modern version of the OSI model, it have less layers.'),
('UDP', 'User Datagram Protocol its a fast transport protocol that works with IP and is not safe.'),
('VPN', 'Simulate a LAN between computers on diferent networks.'),
('WAN', 'It connects other networks with each other between countries and continents.'),
('WLAN', 'It is like a LAN but all the devices are wireless.');

-- --------------------------------------------------------

--
-- Table structure for table `acronyms_es`
--

CREATE TABLE `acronyms_es` (
  `acronym` varchar(512) NOT NULL,
  `description` varchar(512) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `acronyms_es`
--

INSERT INTO `acronyms_es` (`acronym`, `description`) VALUES
('DNS', 'Domain Name Server es donde se guardan las IP de las paginas web y se relacionan con su nombre.'),
('FTP', 'File Transfer Protocol  en un protocolo para enviar archivos entre dispositivos en una red TCP.'),
('HTTP', 'HyperText Transfer Protocol es un protocolo para enviar archivos de hypermedia, como archivos HTML.'),
('ICMP', 'Internet Control Message Protocol es un protocolo de capa de red que detecta errores en la comunicacion de la red.'),
('IP', 'Internet Protocol es un protocolo que sirve para enrutar y redireccionar paquetes de datos.'),
('LAN', 'Es un grupo de ordenadores conectados entre si en un area especifica, la conexion puede ser con o sin cables.'),
('MAN', 'Conecta todos los ordenadores en un area metropolitana.'),
('OSI', 'Define las diferentes capas de comunicacion entre sistemas, cada capa tiene su propia funcion.'),
('PAN', 'Conecta dispositivos electronicos cercanos al usuario, como un smartphone y unos auriculares Bluetooth.'),
('QUIC', 'Quick UDP Internet Connections es un protocolo creado por Google y es como el UDP pero seguro.'),
('SAN', 'Son redes dedicadas a transportar archivos pesados con el objetivo de no colapsar la red principal.'),
('TCP', 'Transmision Control Protocol es un protocolo de transporte lento que indica el destinatario del paquete de datos, lo que lo hace seguro.'),
('TCP/IP', 'Es una version modera del modelo OSI, tiene menos capas.'),
('UDP', 'User Datagram Protocol es un protocolo de transporte rapido que funciona mediante IP y no es seguro.'),
('VPN', 'Simula una LAN entre ordenadores en diferentes redes.'),
('WAN', 'Conecta diferentes redes entre paises y continentes.'),
('WLAN', 'Es como una LAN pero todos los dispositivos son inalambricos.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `acronyms_en`
--
ALTER TABLE `acronyms_en`
  ADD PRIMARY KEY (`acronym`);

--
-- Indexes for table `acronyms_es`
--
ALTER TABLE `acronyms_es`
  ADD PRIMARY KEY (`acronym`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
