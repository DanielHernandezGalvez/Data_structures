<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
</head>

<body>

    <div class="dasboard">
        <div class="sidebar">

        </div>
        <div class="create-form">

            <form action="">
                <input type="text" name="title" id="">
                <div class="form-field">
                    <textarea name="summary" id="" cols="30" rows="10" placeholder="Enter summary:"></textarea>
                </div>

                <div class="form-field">
                    <textarea name="content" id="" cols="30" rows="10" placeholder="Enter post:"></textarea>
                </div>

                <input type="hidden" name="date" value="<?php echo date("Y/m/d") ?>">

                <div class="form-field">
                    <input type="submit" value="Submit" name="create">
                </div>
            </form>

        </div>
    </div>

</body>

</html>