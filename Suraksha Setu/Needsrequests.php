<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Needs Data</title>
    <link rel="icon" type="image/jpg" href="croppedimage.png">
    <style>
       /* General Styles */
       body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #e0e5ec;
}

.container {
    width: 90%;
    margin: 60px auto;
    background-color: #ffffff;
    padding: 24px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1), 0 6px 6px rgba(0, 0, 0, 0.1);
    border-radius: 30px;
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.container:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2), 0 8px 8px rgba(0, 0, 0, 0.2);
}

.header {
    text-align: center;
    margin-bottom: 20px;
}

.header h1 {
    color: #007acc;
    font-size: 36px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
    position: relative;
}

.header h1::after {
    content: '';
    width: 60px;
    height: 4px;
    background-color: #007acc;
    display: block;
    margin: 10px auto 0;
    border-radius: 2px;
}

/* Table Styles */
table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.05);
}

th, td {
    padding: 14px 20px;
    text-align: left;
    border-bottom: 1px solid #dddddd;
}

th {
    background-color: #007acc;
    color: white;
    text-transform: uppercase;
}

tr:nth-child(even) {
    background-color: #ffffff;
}

tr:hover {
    background-color: #e0f7ff;
    transition: background-color 0.3s;
}

/* Delivered Cell Styles */
.delivered-cell {
    font-weight: bold;
    text-align: center;
    color: #28a745;
}

/* Button Styles */
.delete-button, .delivery-button {
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s, transform 0.3s;
    text-transform: uppercase;
    font-weight: bold;
}

.delete-button {
    background-color: #ff4d4d;
    color: white;
}

.delete-button:hover {
    background-color: #ff1a1a;
}

.delete-button:active {
    background-color: #cc0000;
    transform: scale(0.95);
}

.delivery-button {
    background-color: #4caf50;
    color: white;
}

.delivery-button:hover {
    background-color: #45a049;
}

.delivery-button:active {
    transform: scale(0.95);
}

/* Back Button Styles */
.back-button {
    position: fixed;
    top: 20px;
    left: 10px;
    padding: 12px;
    border: none;
    background-color: transparent;
    cursor: pointer;
    border-radius: 50%;
    z-index: 9999;
    transition: transform 0.3s ease-in-out, background-color 0.3s;
}

.back-button:hover {
    transform: scale(1.1);
    background-color: rgba(0, 122, 204, 0.1);
}

.back-button svg {
    width: 35px;
    height: 35px;
    fill: #007acc;
}

/* Additional Modern Enhancements */
header h1::after {
    content: '';
    width: 60px;
    height: 4px;
    background-color: #007acc;
    display: block;
    margin: 10px auto 0;
    border-radius: 2px;
}

th, td {
    padding: 14px 20px;
    text-align: left;
    border-bottom: 1px solid #dddddd;
}

th {
    background-color: #007acc;
    color: white;
    text-transform: uppercase;
}

tr:nth-child(even) {
    background-color: #ffffff;
}

tr:hover {
    background-color: #e0f7ff;
    transition: background-color 0.3s;
}

/* Delivered Cell Styles */
.delivered-cell {
    font-weight: bold;
    text-align: center;
    color: #28a745;
}

/* Button Styles */
.delete-button, .delivery-button {
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s, transform 0.3s;
    text-transform: uppercase;
    font-weight: bold;
}

.delete-button {
    background-color: #ff4d4d;
    color: white;
}

.delete-button:hover {
    background-color: #ff1a1a;
}

.delete-button:active {
    background-color: #cc0000;
    transform: scale(0.95);
}

.delivery-button {
    background-color: #4caf50;
    color: white;
}

.delivery-button:hover {
    background-color: #45a049;
}

.delivery-button:active {
    transform: scale(0.95);
}

/* Back Button Styles */
.back-button {
    position: fixed;
    top: 20px;
    left: 10px;
    padding: 12px;
    border: none;
    background-color: transparent;
    cursor: pointer;
    border-radius: 50%;
    z-index: 9999;
    transition: transform 0.3s ease-in-out, background-color 0.3s;
}

.back-button:hover {
    transform: scale(1.1);
    background-color: rgba(0, 122, 204, 0.1);
}

.back-button svg {
    width: 35px;
    height: 35px;
    fill: #007acc;
}

    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Needs Data</h1>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Mobile</th>
                    <th>State</th>
                    <th>District</th>
                    <th>Address</th>
                    <th>Essentials</th>
                    <th>Extra Needs</th>
                    <th>Delivered</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
<?php
// Include the database configuration file
include 'config.php';

// Function to sanitize input for security
function sanitizeInput($input) {
    global $conn;
    return mysqli_real_escape_string($conn, htmlspecialchars(strip_tags($input)));
}

// Fetch the needs data from the database
$sql = "SELECT * FROM needs";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        // Initialize delivered status as "Active" by default if 'delivered' key is not set
        $delivered = isset($row["delivered"]) ? ($row["delivered"] ? "Inactive" : "Active") : "Active";
        $buttonClass = $delivered === "Active" ? "active-button" : "inactive-button";
        $buttonText = $delivered === "Active" ? "Active" : "Inactive";

        echo "<tr>
                <td>" . sanitizeInput($row["name"]) . "</td>
                <td>" . sanitizeInput($row["mobile"]) . "</td>
                <td>" . sanitizeInput($row["state"]) . "</td>
                <td>" . sanitizeInput($row["district"]) . "</td>
                <td>" . sanitizeInput($row["address"]) . "</td>
                <td>" . sanitizeInput($row["essentials"]) . "</td>
                <td>" . sanitizeInput($row["extra_needs"]) . "</td>
                <td id='delivered-" . sanitizeInput($row["id"]) . "' class='delivered-cell'>
                    <button class='delivery-button " . $buttonClass . "' onclick='toggleDelivery(" . sanitizeInput($row["id"]) . ")'>" . $buttonText . "</button>
                </td>
                <td>
                    <button class='delete-button' onclick='deleteRow(" . sanitizeInput($row["id"]) . ")'>Delete</button>
                </td>
              </tr>";
    }

    echo "</tbody></table>";
} else {
    echo "No data available";
}
// Close connection
$conn->close();
?>

            </tbody>
        </table>
        <button class="back-button" id="back"><svg xmlns="http://www.w3.org/2000/svg" width="35" height="40" fill="currentColor" class="bi bi-arrow-left-circle" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8m15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-4.5-.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
          </svg></button>
    </div>
   
    <script>
    function toggleDelivery(id) {
        var button = document.getElementById('delivered-' + id).querySelector('button');
        var currentStatus = button.textContent.trim();

        if (currentStatus === "Active") {
            button.textContent = "Inactive";
            button.classList.remove('active-button');
            button.classList.add('inactive-button');
        } else {
            button.textContent = "Active";
            button.classList.remove('inactive-button');
            button.classList.add('active-button');
        }

        // Send AJAX request to update delivered status in the database
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'update_delivery.php', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                // Handle response if needed
            }
        };
        xhr.send('id=' + id + '&status=' + currentStatus);
    }

    function deleteRow(id) {
        if (confirm("Are you sure you want to delete this record?")) {
            // Send AJAX request to delete record
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'delete_record.php', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                    // Remove the row from the table on successful delete
                    var row = document.getElementById('delivered-' + id).parentNode.parentNode;
                    row.parentNode.removeChild(row);
                }
            };
            xhr.send('id=' + id);
        }
    }
    
        document.getElementById("back").addEventListener("click", function() {
          window.location.href = "adminpanel.html";
        });
        
</script>
</body>
</html>