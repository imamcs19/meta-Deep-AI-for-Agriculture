-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 14 Mar 2016 pada 14.24
-- Versi Server: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ptvpso` 
-- pwd: x6X7eGs7t8bmDZp
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `batasmaxpupuk`
--

CREATE TABLE IF NOT EXISTS `batasmaxpupuk` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kode` varchar(20) NOT NULL,
  `NPK` double NOT NULL,
  `urea-1` double NOT NULL,
  `sp36-1` double NOT NULL,
  `kcl-1` double NOT NULL,
  `urea-2` double NOT NULL,
  `urea-3` double NOT NULL,
  `kcl-3` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data untuk tabel `batasmaxpupuk`
--

INSERT INTO `batasmaxpupuk` (`id`, `kode`, `NPK`, `urea-1`, `sp36-1`, `kcl-1`, `urea-2`, `urea-3`, `kcl-3`) VALUES
(1, 'T-org', 0, 60, 100, 50, 120, 120, 50),
(2, 'T+jer', 0, 56, 100, 25, 112, 112, 25),
(3, 'T+ppk', 0, 55, 50, 40, 110, 110, 40),
(4, 'M15:15:15', 250, 35, 0, 37.5, 70, 70, 37.5),
(5, 'M10:10:10', 350, 40, 0, 37.5, 80, 80, 37.5),
(6, 'M30:6:8', 350, 5, 50, 25, 10, 10, 25),
(7, 'T-gogo', 0, 60, 200, 75, 120, 120, 75);

-- --------------------------------------------------------

--
-- Struktur dari tabel `batasminpupuk`
--

CREATE TABLE IF NOT EXISTS `batasminpupuk` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `kode` varchar(20) NOT NULL,
  `NPK` double NOT NULL,
  `urea-1` double NOT NULL,
  `sp36-1` double NOT NULL,
  `kcl-1` double NOT NULL,
  `urea-2` double NOT NULL,
  `urea-3` double NOT NULL,
  `kcl-3` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kode` (`kode`),
  UNIQUE KEY `kode_2` (`kode`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data untuk tabel `batasminpupuk`
--

INSERT INTO `batasminpupuk` (`id`, `kode`, `NPK`, `urea-1`, `sp36-1`, `kcl-1`, `urea-2`, `urea-3`, `kcl-3`) VALUES
(1, 'T-org', 0, 50, 50, 25, 100, 100, 25),
(2, 'T+jer', 0, 46, 50, 0, 92, 92, 0),
(3, 'T+ppk', 0, 45, 0, 15, 90, 90, 15),
(4, 'M15:15:15', 150, 30, 0, 0, 60, 60, 0),
(5, 'M10:10:10', 200, 30, 0, 0, 60, 60, 0),
(6, 'M30:6:8', 300, 0, 0, 0, 0, 0, 0),
(7, 'T-gogo', 0, 40, 125, 50, 80, 80, 50);

-- --------------------------------------------------------

--
-- Struktur dari tabel `hargapupuk`
--

CREATE TABLE IF NOT EXISTS `hargapupuk` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `pupuk` varchar(20) NOT NULL,
  `harga` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data untuk tabel `hargapupuk`
--

INSERT INTO `hargapupuk` (`id`, `pupuk`, `harga`) VALUES
(1, 'urea', 1800),
(2, 'sp36', 2000),
(3, 'kcl', 5600),
(4, 'npk15:15:15', 2300),
(5, 'npk10:10:10', 2300),
(6, 'npk30:6:8', 2300);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pilihanpest`
--

CREATE TABLE IF NOT EXISTS `pilihanpest` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `kode` varchar(20) NOT NULL,
  `OPT` varchar(30) NOT NULL,
  `bahan_aktif` varchar(50) NOT NULL,
  `nama_dagang` varchar(50) NOT NULL,
  `harga` int(50) NOT NULL,
  `minKonsentrasi` double NOT NULL,
  `maxKonsentrasi` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data untuk tabel `pilihanpest`
--

INSERT INTO `pilihanpest` (`id`, `kode`, `OPT`, `bahan_aktif`, `nama_dagang`, `harga`, `minKonsentrasi`, `maxKonsentrasi`) VALUES
(1, 'wc', 'wereng coklat', 'dimehipo 290 g/l', 'spartan 290 SL', 11440, 0.5, 1),
(2, 'pb', 'penggerek batang', 'BPMC 500 g/l', 'greta 500 EC', 17600, 0.75, 1),
(3, 'ws', 'walang sangit', 'imidakloprid 10%', 'klopindo 10 WP', 27500, 0.2, 0.4),
(4, 'hw', 'hawar', 'bakterisida', 'indokor 250 EC', 30976, 0.25, 0.5),
(5, 'bd', 'bercak daun', 'bakterisida', 'indokor 250 EC', 30976, 0.5, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pilihanpupuk`
--

CREATE TABLE IF NOT EXISTS `pilihanpupuk` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `kode` varchar(20) NOT NULL,
  `kombpupuk` varchar(15) NOT NULL,
  UNIQUE KEY `id` (`id`,`kombpupuk`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data untuk tabel `pilihanpupuk`
--

INSERT INTO `pilihanpupuk` (`id`, `kode`, `kombpupuk`) VALUES
(1, 'T-org', '-organik'),
(2, 'T+jer', '+jerami'),
(3, 'T+ppk', '+ppk'),
(4, 'M15:15:15', '+NPK 15:15:15'),
(5, 'M10:10:10', '+NPK 10:10:10'),
(6, 'M30:6:8', '+NPK 30:6:8'),
(7, 'T-gogo', 'Padi Gogo');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
