<?php 
extract($_POST);
$servername = "localhost";
$username = "root";
$password = "";
$groupone = 0 ;
$grouptwo = 0;
$groupthree = 0;
$groupfour = 0;
$groupfive = 0;
if($queone == "Yes")
{
	$groupone = $groupone + 10;
}
if($quetwo == "Yes")
{
	$groupone = $groupone + 10;
}
if($quethree)
{
	$grouptwo = $grouptwo + $quethree;
}
if($quefour == "Yes")
{
	$grouptwo = $grouptwo + 5;
}
if($quefive)
{
	$grouptwo = $grouptwo + $quefive;
}
if($quesix == "Yes")
{
	$groupone = $groupone + 7;
}
if($queseven == "Yes")
{
	$grouptwo = $grouptwo + 5;
}
if($queeight == "Yes")
{
	$grouptwo = $grouptwo + 4;
}
if($quenine == "Yes")
{
	$grouptwo = $grouptwo + 7;
}
if($queten == "Yes")
{
	$groupthree = $groupthree + 10;
}
if($queeleven == "Yes")
{
	$groupthree = $groupthree + 10;
}
if($quetwelve == "Yes")
{
	$groupthree = $groupthree + 8;
}
if($quethirteen == "Yes")
{
	$groupthree = $groupthree + 10;
}
if($quefourteen == "Yes")
{
	$groupthree = $groupthree + 9;
}
if($quefifteen == "Yes")
{
	$groupthree = $groupthree + 8;
}
if($quesixteen == "Yes")
{
	$groupthree = $groupthree + 7;
}
if($queseventeen)
{
	$groupfour = $groupfour + $queseventeen;
}
if($queeighteen)
{
	$groupfour = $groupfour + $queeighteen;
}
if($quenineteen == "Yes")
{
	$groupfour = $groupfour + 9;
}
if($quetwenty == "Yes")
{
	$groupfour = $groupfour + 8;
}
if($quetwentyone == "Yes")
{
	$groupfour = $groupfour + 6;
}
if($quetwentytwo == "Yes")
{
	$groupfour = $groupfour + 9;
}
if($quetwentythree == "Yes")
{
	$groupone = $groupone + 7;
}
if($quetwentyfour == "Yes")
{
	$groupfour = $groupfour + 7;
}
if($quetwentyfour == "No")
{
	$groupfour = $groupfour - 7;
}
if($quetwentyfive == "Yes")
{
	$groupfive = $groupfive + 8;
}
if($quetwentysix == "Yes")
{
	$groupfive = $groupfive - $quetwentysix;
}


$conn = mysql_connect($servername, $username, $password);
mysql_select_db('smartjacket_sensors');

$sql = "TRUNCATE TABLE questionnaire_answer";
$retval = mysql_query($sql,$conn);

$sql = "TRUNCATE TABLE questionnaire_processed";
$retval = mysql_query($sql,$conn);

$sql = "TRUNCATE TABLE quest";
$retval = mysql_query($sql,$conn);

$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (1, '$queone')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (2, '$quetwo')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (3, '$quethree')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (4, '$quefour')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (5, '$quefive')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (6, '$quesix')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (7, '$queseven')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (8, '$queeight')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (9, '$quenine')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (10, '$queten')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (11, '$queeleven')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (12, '$quetwelve')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (13, '$quethirteen')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (14, '$quefourteen')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (15, '$quefifteen')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (16, '$quesixteen')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (17, '$queseventeen')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (18, '$queeighteen')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (19, '$quenineteen')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (20, '$quetwenty')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (21, '$quetwentyone')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (22, '$quetwentytwo')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (23, '$quetwentythree')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (24, '$quetwentyfour')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (25, '$quetwentyfive')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_answer (question_number, answer) VALUES (26, '$quetwentysix')";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
//This is for the processed data table.
$sql = "INSERT INTO questionnaire_processed (group_id , group_index) VALUES (1, $groupone)";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_processed (group_id , group_index) VALUES (2, $grouptwo)";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_processed (group_id , group_index) VALUES (3, $groupthree)";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_processed (group_id , group_index) VALUES (4, $groupfour)";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
$sql = "INSERT INTO questionnaire_processed (group_id , group_index) VALUES (5, $groupfive)";
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}

$grone = 0;
$grtwo = 0;
$grthree = 0;
$grfour = 0;
$grfive = 0;
$grtotal = 0;

if($groupone<10)
{
	$grone = 1;
}
else if($groupone>9 && $groupone<20)
{
	$grone = 2;
}
else
{
	$grone = 3;
}

if($grouptwo<7)
{
	$grtwo = 1;
}
else if($grouptwo>7 && $grouptwo<35)
{
	$grtwo = 2;
}
else
{
	$grtwo = 3;
}

if($groupthree<21)
{
	$grthree = 1;
}
else if($groupthree>20 && $groupthree<41)
{
	$grthree = 2;
}
else
{
	$grthree = 3;
}

if($groupfour<7)
{
	$grfour = 1;
}
else if($groupfour>7 && $groupfour<35)
{
	$grfour = 2;
}
else
{
	$grfour = 3;
}

if($groupfive<21)
{
	$grfive = 1;
}
else if($groupfive>20 && $groupfive<41)
{
	$grfive = 2;
}
else
{
	$grfive = 3;
}


$grtotal = $grone + $grtwo + $grthree + $grfour + $grfive ;

if($grtotal>=9)
{
	$str_final = "highques";
}
else if($grtotal>=7 && $grtotal<9)
{
	$str_final = "mediumques";
}
else
{
	$str_final = "lowques";
}
if($queone == "Yes")
{
	$gsr = "Y";
}
else
{
	$gsr = "N";
}

$sql = "INSERT INTO quest (level, ifgsr) VALUES ('$str_final', '$gsr')";
$retval = mysql_query( $sql, $conn );

//header("location:javascript://history.go(-2)");
header("location:../Main.html");
mysql_close($conn);
?>
