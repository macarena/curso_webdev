<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="UTF-8">
</head>
<?php

foreach ($_POST as $campo => $valor) {
?>
	<p><?=$campo?>: <?=$valor?></p>
<?php
}

?>