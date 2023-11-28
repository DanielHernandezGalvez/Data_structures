<?php
include("templates/header.php");
?>

<div class="posts-list w-100 p-5">
    <table class="table tabled-bordered">
        <thead>
            <td>Publication Date</td>
            <td>Title</td>
            <td>Article</td>
            <td>Action</td>
        </thead>
        <tbody>
            <tr>
                <?php
                include("../connect.php");
                $sqlSelect = "SELECT * FROM posts";
                $result = mysqli_query($conn, $sqlSelect);
                while ($data = mysqli_fetch_array($result)) {
                ?>
                    <td><?php echo $data["date"]; ?></td>
                    <td><?php echo $data["title"]; ?></td>
                    <td><?php echo $data["summary"]; ?></td>
                    <td>
                        <a class="btn btn-info" href="view.php?id=<?php echo $data["date"]; ?>">View</a>
                        <a class="btn btn-warning" href="edit.php?id=<?php echo $data["date"]; ?>">Edit</a>
                        <a class="btn btn-danger" href="delete.php?id=<?php echo $data["date"]; ?>">Delete</a>
                    </td>
            </tr>
        <?php
                }
        ?>
        </tbody>
    </table>
</div>

<?php
include("templates/footer.php");
?>