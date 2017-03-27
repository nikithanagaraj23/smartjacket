<?php
	
	
	//query to insert computed values of priority
	
	//$query="INSERT INTO calendar_processed(`eventDate`,`eventPriority`) SELECT eventDate,SUM(value) FROM `calendar_raw` GROUP BY eventDate";
	//$query="REPLACE INTO calendar_processed(`eventDate`,`eventPriority`) SELECT eventDate,SUM(value) FROM `calendar_raw` GROUP BY eventDate";

	$query="SELECT * FROM calendar_processed;";
	$conn = mysql_connect('127.0.0.1','root','');
	
	if(!$conn)
	{		
		die("Could not connect to database server");
	}
	$db = mysql_select_db('smartJacket');
	if(!$db)
	{
		die("Could not select 'smartJacket' database");
	}
	
	//$results = mysql_query($query);
		
	

	//$myArray=array();
	
	if ($result = mysql_query($query)) {

    while($row = mysql_fetch_array($result,MYSQL_ASSOC)) {
            $myArray1[] = $row["eventDate"];
            $myArray2[] = $row["eventPriority"];
			
    }
    //echo json_encode($myArray1);
 
	//echo json_encode($myArray2);
$myArray=array();
$myArray=[$myArray1,$myArray2];

echo json_encode($myArray);
	
	}
	
	
	

mysql_close($conn);


?>