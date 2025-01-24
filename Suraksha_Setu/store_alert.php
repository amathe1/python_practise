<?php
include 'config.php'; // Include your database connection configuration

if (isset($_POST['latitude']) && isset($_POST['longitude']) && isset($_POST['timestamp'])) {
    $latitude = $_POST['latitude'];
    $longitude = $_POST['longitude'];
    $timestamp = $_POST['timestamp']; // This should be in ISO format

    // Prepare and execute insert query
    $sql = "INSERT INTO alert_history (latitude, longitude, alert_time) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("dds", $latitude, $longitude, $timestamp);

    if ($stmt->execute()) {
        echo "Alert record stored successfully.";
    } else {
        echo "Error storing alert record: " . $stmt->error;
    }

    $stmt->close();
} else {
    echo "Missing parameters.";
}

$conn->close();
?>
