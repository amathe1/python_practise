<?php
include 'config.php';

// Fetch the count from the database
$sql = "SELECT count FROM bluetooth_count WHERE id = 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo json_encode(['count' => $row['count']]);
} else {
    echo json_encode(['count' => 0]);
}

$conn->close();
?>
