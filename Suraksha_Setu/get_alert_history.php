<?php
include 'config.php'; // Include your database connection configuration

// Set header to output JSON
header('Content-Type: application/json');

// Fetch alert history data from the database
$sql = "SELECT id, latitude, longitude, alert_time FROM alert_history ORDER BY alert_time DESC";
$result = $conn->query($sql);

if ($result) {
    if ($result->num_rows > 0) {
        $alertHistory = array();
        while ($row = $result->fetch_assoc()) {
            $alertHistory[] = $row;
        }
        echo json_encode($alertHistory);
    } else {
        echo json_encode(array("message" => "No alert history found."));
    }
} else {
    echo json_encode(array("error" => "Error executing query: " . $conn->error));
}

$conn->close();
?>
