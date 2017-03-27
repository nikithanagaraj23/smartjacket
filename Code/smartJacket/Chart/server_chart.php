<?php
	
	
	//query to insert computed values of priority
	
	//$query="INSERT INTO calendar_processed(`eventDate`,`eventPriority`) SELECT eventDate,SUM(value) FROM `calendar_raw` GROUP BY eventDate";
	//$query="REPLACE INTO calendar_processed(`eventDate`,`eventPriority`) SELECT eventDate,SUM(value) FROM `calendar_raw` GROUP BY eventDate";

	$query="SELECT * FROM calendar_processed;";
	$query1="SELECT * FROM `graph` WHERE 1";

$servername = "localhost";
$username = "root";
$password = "";
$conn = mysql_connect($servername, $username, $password);
mysql_select_db('smartjacket_sensors');
	
	
	//$results = mysql_query($query);
		
	

	//$myArray=array();
	
	$result = mysql_query($query);
	
	$result1=mysql_query($query1);

    while($row = mysql_fetch_array($result,MYSQL_ASSOC)) {
            $myArray1[] = $row["eventDate"];
            $myArray2[] = $row["eventPriority"];
			
    }
	
    while($row = mysql_fetch_array($result1,MYSQL_ASSOC)) {
            $myArray3[] = $row["time"];
            $myArray4[] = $row["value"];
			$myArray5[]=$row["level"];
			
    }
    //echo json_encode($myArray1);
 
	//echo json_encode($myArray2);
//$myArray=array();
//$myArray=[$myArray1,$myArray2,$myArray3,$myArray4,$myArray5];
$myArray=array();
$s=sizeof($myArray3);

$myArray3_1=array_slice($myArray3,$s-20);
$myArray4_1=array_slice($myArray4,$s-20);
$myArray5_1=array_slice($myArray5,$s-20);


$myArray=[$myArray1,$myArray2,$myArray3_1,$myArray4_1,$myArray5_1];
//$myArray=array();
//$myArray=[$myArray1,$myArray2,$myArray3,$myArray4,$myArray5];

echo json_encode($myArray);
	
	
	
	

mysql_close($conn);


?>