-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 24, 2025 at 07:02 AM
-- Server version: 10.6.20-MariaDB-cll-lve
-- PHP Version: 8.1.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `csdm`
--

-- --------------------------------------------------------

--
-- Table structure for table `advancedlevel`
--

CREATE TABLE `advancedlevel` (
  `id` int(11) NOT NULL,
  `team_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `member_1_number` varchar(50) NOT NULL,
  `team_member_2_name` varchar(100) DEFAULT NULL,
  `submission_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `advancedlevel`
--

INSERT INTO `advancedlevel` (`id`, `team_name`, `email`, `member_1_number`, `team_member_2_name`, `submission_date`) VALUES
(3, 'Hgg', '22ht1a4425@gmail.com', 'Ggg', 'Hgy', '2024-10-24 04:00:34'),
(4, 'Tech Inventors', '21ht1a4442@gmail.com', 'Harika Mullangi', 'Peeka Amulya', '2024-10-24 06:54:09'),
(5, 'Tech Quires', 'tejaswinigutta009@gmail.com', '8309094057', 'M Tejaswini', '2024-10-24 06:54:44'),
(6, 'Tony Stark', 'charankolli573@gmail.com', '9490651712', 'ravi', '2024-10-24 06:57:08'),
(7, 'Search Bar', '21ht1a4652@gmail.com', '9392543913', 'SHAIK RAHAMTULLA', '2024-10-24 06:57:56'),
(8, 'prasannanavya', 'navyagujjula93@gmail.com', '21HT1A4425', 'B.lakshmi prasanna', '2024-10-24 06:58:26'),
(9, 'Code Admires', '22ht1a4412@gmail.com', 'B Lakshmi ', '', '2024-10-24 06:59:22'),
(10, 'GR gems', 't.gurumani456@gmail.com', '7780154210', 'Rohith', '2024-10-24 06:59:49'),
(11, 'white eagles', 'peddik029@gmail.com', '7013726251', 'krishna charan', '2024-10-24 07:00:02'),
(12, 'heck street', 'popuricharan2004@gmail.com', '7382617128', 'N.Tirupathi', '2024-10-24 07:00:25'),
(13, 'Tech Thinckers', 'shaikabdulnabi2004@gmail.com', '9346022080', 'Shaik Abdul Nabi', '2024-10-24 07:01:01'),
(14, 'Imran\'s Team', '23ht1a44b0@gmail.com', '9908571735', 'P Imran khan', '2024-10-24 07:01:06'),
(15, 'Imran\'s Team', '23ht1a44b0@gmail.com', '9908571735', 'P Imran khan', '2024-10-24 07:01:06'),
(16, 'DK', 'sravanthidevarapu9@gmail.com', '7989074330', 'Kavya sri', '2024-10-24 07:01:59'),
(17, 'Bro code', 'divyatejasunke@gmail.com', '8247421933', 'Tella Eswar Chandra Prasad', '2024-10-24 07:02:26'),
(18, 'FS', 'farhanabegumpatan@gmail.com', 'Farhana begum ', 'Siva Kumari ', '2024-10-24 07:02:44'),
(19, 'FS', 'farhanabegumpatan@gmail.com', 'Farhana begum ', 'Siva Kumari ', '2024-10-24 07:02:44'),
(20, 'DP', 'dileepdavuluri1@gmail.com', '7995537427', 'Pavan', '2024-10-24 07:02:47'),
(21, 'hackstreetboys2', 'vinodbandaru51@gmail.com', '7093808751', 'k.vamsi', '2024-10-24 07:02:49'),
(22, 'dynamic duo', 'jmohankrishna379@gmail.com', '8688110169', '', '2024-10-24 07:02:59'),
(23, 'childish BATCH', 'dharshipuli@gmail.com', 'lakshmidhar', 'rohith', '2024-10-24 07:03:34'),
(24, 'code splitz', 'srinivasbasivila13@gmail.com', '9347491842', 'srinivas', '2024-10-24 07:03:48'),
(25, 'MKM', 'raghunadharao157@gmail.com', 'Kotaru Mani', 'Kolagani Meghana', '2024-10-24 07:04:23'),
(26, 'chalapathi guys', 'pradeepsai867@gmail.com', 'Sodagudi Sai Pradeep', 'Shaik Galishid', '2024-10-24 07:04:33'),
(27, 'SN', 'balisettisasisasi@gmail.com', '9581265470', 'J.Neha', '2024-10-24 07:04:38'),
(28, 'ENGINEERS', 'mylamallikharjunreddy6@email.com', '9515606359', 'Myla.LakshmiMallikharjun Reddy', '2024-10-24 07:04:40'),
(29, 'coding developers', 'premarajua7@gmail.com', '8341052032', '', '2024-10-24 07:04:58'),
(30, 'sinister', 'dineshguntupalli9720@gmail.com', 'Dinesh.', '', '2024-10-24 07:05:01'),
(31, 'Techei Wizards', '22ht1a05b8@gmail.com', 'Peruboina Venkata Sai', 'Perumalla Venkata Naga Dhanush', '2024-10-24 07:05:13'),
(32, 'Techei Wizards', '22ht1a05b8@gmail.com', 'Peruboina Venkata Sai', 'Perumalla Venkata Naga Dhanush', '2024-10-24 07:05:14'),
(33, 'sinister', 'dineshguntupalli9720@gmail.com', 'Dinesh.G', 'Sasikanth.K', '2024-10-24 07:05:18'),
(34, 'lovaraju-subbu', 'subramanyamachyutha2002@gmail.com', '9704831099', 'Subramanyam', '2024-10-24 07:05:35'),
(35, 'code ruler', 'joshnatirumalasetty@gmail.com', '9346736744', 'kasiragavendra Suda', '2024-10-24 07:06:02'),
(36, 'Bigboss', '22ht1a0552@gmail.com', '7306270812', 'CHALLA VASISHTA', '2024-10-24 07:06:10'),
(37, 'MASTER MINDS', 'balajigunji2004@gmail.com', 'GUNJI BALAJI', 'Gudala Ajay Kumar Reddy ', '2024-10-24 07:06:47'),
(38, 'dreams hack', 'fathersdaughter2004@gmail.com', 'Divi Anusha', 'Gali Likitha', '2024-10-24 07:06:49'),
(39, 'TeamArnold2', 'ysaichaitany33@gmail.com', 'Sai Chaitanya Yerramsetty ', 'Subbarao Payyavula', '2024-10-24 07:07:03'),
(40, 'Code Crackers', '22ht1a6159@gmail.com', 'VARIKUTI CHINNA KOTESWARA RAO', 'KAMBHAM JAGADISH', '2024-10-24 07:07:17'),
(41, 'code boosters', 'nithinrajuchilaka@gmail.com', 'chilaka.Nithinraju', 'janamala.gurumurthy', '2024-10-24 07:07:18'),
(42, 'AI2', '23ht1a4371@gmail.com', '9100637856', 'N.sivabrahmaiah', '2024-10-24 07:07:24'),
(43, 'shakti team', 'gayatripendyala555@gmail.com', '9533077555', '', '2024-10-24 07:07:25'),
(44, 'code engineers', 'ananthalakshmivemala@gmail.com', 'vemala.Anantha Lakshmi', 'sri pallavi.somana', '2024-10-24 07:07:27'),
(45, 'mech x4', 'saikumarchapparla@gmail.com', 'ch sai kumar', 'ch ram sharan', '2024-10-24 07:07:47'),
(46, 'chalapathi warriors', '22ht1a0538@gmail.com', 'G.Yona', 'H.Prasannaanjaneyulu', '2024-10-24 07:07:50'),
(47, 'UNBEATABLE CODERS', '22ht1a43b8@gmail.com', 'vangapati manikanta', 'panga meghana', '2024-10-24 07:07:51'),
(48, 'harinadh squad', 'saisriramassr@gmail.com', 'A.saisriram', 'K.venkateswarlu', '2024-10-24 07:08:02'),
(49, 'Immortals', 'bhavyanth33@gmail.com', '8639714155', '7382223355', '2024-10-24 07:08:03'),
(50, 'spark', 'swaroopyelchuri25@gmail.com', 'swaroop', 'k.yagnesh', '2024-10-24 07:08:09'),
(51, 'unbeatable performers', 'perlamaneesha9515@gmail.com', 'P.Sabiya', 'P.Maneesha', '2024-10-24 07:08:12'),
(52, 'unbeatable performers', 'perlamaneesha9515@gmail.com', 'P.Sabiya', 'P.Maneesha', '2024-10-24 07:08:13'),
(53, 'CSE-B', 'saibhargav012@gmail.com', '9133251944', 'MUSTHAKHEEM', '2024-10-24 07:08:20'),
(54, 'PRAVEEN CYBER', '23ht1a4612@gmail.com', '9542644826', '7993543315', '2024-10-24 07:08:24'),
(55, 'artificial intelligence', 'nandeeswar4341@gmail.com', 'nandeeswar kambhampati', 'goddanti gowtham', '2024-10-24 07:08:40'),
(56, 'benchmark', '22ht1a4302@gmail.com', '9963284950', 'devisriprasad', '2024-10-24 07:08:40'),
(57, 'Hunters', 'avinashavinash24576@gmail.com', 'Chirra Lok Sai Avinash Reddy', 'Kalluri Venkata Guru Prasad', '2024-10-24 07:08:42'),
(58, 'code generaters', 'krishnanagavenkat11@gmail.com', 'krishna', 'raja kumar', '2024-10-24 07:09:08'),
(59, 'cse c', 'charansaip7@gmail.com', '7799434071', 'B.omkar abhiram sai', '2024-10-24 07:09:50'),
(60, 'AI TEAM ', '23ht1a43c2@gmail.com', 'v.sagarika', '', '2024-10-24 07:10:02'),
(61, 'hack street boys', 'vamsikrishnaneelam111@gmail.com', 'vamsi krishna neelam ', 'p venkata narayana', '2024-10-24 07:10:10'),
(62, 'Introverts', 'sushmithachakka07@gmail.com', '9014121695', 'krishna chaitanya', '2024-10-24 07:10:31'),
(63, 'city boys', 'prathapreddy5438@gmail.com', 'k.prathap reddy', 'j.venkatesh', '2024-10-24 07:10:42'),
(64, 'code hunt', 'praveenvasarla407@gmail.com', '7780730596', 'praveen', '2024-10-24 07:10:44'),
(65, 'chandbasha', 'chandbashas944@gmail.com', '9392670826', 'V.Venkata Sai Tejesh', '2024-10-24 07:10:48'),
(66, 'Bugatti', 'thouhidshaik614@gmail.com', '9492439097', 's. raghu prem sai', '2024-10-24 07:11:50'),
(67, 'NARUTO UZUMAKI', 'joshuaswaraj@gmail.com', 'PULIPATI JOSHUA SWARAJ', 'MALLE GANESH', '2024-10-24 07:12:02'),
(68, 'ks', 'kuchipuismitha@gmail.com', '8074938131', '', '2024-10-24 07:12:22'),
(69, 'AI SQUAD', 'natanigunasri@gmail.com', 'natani Guna Sri durga priya', 'shaik mehar nigar', '2024-10-24 07:12:34'),
(70, 'saidha-charan', 'saidhaiba45@gmail.com', '6301785751', 'y.prabhu charan', '2024-10-24 07:12:52'),
(71, 'xcution', 'dnlppavan@gmail.com', '9121263887', 'Challa Venkata Krishna', '2024-10-24 07:14:27'),
(72, 'Techies', 'venkatasai2409@gmail.com', '6301770869', 'Gopi Krishna', '2024-10-24 07:14:41'),
(73, 'N.venkateswararao', '23ht1a4376@gmail.com', '7989361070', 'shaik Nailo Rajak', '2024-10-24 07:15:52'),
(74, 'code creators', 'gudipudivijaybabu123@gmail.com', 'Vijay babu Gudipudi', 'Bandaru.Kiranmai', '2024-10-24 07:15:52'),
(75, 'next era', 'namburikowshitha@gmail.com', 'N.kowshitha', 'P.pavani', '2024-10-24 07:16:50'),
(76, 'R K GANG', 'raviteja.a7786@gmail.com', '9030177886', 'B.venkata krishna', '2024-10-24 07:16:57'),
(77, 'Debugging Ninjas', 'chembetimanohar4@gmail.com', '6281547857', 'A.Dinesh', '2024-10-24 07:17:05'),
(78, 'Modern  Moggers', '22ht1a4304@gmail.com', '6303438791', 'hemanth.k', '2024-10-24 07:17:46'),
(79, 'code creators 1', '23ht1a6114@gmail.com', 'DASARI AMARNADH', 'AYILAPOGU PRAVEEN', '2024-10-24 07:18:48'),
(80, 'Team Dynamic ii', '22ht1a4307@gmail.com', 'Arimalla Anil', 'Jaggarapu Sravan', '2024-10-24 07:19:20'),
(81, 'cse', 'shaikasif@gmail.com', '8179445299', '9493996124', '2024-10-24 07:19:31'),
(82, 'AI TECHNO SPARKS', '23ht1a4345@gmail.com', '6301361169', 'Chigine  Pallavi', '2024-10-24 07:19:54'),
(83, 'manoj kumar', 'ramadevimunirathnam@gmail.com', 'mounika nagappagari', 'ch manoj kumar', '2024-10-24 07:21:09'),
(84, 'code chefs', '23ht1a6135@gmail.com', 'PATAN NAJEER KHAN', 'MASEEDU ASIF KAREEM', '2024-10-24 07:21:14'),
(85, 'HONEST CREATERS', '22HT1A4624@gmail.com', 'GOLLAPALLI RAVEENDRA', 'KUKKALA  NAVEEN', '2024-10-24 07:22:51'),
(86, 'AI Code Crackers', '22ht1a4312@gmail.com', '7893141028', 'Pujithasri Chinthapalli', '2024-10-24 07:24:37'),
(87, 'AK', 'faiyazahamedsyedgnt@gmail.com', 'SD.Faiyaz', 'T.Anand', '2024-10-24 07:27:32'),
(88, 'data science', '23ht1a4439@gmail.com', 'g venu', 'g vishnu', '2024-10-24 07:30:29'),
(89, 'N.VAMSI', 'nadimintivamsi7780@gmail.com', 'vamsi', 'divya', '2024-10-24 07:34:06'),
(90, 'sirikavya', 'dongarisirisha600@gmail.com', 'kavya', 'sirisha', '2024-10-24 08:26:00'),
(91, 'sirikavya', 'dongarisirisha600@gmail.com', 'kavya', 'sirisha', '2024-10-24 08:26:01'),
(92, 'sirikavya', 'dongarisirisha600@gmail.com', 'kavya', 'sirisha', '2024-10-24 08:26:02'),
(93, 'sirikavya', 'dongarisirisha600@gmail.com', 'kavya', 'sirisha', '2024-10-24 08:26:02'),
(94, 'sirikavya', 'dongarisirisha600@gmail.com', 'kavya', 'sirisha', '2024-10-24 08:26:02'),
(95, 'hackers', '22ht1a0513@gmail.com', '7036046651', 'PAVAN KRISHNA', '2024-10-24 08:34:35'),
(96, 'FTUGYIK,UOYUO', 'VJYUT78IY70@gmail.com', '578769GNJUH', 'B,IYUG', '2024-10-24 09:02:43');

-- --------------------------------------------------------

--
-- Table structure for table `alerts`
--

CREATE TABLE `alerts` (
  `id` int(11) NOT NULL,
  `alert_type` varchar(255) NOT NULL,
  `alert_date` date NOT NULL,
  `alert_time` time NOT NULL,
  `alert_area` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alerts`
--

INSERT INTO `alerts` (`id`, `alert_type`, `alert_date`, `alert_time`, `alert_area`) VALUES
(1, 'Earthquake', '2025-01-22', '04:25:00', 'Chalapathi institute of technology '),
(2, 'Earthquake', '2025-01-22', '04:25:00', 'Chalapathi institute of technology '),
(3, '', '0000-00-00', '00:00:00', '');

-- --------------------------------------------------------

--
-- Table structure for table `alert_history`
--

CREATE TABLE `alert_history` (
  `id` int(11) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `alert_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alert_history`
--

INSERT INTO `alert_history` (`id`, `latitude`, `longitude`, `alert_time`) VALUES
(1, 16.4155732, 80.4514168, '2024-09-02 06:23:18'),
(2, 16.463185, 80.4043253, '2024-09-25 10:03:33'),
(3, 12.9774411, 77.5700018, '2024-09-25 14:17:47'),
(4, 16.5475012, 80.1367523, '2024-10-07 09:10:07'),
(6, 23.592810828003564, 72.95955033594934, '2025-01-05 15:57:01'),
(7, 17.6868159, 83.2184815, '2025-01-21 03:57:28'),
(8, 17.6868159, 83.2184815, '2025-01-21 03:57:52'),
(9, 17.6868159, 83.2184815, '2025-01-21 03:58:04');

-- --------------------------------------------------------

--
-- Table structure for table `bluetooth_count`
--

CREATE TABLE `bluetooth_count` (
  `id` int(11) NOT NULL,
  `count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bluetooth_count`
--

INSERT INTO `bluetooth_count` (`id`, `count`) VALUES
(1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `codehuntregistrations`
--

CREATE TABLE `codehuntregistrations` (
  `id` int(11) NOT NULL,
  `team_name` varchar(255) NOT NULL,
  `member1_mail` varchar(255) NOT NULL,
  `member1_name` varchar(255) NOT NULL,
  `member1_college` varchar(255) NOT NULL,
  `member1_branch` varchar(50) NOT NULL,
  `member1_year` int(1) NOT NULL,
  `member2_name` varchar(255) NOT NULL,
  `member2_college` varchar(255) NOT NULL,
  `member2_branch` varchar(50) NOT NULL,
  `member2_year` int(1) NOT NULL,
  `member1_mobile` varchar(10) NOT NULL,
  `registration_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `codehuntregistrations`
--

INSERT INTO `codehuntregistrations` (`id`, `team_name`, `member1_mail`, `member1_name`, `member1_college`, `member1_branch`, `member1_year`, `member2_name`, `member2_college`, `member2_branch`, `member2_year`, `member1_mobile`, `registration_time`) VALUES
(6, 'Moon team', 'kavyasingu6@gmail.com', 'Singu Kavya ', 'Chalapathi institute of technology ', 'CSE-DS', 4, 'Challa Sri lekha ', 'Chalapathi institute of technology ', 'CSE-DS', 4, '9391075345', '2024-10-21 06:34:59'),
(7, 'Zygen', 'jayanthkotte888@gmail.com', 'Jayanth Kotte', 'Chalapathi Institute Of Technology ', 'CSE', 4, 'Chakradhar Reddy Bijjamula ', 'Chalapathi Institute Of Technology ', 'CSE', 4, '8074691024', '2024-10-21 08:08:41'),
(8, 'Search bar', '21ht1a4652@gmail.com', 'SHAIK RAHAMTULLA', 'Chalapathi Institute of Technology ', 'CSE-CS', 4, 'JAGADEESH KANNEDARI', 'Chalapathi Institute of Technology ', 'CSE-CS', 4, '9346906159', '2024-10-21 08:43:50'),
(9, 'HONEST CREATERS ', '22ht1a4624@gmail.com', 'GOLLAPALLI RAVEENDRA ', 'Chalapathi institute of technology ', 'CSE-CS', 3, 'KUKKALA NAVEEN ', 'Chalapathi institute of technology ', 'CSE', 3, '7893279556', '2024-10-21 10:25:13'),
(10, 'Surya Kiran, sarath, Anand ', 'suryakirankurra143@gmail.com', 'Surya Kiran ', 'Vvit', 'CSE', 2, 'Sarath yadav ', 'Vvit ', 'CSE', 2, '8341876333', '2024-10-21 11:14:12'),
(11, 'R K GANG', 'raviteja.a7786@gmail.com', 'A Ravi Teja ', 'Gvr&s College of engineering and technology ', 'AIML', 2, 'B.V.Krishna', 'Gvr&s College of engineering and technology ', 'ECE', 2, '9030177886', '2024-10-21 12:05:31'),
(12, 'Straw hats ðŸ‘’ðŸ´â€â˜ ï¸', 'malleswararao1511@gmail.com', 'A. Somasekhar', 'Chalapathi Institute of technology', 'CSE-AI', 2, 'B Naga Malleswararao', 'Chalapathi Institute of technology', 'CSE-AI', 2, '7569587392', '2024-10-21 12:28:04'),
(13, 'No', 'dharanigorrepati309@gmail.com', 'GORREPATI DHARANI ', 'NRI INSTITUTE OF TECHNOLOGY ', 'AIML', 4, 'Indu,Archana', 'NRI INSTITUTE OF TECHNOLOGY ', 'AIML', 4, '8179048916', '2024-10-21 13:46:57'),
(14, 'Syntax sacrasm', 'kotavenkatanarayana123@gmail.com', 'Kota Venkata Narayana ', 'NRI Institute Of Technology ', 'CSE-DS', 2, 'Kolakaluri Anand Ofir ', 'NRI Institute Of Technology ', 'CSE-DS', 2, '9392408547', '2024-10-21 13:58:25'),
(15, 'DS team', 'sivakumarreddy.2204@gmail.com', 'BADU SIVA KUMAR REDDY', 'NRI INSTITUTE OF TECHNOLOGY ', 'CSE-DS', 3, 'P DEVI VARA PRASAD ', 'NRI INSTITUTE OF TECHNOLOGY ', 'CSE-DS', 3, '8919975067', '2024-10-21 14:44:33'),
(16, 'Hacker', 'sampath2005h@gmail.com', 'NADAMALURU SAMPATH KUMAR', 'VASIREDDY VENKATADRI INSTITUTE OF TECHNOLOGY ', 'CSE-AI', 2, 'CHILAKALA VISHNU VARDAN', 'VASIREDDY VENKATADRI INSTITUTE OF TECHNOLOGY ', 'CSE-AI', 2, '7989624678', '2024-10-21 15:08:55'),
(17, 'Sparkle ', 'annapurna5205@gmail.com', 'Chilakapati.Annapurna', 'Gvr&s college of engineering and technology ', 'AIML', 3, 'Saijyothi.Vadranam', 'Gvr&s college of engineering and technology ', 'AIML', 3, '9573507789', '2024-10-21 16:23:42'),
(18, 'Chandbasha', 'chandbashas944@gmail.com', 'SHAIK CHAND BASHA ', 'Chalapathi institute of technology ', 'CSE-DS', 2, 'V venkata Sai Tejesh ', 'Chalapathi institute of technology ', 'CSE-DS', 2, '9392670826', '2024-10-21 16:40:01'),
(19, 'Achievers ', 'sahithyakadiyamsetti@gmail.com', 'SHAIK SOHEL ', 'Kallam HaranadhaReddy Institute of Technology ', 'IT', 4, 'KADIYAMSETTI SAHITHYA ', 'Kallam HaranadhaReddy Institute of Technology ', 'IT', 4, '9515707749', '2024-10-21 19:35:23'),
(20, 'Pragna', 'neelisettypragna37@gmail.com', 'Lakshmi Sai Pragna', 'Vvit college ', 'AIML', 1, 'Lakshmi ', 'Vvit college ', 'AIML', 1, '7013501499', '2024-10-22 03:56:55'),
(21, 'White eagles', 'peddik029@gmail.com', 'Peddi.Naga Sai Krishna Charan', 'Chalapathi Institute of Technology ', 'CSE-CS', 4, 'Daggumati.Dinesh', 'Chalapathi Institute of Technology ', 'CSE-CS', 4, '7013726251', '2024-10-22 04:06:16'),
(22, 'Dynamic Duo', 'jmohankrishna379@gmail.com', 'Krishna ', 'GVR&S college of engineering and technology ', 'CSE', 2, 'Prem Kumar ', 'GVR&S college of engineering and technology ', 'CSE', 2, '8688110169', '2024-10-22 06:53:31'),
(23, 'Imran\'s Team', '23ht1a44b0@gmail.com', 'Shaik Varfan', 'Chalapathi Institute of Technology, Mothadaka ', 'CSE-DS', 2, 'Pathan Imran Khan', 'Chalapathi Institute of Technology, Mothadaka ', 'CSE-DS', 2, '9908571735', '2024-10-22 07:37:49'),
(24, 'Code Crackers ', '22ht1a6159@gmail.com', 'VARIKUTI CHINNA KOTESWARA RAO ', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'AIML', 3, 'KAMBHAM JAGADISH ', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'AIML', 3, '9182687179', '2024-10-22 08:44:39'),
(25, 'CAI-B', '23ht1a43b0@gmail.com', 'Shaik Nailo Rajak', 'Chalapthi institute of technology ', 'CSE-AI', 2, 'N venkateswrarao ', 'Chalapathi Institute of Technology ', 'CSE-AI', 2, '7989361070', '2024-10-22 09:44:02'),
(26, 'GR gems ', 't.gurumani456@gmail.com', 'Gurumani ', 'Hindu college of engineering and technology ', 'CSE', 2, 'Rohit ', 'Hindu college of engineering and technology ', 'CSE', 2, '7780154210', '2024-10-22 12:31:04'),
(27, 'SANATANI BOYS', 'subbukatreddy81@gmail.com', 'K.SUBBA REDDY', 'VIGNAN UNIVERSITY ', 'CSE', 1, 'B.VIVEK', 'SRM UNIVERSITY', 'AIML', 1, '8367668555', '2024-10-22 14:03:44'),
(28, 'Code', 'chanikyachowdary8866@gmail.com', 'Chanikya Chowdary Samineni ', 'Vfstr', 'CSE', 1, 'Jaswanth', 'Vfstr', 'CSE', 2, '9392453073', '2024-10-22 14:29:06'),
(29, 'Bro Code', 'divyatejasunke@gmail.com', 'Divya Teja Sunke ', 'NRI institute of technology ', 'CSE-DS', 2, 'Tella Eswar Chandra Prasad', 'NRI institute of technology ', 'CSE-DS', 2, '8247421933', '2024-10-22 14:50:24'),
(30, 'Yamuna sri', 'srilakshmikonakanchi324@gmail.com', ' Konakanchi Srilakshmi ', 'Vignan\'s Lara institute of technology and science ', 'CSE-DS', 3, 'Aladasu Yamuna', 'Vignan\'s Lara institute of technology and science ', 'CSE', 3, '9392873327', '2024-10-22 14:53:37'),
(31, 'Sk katishma', 'skkarishma739@gmail.com', 'VU_241FA04A09@gmail.com', 'Vignan university', 'CSE', 1, 'Sk. Karishma', 'Vastr', 'CSE', 1, '8885888739', '2024-10-22 15:07:34'),
(32, 'Ai Walker', 'jagadishjai290@gmail.com', 'Jagadeesh', 'Hindu college ', 'AIML', 3, 'Amarnadh ', 'Hindu college ', 'AIML', 3, '7671910493', '2024-10-22 15:36:09'),
(33, 'Jataprolu kowshik ', 'jataprolukowshik@gmail.com', 'Jataprolu kowshik ', 'MVRS ENGINEERING COLLEGE ', 'CSE', 4, 'Jataprolu kowshik', 'MVRS ENGINEERING COLLEGE ', 'CSE', 4, '9676548361', '2024-10-22 16:36:31'),
(34, 'Decoder', 'vu.241fa04e66@gmail.com', 'Vinit Rajak ', 'Vignan university ', 'CSE', 1, 'Priyanshu kumar Gupta ', 'Vignan university ', 'CSE-DS', 1, '8235395227', '2024-10-22 16:45:34'),
(35, 'Code breakers', 'vu.241fa04106@gmail.com', 'Rajasri kondaveeti', 'Vignan university ', 'CSE', 1, 'Sharabu Asritha', 'Vignan university ', 'CSE', 1, '7330966733', '2024-10-23 02:50:49'),
(36, 'Akhil', 'akhilbatchu08@gmail.com', 'B.UMA NAGA SRI AKHIL', 'Chalapathi institute of technology ', 'CSE-DS', 2, 'G.VENU', 'Chalapathi institute of technology ', 'CSE-DS', 2, '6303880362', '2024-10-23 04:30:39'),
(37, 'VR', 'ravichandrapathi926@gmail.com', 'Ravichandra pathi', 'Universal college of engineering and technology, Dokiparru ', 'CSE', 3, 'Vamsi Madiga', 'Universal college of engineering and technology, Dokiparru ', 'CSE', 3, '9550808836', '2024-10-23 06:20:04'),
(38, 'Sk', 'kuchipudismitha@gmail.com', 'Smitha ', 'GVR&S ', 'CSE-AI', 2, 'Kowsalya ', 'GVR&S', 'CSE', 2, '8074938131', '2024-10-23 07:08:48'),
(39, 'KS', 'kuchipudismitha@gmail.com', 'Smitha ', 'GVR&S ', 'CSE-AI', 2, 'Kowsalya ', 'GVR&S', 'CSE', 2, '8074938131', '2024-10-23 07:09:08'),
(40, 'Bugatti', 'thouhidshaik614@gmail.com', 'Shaik Thouhid', 'NRI Institute of technology', 'CSE-DS', 2, 'Swarna raghupremsai', 'NRI Institute of technology', 'CSE-DS', 2, '9492439097', '2024-10-23 07:09:44'),
(41, 'FS', 'farhanabegumpatan@gmail.com', 'Farhana begum', 'GVR&S', 'AIML', 2, 'Sivakumari ', 'GVR&S', 'CSE', 2, '8919850205', '2024-10-23 07:12:03'),
(42, 'Code Hunters', 'gudipudivijaybabu123@gmail.com', 'Vijay babu Gudipudi ', 'Chalapathi Institute Of Technology ', 'AIML', 2, 'Bandaru kiranmai', 'Chalapathi Institute Of Technology ', 'AIML', 2, '9347742178', '2024-10-23 07:18:09'),
(44, 'Manoj Kumar ', 'ramadevimunirathnam@gmail.com', 'Nagappagari Mounika', 'Chalapathi institute of technology ', 'CSE-DS', 2, 'Ch Manoj Kumar ', 'Chalapathi institute of technology ', 'CSE-DS', 2, '8328314452', '2024-10-23 08:00:52'),
(45, 'MK', 'kavyasrichimmirikbt@gmail.com', ' CHIMMIRI KAVYA SRI', 'Vignan\'s lara Institute of technology and science', 'CSE-DS', 3, 'VASANTHA MANISHA', 'KKR & KSR Institute of technology and science', 'CSE', 3, '6302682524', '2024-10-23 08:26:49'),
(46, 'Tech inventors', 'harikamullangi2003@gmail.com', 'Harika Mullangi ', 'Chalapathi institute of technology ', 'CSE-DS', 4, 'Peeka Amulya', 'Chalapathi institute of technology ', 'CSE-DS', 4, '9322119203', '2024-10-23 09:03:20'),
(47, 'SN', 'balisettisasisasi@gmail.com', ' Balisetti   Sasi Tirumala Nagamani ', 'GVR&S ', 'AIML', 2, 'JONNAKUTI  NEHA ', 'GVR&S ', 'AIML', 2, '9581365470', '2024-10-23 09:07:07'),
(48, 'Prasannanavya ', '21ht1a4405@gmail.com', 'BAINABOINA LAKSHMI PRASANNA', 'Chalapathi Institute of technology', 'CSE-DS', 4, 'G. NAVYA', 'Chalapathi Institute of technology', 'CSE-DS', 4, '7674974248', '2024-10-23 09:08:51'),
(49, 'Colorful ', 'pasupuletisailakshmi01@gmail.com', 'P. Sri Lakshmi ', 'Gvr&s', 'AIML', 2, 'Thasleema ', 'Gvr&s', 'AIML', 2, '8466935486', '2024-10-23 09:39:06'),
(50, 'Tony stark', 'charankolli573@gmail.com', 'Charan', 'Chalapathi institute of technology ', 'CSE-AI', 4, 'Chetan', 'Chalapathi institute of technology ', 'CSE-AI', 4, '9490651712', '2024-10-23 09:50:55'),
(51, 'Backlog Bashers Team', 'maheshbabunaidu2004@gmail.com', 'Mahesh Babu.P', 'Chalapathi Institute of Technology', 'CSE', 2, 'K.Venkat Sai', 'Chalapathi Inst of Technology ', 'CSE', 2, '9154568386', '2024-10-23 09:55:44'),
(52, 'Introverts', 'sushmithachakka07@gmail.com', 'Sushmitha ', 'GVR&S college of engineering and technology ', 'ECE', 2, 'Krishna chaitanya ', 'GVR&S college of engineering and technology ', 'ECE', 2, '9014121695', '2024-10-23 10:33:45'),
(53, 'AI SQUAD', 'natanigunasri@gmail.com', 'Natani Guna Sri Durgapriya ', 'Chalapathi institute of technology mothadhaka ', 'CSE-AI', 2, 'Shaik Mehar niger', 'Chalapathi institute of technology mothadhaka ', 'CSE-AI', 2, '9951123733', '2024-10-23 10:50:40'),
(54, 'Tech Thinker ', 'shaikabdulnabi2004@gmail.com', 'SHAIK ABDUL NABI', 'Chalapathi institute of technology ', 'ECE', 3, 'Narra Ramesh Reddy ', 'Chalapathi institute of technology ', 'ECE', 3, '9346022080', '2024-10-23 10:53:51'),
(55, 'Code hunter ', 'praveenvasarla407@gmail.com', 'Vasarla praveen ', 'Chalapathi institute of technology ', 'CSE', 2, 'Venkatrao', 'Chalapathi institute of technology ', 'CSE', 2, '7780730596', '2024-10-23 11:02:55'),
(56, 'Next era ', 'namburikowshitha@gmail.com', 'Kowshitha Namburi', 'Chalapathi institute of technology ', 'CSE', 3, 'M .Sri Lakshmi Prasanna ', 'Chalapathi institute of technology ', 'CSE', 3, '9440628798', '2024-10-23 11:22:03'),
(57, 'Unbeatable coders', '22ht1a43b8@gmail.com', 'Vangapati manikanta', 'Chalapathi institute of technology ', 'CSE-AI', 3, 'Panga Meghana', 'Chalapathi institute of technology ', 'CSE-AI', 3, '6303062574', '2024-10-23 11:32:49'),
(58, 'Unbeatable performers', '22ht1a4388@gmail.com', 'Pathan sabiya', 'Chalapathi institute of technology ', 'CSE-AI', 3, 'Perla maneesha', 'Chalapathi institute of technology ', 'CSE-AI', 3, '9989133130', '2024-10-23 11:36:13'),
(59, 'Engineers', 'mylamallikharjunreddy6@gmail.com', 'MYLA LAKSHMI MALLIKHARJUN REDDY ', 'Chalapathi institute of technology ', 'CSE', 2, 'Koppula Chandra Sekhar ', 'Chalapathi institute of technology ', 'CSE', 2, '9515606359', '2024-10-23 11:55:39'),
(60, 'MKM  Team', 'raghunadharao157@gmail.com', 'K. mani', 'Chalapathi Institute of Technology', 'CSE', 3, 'K. Meghana', 'Chalapathi Institute of Technology', 'CSE', 3, '9347568580', '2024-10-23 13:11:53'),
(61, 'MKM Team', 'raghunadharao157@gmail.com', 'K. Mani', 'Chalapathi Institute of Technology', 'CSE', 3, 'K. Meghana', 'Chalapathi Institute of Technology', 'CSE', 3, '9347568580', '2024-10-23 13:16:14'),
(62, 'Dk', 'sravanthidevarapu9@gmail.com', 'DEVARAPU SRAVANTHI', 'St. Marry\'s women\'s engineering college', 'CSE', 3, 'CHIMMIRI KAVYA SRI', 'vignan\'s lara Institute of technology and science', 'CSE-DS', 3, '7989074330', '2024-10-23 13:22:16'),
(63, 'Bug rebels ', '23ht1a4315@gmail.com', 'Manohar ', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'Yashwanth ', 'Chalapathi institute of technology ', 'CSE-AI', 2, '8688155269', '2024-10-23 13:27:44'),
(64, 'Code Admires ', '22ht1a4412@gmail.com', 'B Lakshmi Sindhu ', 'Chalapathi Institute of Technology ', 'CSE-DS', 3, 'D Kaveri', 'Chalapathi Institute of Technology ', 'CSE-DS', 3, '8247626184', '2024-10-23 13:29:36'),
(65, 'IMMORTALS', '22ht1a4365@gmail.com', 'Manam Bhavyanth', 'Chalapathi Institute Of Technology', 'CSE-AI', 3, 'Chalavadi Vamsi', 'Chalapathi Institute Of Technology', 'CSE-AI', 3, '8639714155', '2024-10-23 13:41:35'),
(66, 'Modern Moggers', '22ht1a4304@gmail.com', 'ANKEM YUVA NAGA DURGA ABHISHEK', 'Chalapathi Institute Of Technology', 'CSE-AI', 3, 'Kalari Hemanth', 'Chalapathi Institute Of Technology', 'CSE-AI', 3, '6303438791', '2024-10-23 13:44:34'),
(67, 'Debugging Ninjas', '22ht1a4320@gmail.com', 'Chembeti Manohar', 'Chalapathi Institute Of Technology', 'CSE-AI', 3, 'Appisetty Dinesh', 'Chalapathi Institute Of Technology', 'CSE-AI', 3, '6281547857', '2024-10-23 13:48:38'),
(68, 'Techie wizards', '22ht1a05b8@gmail.com', 'Peruboina Venkatasai', 'Chalapathi institute of technology ', 'CSE', 3, 'Perumalla Venkata Naga Dhanush', 'Chalapathi institute of technology ', 'CSE', 3, '7075254372', '2024-10-23 13:51:53'),
(69, 'MJ', 'jayasrimulakaledu@gmail.com', 'Mulakaledu Jayasri ', 'Krishnaveni engineering college for women ', 'CSE', 4, 'Shaik Mubhasheera Bhanu ', 'Krishnaveni engineering College for women ', 'CSE', 4, '7382743563', '2024-10-23 14:52:38'),
(70, 'LOVARAJU-SUBBU', 'subramanyamachyutha2002@gmail.com', 'Subramanyam Achyutha', 'Vignan\'s LARA Institute of Technology & ScienceVignan\'s LARA Institute of Technology & Science ', 'CSE-DS', 3, 'Lovaraju', 'Vignan\'s LARA Institute of Technology & Science', 'CSE-DS', 3, '9704831099', '2024-10-23 15:40:05'),
(71, 'AI Code Crackers', '22ht1a4312@gmail.com', 'Vaishnavi Bareddy', 'Chalapathi Institute of Technology ', 'CSE-AI', 3, 'PujithaSri Chinthapalli ', 'Chalapathi Institute of Technology ', 'CSE-AI', 3, '7893141028', '2024-10-23 15:41:10'),
(72, 'N.venkateswararao', '23ht1a4376@gmail.com', 'Sk.nailo rajak', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'N.venkateswararao', 'Chalapathi institute of technology ', 'CSE-AI', 2, '7989361070', '2024-10-23 16:18:55'),
(73, 'Mech x4', 'saikumarchapparla@gmail.com', 'Chapparla sai kumar', 'Chalapathi institute of technology ', 'CSE', 3, 'Addanki prasanth ', 'Chalapathi institute of technology ', 'CSE', 3, '9347085890', '2024-10-23 18:01:16'),
(74, 'Code splitz', 'srinivasbasivila13@gmail.com', 'srinivas basivila', 'Khit', 'OT', 2, 'Teja sri', 'Khit', 'OT', 2, '9347491842', '2024-10-24 02:33:48'),
(75, 'AI Team ', '23ht1a43c2@gmail.com', 'V.Sagarika', 'Chalapathi institute of technology motadaka ', 'CSE-AI', 2, 'Sneha latha', 'Chalapathi institute of technology motadaka ', 'CSE-AI', 2, '8019745992', '2024-10-24 03:36:28'),
(76, 'Team  Dynamic ii', '22ht1a4307@gmail.com', 'Arimalla Anil ', 'Chalapathi institute of technology ', 'CSE-AI', 3, 'Jaggarapu Sravan', 'Chalapathi institute of technology ', 'CSE-AI', 3, '7671997148', '2024-10-24 03:37:38'),
(77, 'AI2', '23ht1a4371@gmail.com', 'Mopidevi. Harshitha', 'Chalapathi Institute of technology', 'CSE-AI', 2, 'Nallabothula siva brahmaiah', 'Chalapathi Institute of technology', 'CSE-AI', 2, '9398457504', '2024-10-24 03:43:46'),
(78, 'Developers', '23ht1a0585@gmail.com', 'Balasri kunisetti', 'Chalapathi institute of technology ', 'CSE', 2, 'Mani vardhan reddy lekkala', 'Chalapathi institute of technology ', 'CSE', 2, '8688976348', '2024-10-24 03:52:46'),
(79, 'Coding developers', 'premarajua7@gmail.com', 'Premaraju ', 'Chalapathi institute of technology ', 'CSE', 2, 'Kunisetti balasri', 'Chalapathi institute of technology ', 'CSE', 2, '8341052032', '2024-10-24 04:03:13'),
(80, 'AI thaluka ', '23ht1a4329@gmail.com', 'Naveen ', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'Vinay', '93928', 'CSE-AI', 2, '9392822739', '2024-10-24 04:03:16'),
(81, 'Coding thaluka ', '23ht1a4329@gmail.com', 'Naveen ', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'Vinay', '93928', 'CSE-AI', 2, '9392822739', '2024-10-24 04:04:22'),
(82, 'Hunter hunt ', '23ht1a4329@gmail.com', 'Naveen ', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'Vinay', '93928', 'CSE-AI', 2, '9392822739', '2024-10-24 04:04:57'),
(83, 'Code engineers', 'ananthalakshmivemala@gmail.com', 'Vemala.Anantha Lakshmi', 'Chalapathi institute of technology ', 'CSE-DS', 3, 'Sri Pallavi.somala', 'Chalapathi institute of technology ', 'CSE-DS', 3, '9381102960', '2024-10-24 04:05:38'),
(84, 'Bigboss', '22ht1a0552@gmail.com', 'JANJHYAM SAI CHAITHANYA', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, 'CHALLA VASISHTA', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, '7306270812', '2024-10-24 04:06:51'),
(85, 'Hunter', 'avinashavinash24576@gmail.com', 'Chirra Lok sai Avinash Reddy', 'Chalapathi Institute of technology', 'CSE', 3, 'Kalluri Venkata Guru Prasad', 'Chalapathi Institute of technology', 'CSE', 3, '9642784897', '2024-10-24 04:07:47'),
(86, 'SINISTER', 'dineshguntupalli9720@gmail.com', 'Dinesh Chowdary', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, 'Sasikanth', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, '7981643262', '2024-10-24 04:10:55'),
(87, 'AI TECHNO SPARKS', '23ht1a4345m@gmai.com', 'Kapu mani shankar Reddy ', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'Chigine pallavi ', 'Chalapathi institute of technology ', 'CSE-AI', 2, '6301361169', '2024-10-24 04:11:01'),
(88, 'ARTIFICIAL INTELLIGENCE ', 'nandeeswar4341@gmail.com', 'Nandeeswar kambhampati ', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'GODDANTI GOWTHAM', 'Chalapathi institute of technology ', 'CSE-AI', 2, '7013158264', '2024-10-24 04:13:45'),
(89, 'Master Minds', 'balajigunji2004@gmail.com', 'Gunji Balaji', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, 'Gudala Ajay Kumar Reddy ', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, '6300107345', '2024-10-24 04:14:16'),
(90, 'Xcution', 'dnlppavan@gmail.com', 'Dokku Pavan Krishna', 'Chalapathi Institute of technology', 'CSE', 3, 'Challa Venkata Krishna', 'Chalapathi Institute of technology', 'CSE', 3, '9121263887', '2024-10-24 04:14:16'),
(91, 'Reddy', '23ht1a4356@gmail.com', 'K.gopi', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'Prabhakar ', 'Chalapathi institute of technology ', 'CSE-AI', 2, '8074042919', '2024-10-24 04:15:53'),
(92, 'CHALAPATHI WARRIORS', '22ht1ao548@gmail.com', 'Haridasula Prasannanjaneyulu', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, 'Gochipathala Yona', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, '7013104010', '2024-10-24 04:18:48'),
(93, 'Team Ai(2.0)', 'prathapreddy5438@gmail.com', 'K.prathap Reddy', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'J.venkatesh', 'Chalapathi institute of technology ', 'CSE-AI', 2, '9381961226', '2024-10-24 04:20:33'),
(94, 'Code boosters', 'nithinrajuchilaka@gmail.com', 'Chilaka.Nithinraju', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, 'Janamala.Gurumurthy', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE', 3, '6303076432', '2024-10-24 04:21:42'),
(95, 'City boys ', 'prathapreddy5438@gmail.com', 'K.prathap Reddy', 'Chalapathi institute of technology ', 'CSE-AI', 2, 'J.venkatesh', 'Chalapathi institute of technology ', 'CSE-AI', 2, '9381961226', '2024-10-24 04:23:15'),
(96, 'Benchmark ', '22ht1a4302@gmail.com', 'Karthikeya', 'Chalapathi institute of technology ', 'CSE-AI', 3, 'Devi Sri Prasad ', 'Chalapathi institute of technology ', 'CSE-AI', 3, '9963284950', '2024-10-24 04:24:29'),
(97, 'Shakti team', 'gayatriendyala@gmail.com', 'PRASANNA KOMALA SIVA GAYATRI. Pendyala', 'Chalapathi institute of technology ', 'CSE-DS', 3, 'Leela bhargavi. Pedavalli', 'Chalapathi institute of technology ', 'CSE-DS', 3, '9533077555', '2024-10-24 04:28:26'),
(98, 'POWER PAIR', 'ramyakala13042006@gmail.com', 'Ch Ramya kala', 'City', 'CSE-DS', 2, 'Ch anjali', 'Ciry', 'CSE-DS', 2, '7989376187', '2024-10-24 04:48:29'),
(99, 'Ds', '23ht1a4439@gmail.com', 'G venu', 'Chalapathi institute of technology ', 'CSE-DS', 2, 'G vishnu', 'Chalapathi institute of technology ', 'CSE-DS', 2, '9391932229', '2024-10-24 04:48:33'),
(100, 'CSE', 'asifshaik1812@gmail.com', 'Sk Asif', 'Chalapathi institute of technology (city))', 'CSE', 2, 'Y Dinesh ', 'Chalapathi institute of technology (city)', 'CSE', 2, '8179445299', '2024-10-24 05:02:29'),
(101, 'Spark', 'swaroopyelchuri25@gmail.com', 'Swaroop', 'Chalapathi institute of technology ', 'CSE-DS', 2, 'K.Yagnesh', 'Chalapathi institute of technology ', 'CSE-DS', 2, '9346081055', '2024-10-24 05:04:11'),
(102, 'Ak', 'faiyazahamedsyedgnt@gmail.com', 'Sd. Faiyazahamed', 'City', 'CSE', 2, 'T. Anand ', 'City', 'CSE', 2, '9121381992', '2024-10-24 05:05:33'),
(103, 'DP', 'dileepdavuluri1@gmail.com', 'Pavan', 'Chalapathi institute of technology ', 'CSE-AI', 4, 'Dileep', 'Chalapathi institute of technology ', 'CSE-AI', 4, '7995537427', '2024-10-24 05:05:52'),
(104, 'CSE-B', 'saibhargav012@gmail.com', 'Sai bhargav', 'Chalapathi institute of engineering and technology ', 'CSE', 2, 'MUSTHAKHEEM', 'Chalapathi institute of engineering and technology ', 'CSE', 2, '9133251944', '2024-10-24 05:33:20'),
(105, 'Shaik Bellamkonda saidha', 'saidhaiba45@gmail.com', 'Shaik Bellamkonda saidha', 'Khit', 'CE', 2, 'shaik Bellamkonda saidha, yenibera Prabhu charan', 'Khit', 'CE', 2, '6301785751', '2024-10-24 05:33:46'),
(106, 'Hack street boys', 'vamsikrishnaneelam111@gmail.com', 'Vamsi krishna', 'Chalapathi institute of engineering and technology ', 'CSE', 3, 'P venkata narayana ', 'Chalapathi institute of engineering and technology ', 'CSE', 3, '9059420400', '2024-10-24 05:38:03'),
(107, 'NARUTO UZUMAKI ', 'joshuaswaraj@gmail.com', 'PULIPATI JOSHUA SWARAJ', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE-CS', 3, 'MALLE GANESH', 'CHALAPATHI INSTITUTE OF TECHNOLOGY ', 'CSE-CS', 3, '7780654486', '2024-10-24 05:41:44'),
(108, 'CSE C', 'charansaip7@gmail.com', 'Charan ', 'Chalapathi institute of engineering  and technology ', 'CSE', 2, 'Omkar abhiram sai', 'Chalapathi institute of technology ', 'CSE-AI', 3, '7702793835', '2024-10-24 05:45:35'),
(109, 'Childish BATCH  ', 'dharshipuli@gmail.com', 'Lakshmidhar ', 'Chalapathi institute of engineering and technology ', 'CSE-CS', 2, 'Jakkireddy rohith raghavendra reddy', 'CIET', 'CSE-CS', 2, '8143637554', '2024-10-24 05:49:09'),
(110, 'Hack street', 'popuricharan2004@gmail.com', 'Charan Rajesh', 'Chalapathi institute of engineering and technology ', 'CSE', 3, 'N tirupathi ', 'Chalapathi institute of engineering and technology ', 'CSE', 3, '9059420400', '2024-10-24 05:49:17'),
(111, 'CIET', 'vinodbandaru51@gmail.com', 'B.Vinod', 'Chalapathi institute of engineering and technology ', 'CSE', 3, 'K.vamsi', 'Chalapathi institute of engineering and technology ', 'CSE', 3, '7093808751', '2024-10-24 05:49:49'),
(112, 'Tech Quires', 'tejaswinigutta009@gmail.com', 'G Tejaswini ', 'Chalapathi Institute of Engineering and Technology ', 'CSE-CS', 2, 'M Tejaswini ', 'Chalapathi Institute of Engineering and Technology ', 'CSE-CS', 2, '8309094057', '2024-10-24 05:53:07'),
(113, 'Chalapathi guys', 'sodagudi12@gmail.com', 'Sai pradeep ', 'Chalapathi Institute of engineering and technology', 'CSE-CS', 2, 'Shaik galishid', 'Chalapathi Institute of engineering and technology', 'CSE-CS', 2, '9989996966', '2024-10-24 05:53:33'),
(114, 'Code runners', 'joshnatirumalasetty@gmail.com', 'Joshna Tirumalasetty ', 'Kallam Haranadhareddy Institute of technology ', 'OT', 2, 'Kasiragavendra suda', 'Kallam Haranadhareddy Institute of technology ', 'OT', 2, '9346736744', '2024-10-24 05:56:53'),
(115, 'Harinadh squad ', 'saisriramassr@gmail.com', 'Amaravathi saisriram ', 'Kallam Haranadha Reddy institute of technology ', 'OT', 2, 'K Venkateswarlu', 'Chalapathi institute of technology ', 'CSE-DS', 4, '9110740250', '2024-10-24 05:59:09'),
(116, 'N.vamsi', 'nadimintivamsi7780@gmail.com', 'N.vamsi', 'Khit', 'OT', 2, 'Divya', 'Khit', 'OT', 2, '7780231121', '2024-10-24 05:59:19'),
(117, 'Code generator ', 'krishnanagavenkat11@gmail.com', 'Krishna ', 'Khit', 'OT', 2, 'Raja Kumar ', 'Khit ', 'OT', 2, '7337579718', '2024-10-24 06:01:55'),
(118, 'Techies', 'venkatasai2409@gmail.com', 'Venkata Sai ', 'Khit', 'OT', 2, 'Gopi krishna', 'Khit ', 'OT', 2, '6301770869', '2024-10-24 06:03:15'),
(119, 'Code chefs', 'najeerkhanp335@gmail.com', 'Patan Najeer Khan', 'Chalapathi institute of technology ', 'AIML', 2, 'Sk. MASEEDU asif', 'Chalapathi institute of technology ', 'AIML', 2, '7997488619', '2024-10-24 06:11:52'),
(120, 'Team Arnold', 'ysaichaitanya33@gmail.com', 'Sai Chaitanya Yerramsetty ', 'Chalapathi institute of technology ', 'CSE-AI', 4, 'Yuva', 'Chalapathi institute of technology ', 'CSE-DS', 4, '9381015031', '2024-10-24 06:13:05'),
(121, 'Code creators', '23ht1a6114@gmail.com', 'Dasari amar nadh ', 'Chalapathi institute of technology ', 'AIML', 2, 'A. Praveen', 'Chalapathi institute of technology ', 'AIML', 2, '9603376794', '2024-10-24 06:15:12'),
(122, 'Team Arnold2', 'ysaichaitanya33@gmail.com', 'Sai Chaitanya Yerramsetty ', 'Chalapathi institute of technology ', 'CSE-AI', 4, 'Subbarao payyavula', 'Chalapathi institute of technology ', 'CSE-AI', 3, '9381015031', '2024-10-24 06:24:38'),
(123, 'Dreams hack', 'fathersdaughter2004@gmail.com', 'Divi Anusha', 'Chalapathi Institute of Technology', 'CSE-AI', 4, 'GALI Likitha ', 'Chalapathi Institute of Technology ', 'CSE-AI', 4, '9985577383', '2024-10-24 06:24:52'),
(124, 'Cuber', '23ht1a4612@gmail.com', 'Praveen Kumar ', 'City ', 'CSE-CS', 2, 'Khaja', 'City', 'CSE-CS', 2, '9542644826', '2024-10-24 06:28:32'),
(125, 'Praveen cyber', '23ht1a4612@gmail.com', 'Praveen', 'City ', 'CSE-CS', 2, 'Khaja', 'City', 'CSE-CS', 2, '9542644826', '2024-10-24 06:29:57'),
(126, 'Shoryanga parvam', '22ht1a44a1@gmail.com', 'Shaik kifay ', 'Chalapathi institute of technology ', 'CSE-DS', 3, 'Shaik kaleem ', 'Chalapathi institute of technology ', 'CSE-DS', 3, '9110588185', '2024-10-24 08:36:37');

-- --------------------------------------------------------

--
-- Table structure for table `detection_count`
--

CREATE TABLE `detection_count` (
  `id` int(11) NOT NULL,
  `count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detection_count`
--

INSERT INTO `detection_count` (`id`, `count`) VALUES
(1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `diseases`
--

CREATE TABLE `diseases` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diseases`
--

INSERT INTO `diseases` (`id`, `name`) VALUES
(1, 'fever'),
(2, 'cold'),
(3, 'flu'),
(4, 'diabetes'),
(5, 'hypertension'),
(6, 'asthma'),
(7, 'Malaria'),
(8, 'Typhoid'),
(9, 'Dengue'),
(10, 'Diarrhoea'),
(11, 'Chickengunya'),
(12, 'cholera'),
(13, 'tuber closis'),
(14, 'cancer'),
(15, 'hepatitis');

-- --------------------------------------------------------

--
-- Table structure for table `elitelevel`
--

CREATE TABLE `elitelevel` (
  `id` int(11) NOT NULL,
  `team_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `member_1_number` varchar(50) NOT NULL,
  `team_member_2_name` varchar(100) DEFAULT NULL,
  `submission_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `elitelevel`
--

INSERT INTO `elitelevel` (`id`, `team_name`, `email`, `member_1_number`, `team_member_2_name`, `submission_date`) VALUES
(2, 'Hgg', '22ht1a4425@gmail.com', 'Ggg', 'Ghy', '2024-10-24 04:10:03'),
(3, 'tech thinckers', 'shaikabdulnabi2004@gmail.com', '9346022080', 'Shaik Abdul Nabi', '2024-10-24 07:41:55'),
(4, 'SN', 'balisettisasisasi@gmail.com', '9581365470', 'J.Neha', '2024-10-24 07:44:08'),
(5, 'GR gems', 't.gurumani456@gmail.com', '7780154210', 'Rohith ', '2024-10-24 07:45:30'),
(6, 'Code Admires', '22ht1a4412@gmail.com', 'B Lakshmi Sindhu', 'D Kaveri', '2024-10-24 07:54:26');

-- --------------------------------------------------------

--
-- Table structure for table `government_users`
--

CREATE TABLE `government_users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `security_token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `government_users`
--

INSERT INTO `government_users` (`id`, `username`, `security_token`) VALUES
(1, 'gov111', '123'),
(2, 'gov112', '456'),
(3, 'gov122', '789');

-- --------------------------------------------------------

--
-- Table structure for table `medications`
--

CREATE TABLE `medications` (
  `id` int(11) NOT NULL,
  `disease_id` int(11) DEFAULT NULL,
  `medication` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medications`
--

INSERT INTO `medications` (`id`, `disease_id`, `medication`) VALUES
(1, 1, 'Paracetamol'),
(2, 1, 'Ibuprofen'),
(3, 1, 'Take Rest'),
(4, 1, 'Take Fluids'),
(5, 2, 'Antihistamines'),
(6, 2, 'Decongestants'),
(7, 2, 'Cough suppressants'),
(8, 2, 'Fluids'),
(9, 3, 'Antiviral drugs'),
(10, 3, 'Pain relievers'),
(11, 3, 'Rest'),
(12, 3, 'Fluids'),
(13, 4, 'Insulin'),
(14, 4, 'Metformin'),
(15, 4, 'Sulfonylureas'),
(16, 4, 'Meglitinides'),
(17, 5, 'Diuretics'),
(18, 5, 'ACE inhibitors'),
(19, 5, 'Calcium channel blockers'),
(20, 5, 'Beta blockers'),
(21, 6, 'Inhaled corticosteroids'),
(22, 6, 'Long-acting beta agonists'),
(23, 6, 'Leukotriene modifiers'),
(24, 6, 'Theophylline'),
(25, 7, 'Consult a Doctor'),
(26, 7, 'chloroquine'),
(27, 7, 'Malarone'),
(28, 7, 'Take Rest'),
(29, 8, 'Cephalosporins'),
(30, 8, 'Macrolides'),
(31, 8, 'Take Rest'),
(32, 8, 'Eat Raw Fruits'),
(33, 9, 'Consult a doctor'),
(34, 9, 'Acetaminophen'),
(35, 9, 'Aspirin'),
(36, 9, 'Eat Leafy Vegetables'),
(37, 10, 'Drink ORS'),
(38, 10, 'loperamide'),
(39, 10, 'Bismuth Subsalicylate'),
(40, 10, 'Eat Bananas'),
(41, 11, 'Acetaminophen'),
(42, 11, 'Paracetmol'),
(43, 11, 'Eat Vitamin-c rich fruits like Oranges,Kiwis'),
(44, 12, 'Consult a Doctor'),
(45, 12, 'chloramphenicol'),
(46, 12, 'Drink ORS'),
(47, 13, 'Immediately Consult a Doctor'),
(48, 13, 'Rifampin'),
(49, 13, 'isoniazid'),
(50, 13, 'Eat leafy vegetables'),
(51, 14, 'Immediately Consult a Doctor'),
(52, 14, 'Get full body checkup'),
(53, 15, 'Immediately consult a Doctor'),
(54, 15, 'Avoid contact with other'),
(55, 15, 'Use Medicines prescripted by Doctor');

-- --------------------------------------------------------

--
-- Table structure for table `needs`
--

CREATE TABLE `needs` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `state` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `essentials` text NOT NULL,
  `extra_needs` text DEFAULT NULL,
  `submissionTime` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `needs`
--

INSERT INTO `needs` (`id`, `name`, `mobile`, `state`, `district`, `address`, `essentials`, `extra_needs`, `submissionTime`) VALUES
(29, 'Avutu Lokesh Reddy', '8312546589', 'Andhra Pradesh', 'Guntur', 'RS colony, Reddypalem\r\n133-18-4003', 'Food & Water, Cloth, Medicines, First aid kit', 'Extra food packs', '2025-01-21 04:09:06');

-- --------------------------------------------------------

--
-- Table structure for table `public_users`
--

CREATE TABLE `public_users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `public_users`
--

INSERT INTO `public_users` (`id`, `username`, `password`) VALUES
(1, 'user1', '123'),
(2, 'user2', '123'),
(3, 'user3', '123'),
(20, '1234567890', '123'),
(21, '9912483007', 'Amrutha@4829'),
(22, '7997134292', 'ijak2002'),
(23, '7997134292', 'ijak2002'),
(24, '8328458690', '12345678'),
(25, '2200090010csit@gmail.com', 'abc@123'),
(26, '9347237345', 'manasa@2005');

-- --------------------------------------------------------

--
-- Table structure for table `safeplaces`
--

CREATE TABLE `safeplaces` (
  `id` int(11) NOT NULL,
  `alert_type` varchar(50) NOT NULL,
  `issued_by` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `location` varchar(100) NOT NULL,
  `safe_places` varchar(255) DEFAULT NULL,
  `intensity` varchar(50) DEFAULT NULL,
  `valid_until` date DEFAULT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `safeplaces`
--

INSERT INTO `safeplaces` (`id`, `alert_type`, `issued_by`, `date`, `location`, `safe_places`, `intensity`, `valid_until`, `description`, `created_at`) VALUES
(1, 'Earthquake', 'Suraksha Setu', '2025-03-01', 'Guntur, Andhra Pradesh', 'Lakshmipuram, Hollywood/Bollywood ', '5', '2025-03-03', '', '2025-01-21 04:05:25');

-- --------------------------------------------------------

--
-- Table structure for table `symptoms`
--

CREATE TABLE `symptoms` (
  `id` int(11) NOT NULL,
  `disease_id` int(11) DEFAULT NULL,
  `symptom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `symptoms`
--

INSERT INTO `symptoms` (`id`, `disease_id`, `symptom`) VALUES
(1, 1, 'High temperature'),
(2, 1, 'Sweating'),
(3, 1, 'Headache'),
(4, 1, 'Body pains'),
(6, 2, 'Loss of smell'),
(7, 2, 'Sore throat'),
(8, 2, 'Coughing'),
(9, 2, 'Sneezing'),
(10, 3, 'Fever'),
(11, 3, 'Head ache'),
(12, 3, 'Fatigue'),
(13, 3, 'Body pains'),
(14, 4, 'Increased thirst'),
(15, 4, 'Frequent urination'),
(16, 4, 'Fatigue'),
(17, 4, 'Weight loss'),
(18, 5, 'Anxiety'),
(19, 5, 'Nausea'),
(20, 5, 'Chest pain'),
(21, 5, 'Chest pain'),
(22, 6, 'Shortness of breath'),
(23, 6, 'Anxiety'),
(24, 6, 'Chest tightness'),
(25, 6, 'Coughing'),
(26, 7, 'Fever'),
(27, 7, 'Headache'),
(28, 7, 'Nausea'),
(29, 7, 'diarrhoea'),
(30, 8, 'Nausea'),
(31, 8, 'Fever'),
(32, 8, 'Skin rashes'),
(33, 8, 'Bodypains'),
(34, 9, 'vomitings'),
(35, 9, 'joint pains'),
(36, 9, 'Headache'),
(37, 9, 'High fever'),
(38, 10, 'bloating'),
(39, 10, 'nausea'),
(40, 10, 'Bellly pain'),
(41, 11, 'Joint pains'),
(42, 11, 'Fever'),
(43, 11, 'Skin rashes'),
(44, 11, 'Headache'),
(45, 12, 'vomitings'),
(46, 12, 'Nausea'),
(47, 12, 'Dehydration'),
(48, 13, 'Severe Weight loss'),
(49, 13, 'Fever'),
(50, 13, 'Breathing problem'),
(51, 14, 'Abnormal Bleeding'),
(52, 14, 'Severe Headache'),
(53, 14, 'Abnormal Weight loss'),
(54, 15, 'Joint pains'),
(55, 15, 'Loss of appetite'),
(56, 15, 'diarrhoea');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advancedlevel`
--
ALTER TABLE `advancedlevel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alerts`
--
ALTER TABLE `alerts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alert_history`
--
ALTER TABLE `alert_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `codehuntregistrations`
--
ALTER TABLE `codehuntregistrations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `team_name` (`team_name`);

--
-- Indexes for table `diseases`
--
ALTER TABLE `diseases`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `elitelevel`
--
ALTER TABLE `elitelevel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `government_users`
--
ALTER TABLE `government_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medications`
--
ALTER TABLE `medications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `disease_id` (`disease_id`);

--
-- Indexes for table `needs`
--
ALTER TABLE `needs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `public_users`
--
ALTER TABLE `public_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `safeplaces`
--
ALTER TABLE `safeplaces`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `symptoms`
--
ALTER TABLE `symptoms`
  ADD PRIMARY KEY (`id`),
  ADD KEY `disease_id` (`disease_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `advancedlevel`
--
ALTER TABLE `advancedlevel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT for table `alerts`
--
ALTER TABLE `alerts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `alert_history`
--
ALTER TABLE `alert_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `codehuntregistrations`
--
ALTER TABLE `codehuntregistrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=127;

--
-- AUTO_INCREMENT for table `diseases`
--
ALTER TABLE `diseases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `elitelevel`
--
ALTER TABLE `elitelevel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `government_users`
--
ALTER TABLE `government_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `medications`
--
ALTER TABLE `medications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `needs`
--
ALTER TABLE `needs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `public_users`
--
ALTER TABLE `public_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `safeplaces`
--
ALTER TABLE `safeplaces`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `symptoms`
--
ALTER TABLE `symptoms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `medications`
--
ALTER TABLE `medications`
  ADD CONSTRAINT `medications_ibfk_1` FOREIGN KEY (`disease_id`) REFERENCES `diseases` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `symptoms`
--
ALTER TABLE `symptoms`
  ADD CONSTRAINT `symptoms_ibfk_1` FOREIGN KEY (`disease_id`) REFERENCES `diseases` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
