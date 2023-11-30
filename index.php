<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple blog</title>
</head>

<body>
    <header class="p-4 bg-dark text-center">
        <h1>Simple blog</h1>
    </header>
    <div class="post-list">
        <?php
        include("connect.php");
        $sqlSelect = "SELECT * FROM posts";
        $result = mysqli_query($conn, $sqlSelect);
        while ($data = mysqli_fetch_array($result)) {
            ?>
                <div class="row mb-4">
                    <div class="col-sm-2">
                        <?php echo $data["date"]; ?>
                    </div>
                    <div class="col-sm-2">
                        <?php echo $data["title"]; ?>
                    </div>
                    <div class="col-sm-5">
                        <?php echo $data["content"]; ?>
                    </div>
                    <div class="col-sm-3">
                        <a href="view.php<?php echo $data["id"]; ?>" class="btn btn-primary">READ MORE</a>
                    </div>
                </div>
            <?php
        }
        ?>
    </div>
</body>

</html>