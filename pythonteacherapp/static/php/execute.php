<?php

    $language = 'python';
    $code = $_POST['code'];
    echo($language);
    $random = substr(md5(mt_rand()), 0, 7);
    $filePath = "temp/" . $random . "." . $language;
    $programFile = fopen($filePath, "w");
    fwrite($programFile, $code);
    fclose($programFile);

    // Execute the code based on the selected language
    if ($language == "python") {
        $output = shell_exec("C:\Program Files\Python310\python.exe $filePath 2>&1");
        echo $output;
    } else {
        // Handle other languages here
    }

?>
