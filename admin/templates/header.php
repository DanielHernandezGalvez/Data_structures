<?php 
session_start();
if(!isset($_SESSION["user"])){
    header("Location:login.php");
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>

<body>

    <div class="dasboard d-flex justify-content-between">
        <div class="sidebar bg-dark vh-100">
            <h1 class="bg-primary"><a href="./index.php" class="text-light text-decoration-none">Dashboard</a></h1>
            <div class="menus p-4 mt-5">
                <div class="menu">
                    <a class="text-light text-decoration-none" href="create.php "><strong>Add new Post</strong></a>
                </div>
                <div class="menu mt-5">
                    <a class="btn btn-info" href="logout.php">Log out</a>
                </div>
            </div>
        </div>