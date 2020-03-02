<?php
if($_POST){

    $email = $_POST['email'];
    $name = $_POST['name'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];

    $headers = "MIME-Version: 1.0\r\n";
    $headers .= "Content-type: text/plain; charset=iso-8859-1\r\n";
    $headers .= "From: $name <$email>\r\nReply-to : $name <$email>\nX-Mailer:PHP";

    $subject="$subject";
    $destinataire="apiou.kalene@gmail.com";
    $body="$message";

    if(mail($destinataire,$subject,$body,$headers)) {
    $response['status'] = 'success';
    $response['msg'] = 'Your mail is sent';
    } else {
    $response['status'] = 'error';
    $response['msg'] = 'Something went wrong';
    }

    echo json_encode($response);
}
if($_POST){

    $emailEnd = $_POST['emailEnd'];
    $nameEnd = $_POST['nameEnd'];
    $subjectEnd = $_POST['subjectEnd'];
    $messageEnd = $_POST['messageEnd'];

    $headers = "MIME-Version: 1.0\r\n";
    $headers .= "Content-type: text/plain; charset=iso-8859-1\r\n";
    $headers .= "From: $nameEnd <$emailEnd>\r\nReply-to : $nameEnd <$emailEnd>\nX-Mailer:PHP";

    $subject="$subjectEnd";
    $destinataire="apiou.kalene@gmail.com";
    $body="$messageEnd";

    if(mail($destinataire,$subject,$body,$headers)) {
    $response['status'] = 'success';
    $response['msg'] = 'Your mail is sent';
    } else {
    $response['status'] = 'error';
    $response['msg'] = 'Something went wrong';
    }

    echo json_encode($response);
}
?>