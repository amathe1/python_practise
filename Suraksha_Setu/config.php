<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

/* Database credentials */
define('DB_SERVER', 'localhost');
define('DB_PORT', '3306');
define('DB_USERNAME', 'sivaji');
define('DB_PASSWORD', 'EY348*yhZcB$');
define('DB_NAME', 'csdm');

/* Attempt to connect to MySQL database */
$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME, DB_PORT);

// Check connection
if ($conn === false) {
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
?>