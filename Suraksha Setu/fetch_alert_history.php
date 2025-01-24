<?php
include 'config.php'; // Include your database connection configuration

$sql = "SELECT id, latitude AS lat, longitude AS lng, alert_time FROM alert_history";
$result = $conn->query($sql);

$records = array();

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        // Convert alert_time to the desired time zone (e.g., Asia/Kolkata)
        $dateTime = new DateTime($row['alert_time'], new DateTimeZone('UTC'));
        $dateTime->setTimezone(new DateTimeZone('Asia/Kolkata')); // Change this to your desired time zone
        $row['alert_time'] = $dateTime->format('Y-m-d H:i:s');

        $records[] = $row;
    }
}

header('Content-Type: application/json');
echo json_encode($records);

$conn->close();
?>
