<?php
include 'config.php';
header('Content-Type: application/json');

// Enable error logging
ini_set('log_errors', 1);
ini_set('error_log', 'php_errors.log');
error_reporting(E_ALL);

$disease = isset($_GET['disease']) ? $_GET['disease'] : '';

if ($disease) {
    error_log("Received request for disease: " . $disease);

    // Retrieve disease id
    $stmt = $conn->prepare("SELECT id FROM diseases WHERE name = ?");
    if (!$stmt) {
        error_log("Failed to prepare statement: " . $conn->error);
        die(json_encode(['error' => 'Failed to prepare statement']));
    }
    $stmt->bind_param("s", $disease);
    $stmt->execute();
    $stmt->bind_result($disease_id);
    $stmt->fetch();
    $stmt->close();

    if ($disease_id) {
        error_log("Disease ID found: " . $disease_id);

        // Retrieve symptoms
        $symptoms = [];
        $stmt = $conn->prepare("SELECT symptom FROM symptoms WHERE disease_id = ?");
        if (!$stmt) {
            error_log("Failed to prepare statement: " . $conn->error);
            die(json_encode(['error' => 'Failed to prepare statement']));
        }
        $stmt->bind_param("i", $disease_id);
        $stmt->execute();
        $result = $stmt->get_result();
        while ($row = $result->fetch_assoc()) {
            $symptoms[] = $row['symptom'];
        }
        $stmt->close();
        error_log("Symptoms retrieved: " . json_encode($symptoms));

        // Retrieve medications
        $medications = [];
        $stmt = $conn->prepare("SELECT medication FROM medications WHERE disease_id = ?");
        if (!$stmt) {
            error_log("Failed to prepare statement: " . $conn->error);
            die(json_encode(['error' => 'Failed to prepare statement']));
        }
        $stmt->bind_param("i", $disease_id);
        $stmt->execute();
        $result = $stmt->get_result();
        while ($row = $result->fetch_assoc()) {
            $medications[] = $row['medication'];
        }
        $stmt->close();
        error_log("Medications retrieved: " . json_encode($medications));

        echo json_encode(['symptoms' => $symptoms, 'medications' => $medications]);
    } else {
        echo json_encode(['error' => 'Disease not found']);
    }
} else {
    echo json_encode(['error' => 'No disease specified']);
}

$conn->close();
?>