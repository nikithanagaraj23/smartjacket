<?php

$servername = "localhost";
$username = "root";
$password = "";
$conn = mysql_connect($servername, $username, $password);
mysql_select_db('smartjacket_sensors');
$sql = "SELECT answer FROM questionnaire_answer WHERE question_number = 5";
$retval = mysql_query( $sql, $conn );
$ans = mysql_fetch_row($retval);
if($ans[0]>=4)
{
	echo("Start earlier to escape peak hour traffic.");
	echo "<br>";
}

$sql = "SELECT answer FROM questionnaire_answer WHERE question_number = 3";
$retval = mysql_query( $sql, $conn );
$ans = mysql_fetch_row($retval);
if($ans[0]<5)
{
	echo("Switch from caffinated to decaffeinated coffee or herbal tea. Leave work at lunchtime to take a short walk or relax outside your work environment.Take a 5-minute relaxation break – practice a relaxation exercise.
\n");
	echo "<br>";
}

$sql = "SELECT answer FROM questionnaire_answer WHERE question_number = 7";
$retval = mysql_query( $sql, $conn );
$ans = mysql_fetch_row($retval);
if($ans[0] == "Yes")
{
	echo("Contact human resources to clear the air. Conversation is key to solving every problem\n");
	echo "<br>";
}

$sql = "SELECT answer FROM questionnaire_answer WHERE question_number = 14";
$retval = mysql_query( $sql, $conn );
$ans = mysql_fetch_row($retval);
if($ans[0] == "Yes")
{
	echo("Approach a professional for counselling. \n");
	echo "<br>";
}

$sql = "SELECT answer FROM questionnaire_answer WHERE question_number = 25";
$retval = mysql_query( $sql, $conn );
$ans = mysql_fetch_row($retval);
if($ans[0] == "Yes")
{
	echo("Approach a dietician for stabilising a healthy weight for your age and height. Also eat lots of fruits and vegetables and drink lots of water.\n");
	echo "<br>";
}

$sql = "SELECT eventDate FROM calendar_processed WHERE level='highcal'";
$retval = mysql_query( $sql, $conn );

while($row = mysql_fetch_array($retval,MYSQL_ASSOC))
	{
		
		foreach($row as $key=>$value)
		{
			echo "You have a very busy schedule on this day.";
			echo "$key---$value";
			echo "Try and readjust your schedule if possible or try and be better prepared for your meetings in order to boost your confidence.";
		}
		
	}





?>