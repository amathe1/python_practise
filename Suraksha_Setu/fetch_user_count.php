<?php
include 'config.php'; // Include the database configuration file

// Fetch total number of users
$sql = "SELECT COUNT(*) AS total_users FROM public_users";
$result = $conn->query($sql);

$total_users = $result->fetch_assoc()['total_users'];

// Return data as JSON
echo json_encode(['total_users' => $total_users]);

$conn->close();
?>
