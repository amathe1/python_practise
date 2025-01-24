<?php
// send_alert.php

// Include database configuration
include 'config.php';

// Retrieve POST data
$data = json_decode(file_get_contents('php://input'), true);

// Check if all required fields are present
if (isset($data['alertType']) && isset($data['alertDate']) && isset($data['alertTime']) && isset($data['alertArea'])) {
    $alertType = $data['alertType'];
    $alertDate = $data['alertDate'];
    $alertTime = $data['alertTime'];
    $alertArea = $data['alertArea'];

    // Prepare and bind SQL statement
    $stmt = $conn->prepare("INSERT INTO alerts (alert_type, alert_date, alert_time, alert_area) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $alertType, $alertDate, $alertTime, $alertArea);

    // Execute SQL statement
    if ($stmt->execute()) {
        echo json_encode(['success' => true]);
    } else {
        echo json_encode(['success' => false, 'message' => 'Database insert failed: ' . $stmt->error]);
    }

    // Close statement and connection
    $stmt->close();
    $conn->close();
} else {
    // If any required field is missing
    echo json_encode(['success' => false, 'message' => 'Invalid input']);
}
?>