
<?php
$link = mysql_connect('localhost');
if (!$link) {
    die('Não foi possível conectar: ' . mysql_error());
}
echo 'Conexão bem sucedida';

$resultado = mysql_query("SELECT * FROM produtos");

print_r($resultado);

mysql_close($link);
?>
