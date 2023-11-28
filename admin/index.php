<?php
include("templates/header.php");
?>

<div class="posts-list">
    <table class="table tabled-bordered">
        <thead>
            <td>Publication Date</td>
            <td>Title</td>
            <td>Article</td>
            <td>Action</td>
        </thead>
        <tbody>
            <?php
                include("../connect.php");
                $sqlSelect = "SELECT * FROM posts";
                $result = mysqli_query($conn, $sqlSelect);
                while($data = mysqli_fetch_array($result)) {
                    ?>

                    <?php
                }
            ?>
        </tbody>
    </table>
</div>

<?php
include("templates/footer.php");
?>