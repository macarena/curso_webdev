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

foreach ($_FILES as $arquivo) {
	
	$arquivo_tmp = $aquivo['tmp_name'];
	$destino = 'img/' . $arquivo['name'];

	move_uploaded_file( $arquivo_tmp, $destino );

	?>

	<img src="<?=$destino?>">

<?
}
?>
