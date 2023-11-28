<?php
if(isset($_POST["create"])) {
    include("../connect.php");
    $title = mysqli_escape_string($conn, $_POST["title"]);
    $summary = mysqli_escape_string($conn, $_POST["summary"]);
    $content = mysqli_escape_string($conn, $_POST["content"]);
    $date = mysqli_escape_string($conn, $_POST["date"]);

    $sqlinsert = "INSERT INTO posts(date, title, summary, content) VALUES ('$date', '$title', '$summary', '$content')";

    if(mysqli_query($conn, $sqlinsert)){

    } else {
        die("Data is not inserted");
    }
    // echo $title;
    // echo $summary;
    // echo $content;
    // echo $date;
}
?>