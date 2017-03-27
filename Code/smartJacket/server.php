<?php
	//extract($_GET);
	
	
$monthNames=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
	$query1="DELETE FROM `calendar_raw` WHERE 1";
	$conn = mysql_connect('127.0.0.1','root','');
	if(!$conn)
	{		
		die("Could not connect to database server");
	}
	$db = mysql_select_db('smartJacket_sensors');
	if(!$db)
	{
		die("Could not select 'smartJacket' database");
	}
	$results1 = mysql_query($query1);

	$a= json_decode($_GET['eventlist']); // array(1, 2, 3)

	for ($x = 0; $x <sizeof($a); $x++) 
	{
	$b=explode(":",$a[$x]);
	$event=$b[0];
	$eventDate=$b[2];
	//$eventDate='2015-02-01';
	$eventPriority=$b[1];
	
	//echo eventDate;
	$eventDate1=explode(" ",$eventDate);
	$day=$eventDate1[0];
	$month=$eventDate1[1];
	$date=$eventDate1[2];
	$year=$eventDate1[3];
	
	//echo $month;
	
	switch ($month) {
    case "Jan":
       $m='01';
        break;
    case 'Feb':
        $m='02';
        break;
    case 'Mar':
        $m='03';
        break;
	case "Apr":
       $m='04';
        break;
    case 'May':
        $m='05';
        break;
    case 'Jun':
        $m='06';
        break;
	case "Jul":
       $m='07';
        break;
    case 'Aug':
        $m='08';
        break;
    case 'Sep':
        $m='09';
        break;
	case "Oct":
       $m='10';
        break;
    case 'Nov':
        $m='11';
        break;
    case 'Dec':
        $m='12';
        break;
    }
	
	if($eventPriority==1)
	{
		$value=10;
		}
	else if($eventPriority==2)
	{
		$value=5;
	}
	else if($eventPriority==3)
	{
		$value=1;
	}
	$dataarray=array($year,$m,$date);
	$actualDate=implode("-",$dataarray);
	
	
	//echo $actualDate;
	
	
	/*if(!isset($grd))
	{
		die("I was expecting a grade to be input");
	}
	*/
	
	//$query = "SELECT * FROM calendar_raw;";
	

//$query = "INSERT INTO calendar_raw (auto_id,event, eventDate, priority)
//VALUES ('','presentation', '2015-01-21', '2')";
//$query="INSERT INTO 'calendar_raw(`auto_id`, `event`, `eventDate`, `priority`) VALUES ('','$event','$eventDate','$eventPriority')";

//$query="INSERT INTO `calendar_raw`(`auto_id`, `event`, `eventDate`, `priority`) VALUES ('','$event','$actualDate','$eventPriority')";
$query="INSERT INTO `calendar_raw`(`event`, `eventDate`, `priority`,`value`) VALUES ('$event','$actualDate','$eventPriority','$value')";

	
	
	$results = mysql_query($query);
		
		if(!$results)
	{
		die(mysql_error());
	}
	
	}
	
	$query3="DELETE FROM `calendar_processed` WHERE 1";
	
	//$query4="INSERT INTO calendar_processed(`eventDate`,`eventPriority`) SELECT eventDate,SUM(value) FROM `calendar_raw` GROUP BY eventDate";
	$query4="INSERT INTO calendar_processed(`eventDate`,`eventPriority`) SELECT eventDate,SUM(value) FROM `calendar_raw` GROUP BY eventDate";
	
	$query5 = "SELECT `eventDate`, `eventPriority` FROM `calendar_processed` WHERE 1";
	
	
	$results3 = mysql_query($query3);
	$result4=mysql_query($query4);
		
	$result5=mysql_query($query5);	
	

	while($row = mysql_fetch_array($result5,MYSQL_ASSOC))
	{
		$val=$row['eventPriority'];
		$evDate=$row['eventDate'];
	//	echo "<ol>";
		if($val>15)
		{
					//echo "high";
			$level="highcal";
		}
		else
		{
		$level="lowcal";
		}
		
		$query1="UPDATE `calendar_processed` SET `level`='$level' WHERE `eventDate`='$evDate'";
		$results1 = mysql_query($query1);
			
	}
	
mysql_close($conn);


?>