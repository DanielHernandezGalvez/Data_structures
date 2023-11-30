<?php 
$dbHost = "localhost";
$dbUser = "root";
$dbPass = "";
$dbName = "cms";

$conn = mysqli_connect($dbHost, $dbUser, $dbPass, $dbName);
if(!$conn){
    die("Someting is wrong, cannot connect with the database");
}
?>
