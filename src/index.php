<?php

include_once 'head.php';
include_once 'header.php';
?>

<div class="container">

       <h1 class="m-3 text-center">Adresse IP du serveur: <?= $_SERVER['HTTP_HOST']?></h1>

       <div class="d-flex flex-wrap justify-content-between">
              <?php for ($i=0; $i < 6 ; $i++) { ?>
              <div class="card bg-light mb-3 m-3 col-3" style="max-width: 18rem;">
                     <div class="card-header">Cible <?= $i ?></div>
                     <div class="card-body">
                            <h5 class="card-title">Light card title</h5>
                            <a class="btn btn-primary" href="cmd.php?id=<?= $i ?>">Go</a>
                     </div>
              </div>
              <?php     
              }?>
       </div>
</div>

</html>