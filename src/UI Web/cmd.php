<?php

$id = strval($_GET['id']);
session_start();
empty($_SESSION['log'. $id ]) ? $_SESSION['log'. $id ] = [] : $_SESSION['log'. $id  ] = $_SESSION['log'. $id ];
include_once 'head.php';
include_once 'header.php';
?>

<div class="container mt-3">
       <form method="post" class="input-group mb-3" name="oui">
              <input type="text" name="oui" class="form-control" aria-label="Recipient's username"
                     aria-describedby="button-addon2">
              <div class="input-group-append">
                     <button class="btn btn-outline-secondary" type="submit" id="button-addon2">Executer</button>
              </div>
       </form>

       <?php if (isset($_POST['oui']) && !empty($_POST['oui'])) {
              $output = shell_exec('python server.py' .htmlspecialchars($_POST['oui']) )
              ?>
       <div class="border rounded p-3 border-secondary">
              <p><?= utf8_encode($output) ?></p>
       </div>
       <?php
       } ?>

       <?php if (isset($_SESSION['log'. $id ])) { ?>
       <!-- ================================================== -->
       <div class="border rounded p-3 border-secondary mt-3 overflow-auto">

              <h2 class="text-center m-3">Log</h2>
              <hr>
              <ul class="list-group list-group-flush">
                     <?php foreach ($_SESSION['log'. $id ] as $cmd) { ?>
                            <li class="list-group-item"><?= $cmd ?></li>
                     <?php
                     } ?>
              </ul>
       </div>
       <!-- ================================================== -->
       <?php
       } ?>
</div>

</html>