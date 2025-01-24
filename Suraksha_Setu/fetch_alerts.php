<?php
// fetch_alerts.php

include 'config.php';

// Fetch alerts from database
$result = $conn->query("SELECT alert_type, alert_date, alert_time, alert_area FROM alerts ORDER BY id DESC LIMIT 1");

$alerts = [];
while ($row = $result->fetch_assoc()) {
    $alerts[] = [
        'alertType' => $row['alert_type'],
        'alertDate' => $row['alert_date'],
        'alertTime' => $row['alert_time'],
        'alertArea' => $row['alert_area']
    ];
}

if (!empty($alerts)) {
    echo json_encode(['success' => true, 'alerts' => $alerts]);
} else {
    echo json_encode(['success' => false, 'message' => 'No alerts found']);
}

$conn->close();
?>