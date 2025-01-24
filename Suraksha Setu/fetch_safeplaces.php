<?php
require_once 'config.php';

$sql = "SELECT * FROM safeplaces";
$result = $conn->query($sql);

$alerts = [];
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $alerts[] = $row;
    }
}

echo json_encode($alerts);

$conn->close();
?>
