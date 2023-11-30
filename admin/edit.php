<?php
include("templates/header.php");
?>

<?php
$id = $_GET["id"];
if ($id) {
    include("../connect.php");
    $sqlEdit = "SELECT * FROM posts WHERE id = $id";
    $result = mysqli_query($conn, $sqlEdit);
} else {
    echo "not found post";
}

?>

<div class="create-form w-100 mx-auto p-4" style="max-width: 700px;">
    <form action="process.php" method="post">
        <?php
        while ($data = mysqli_fetch_array($result)) {
        ?>


            <div class="form-field  mb-4">
                <input type="text" class="form-control" name="title" id="" placeholder="Enter title:" value="<?php echo $data["title"]; ?>">
            </div>

            <div class="form-field  mb-4">
                <textarea name="summary" id="" class="form-control" cols="30" rows="10" placeholder="Enter summary:"><?php echo $data["summary"]; ?></textarea>
            </div>

            <div class="form-field">
                <textarea name="content" id="" class="form-control" cols="30" rows="10" placeholder="Enter post:"><?php echo $data["content"]; ?></textarea>
            </div>
            <input type="hidden" name="id" value="<?php echo $id; ?>">
            <input type="hidden" name="date" value="<?php echo date("Y/m/d") ?>">

            <div class="form-field my-4">
                <input type="submit" class="btn btn-primary" value="Submit" name="update">
            </div>
        <?php
        }
        ?>
    </form>
</div>
<?php
include("templates/footer.php");
?>