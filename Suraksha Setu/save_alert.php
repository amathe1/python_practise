<?php
include 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $alert_type = $_POST['alert'];
    $issued_by = $_POST['issuedBy'];
    $date = $_POST['date'];
    $location = $_POST['location'];
    $safe_places = $_POST['safeplaces'];
    $intensity = $_POST['intensity'];
    $valid_until = $_POST['validUntil'];
    $description = $_POST['description'];

    $sql = "INSERT INTO safeplaces (alert_type, issued_by, date, location, safe_places, intensity, valid_until, description)
            VALUES ('$alert_type', '$issued_by', '$date', '$location', '$safe_places', '$intensity', '$valid_until', '$description')";

    if ($conn->query($sql) === TRUE) {
        echo "<p id='success-message'>New record created successfully</p>";
        echo "<script>
                setTimeout(function() {
                    window.location.href = 'adminpanel.html';
                }, 3000);
              </script>";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>
