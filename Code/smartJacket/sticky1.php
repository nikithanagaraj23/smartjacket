<html>
<head>
<script src="theme/js/jquery.js"></script>

<script>

$(document).ready(function() {
  //alert("hello");
  //$(this).animate({backgroundColor: 'red'}, 'slow');
 //  $("body").css("background-color", 'red' );
   });
  
	function show_suggestions()
	{
		var suggest1=document.getElementById("suggest1").innerHTML;
		//alert(suggest1);
		var suggest2=suggest1.split("<br>").join(",");
		var suggest3=suggest2.split("<p>");
		//document.getElementById("txt").value=suggest3[1];
		var suggestion1=suggest3[0];
		//alert(suggestion1);
		xhr = new XMLHttpRequest();
		xhr.onreadystatechange = updateFields;
		xhr.open("GET","sug.php?txt="+suggestion1,true);
		xhr.send();
	}
	
	function updateFields()
	{
	if(xhr.readyState==4)
	{
	div1=document.getElementById("audio");
	div1.innerHTML=xhr.responseText;
	}
	}

	function show_suggestions_shortterm()
	{
		var suggest1=document.getElementById("suggest_shortterm").innerHTML;
		//alert(suggest1);
		var suggest2=suggest1.split("<br>").join(",");
		var suggest3=suggest2.split("<p>");
		//document.getElementById("txt").value=suggest3[0];
		var suggestion1=suggest3[0];
		//alert(suggestion1);
		xhr1 = new XMLHttpRequest();
		xhr1.onreadystatechange = updateFields1;
		xhr1.open("GET","sug.php?txt="+suggestion1,true);
		xhr1.send();
	}
	
	function updateFields1()
	{
	if(xhr1.readyState==4)
	{
	div1=document.getElementById("audio");
	div1.innerHTML=xhr1.responseText;
	}
	}
	
	function show_suggestions_longterm()
	{
		var suggest1=document.getElementById("suggest_longterm").innerHTML;
		//alert(suggest1);
		var suggest2=suggest1.split("<br>").join(",");
		var suggest3=suggest2.split("<p>");
		//document.getElementById("txt").value=suggest3[0];
		var suggestion1=suggest3[0];
		//alert(suggestion1);
		xhr2 = new XMLHttpRequest();
		xhr2.onreadystatechange = updateFields2;
		xhr2.open("GET","sug.php?txt="+suggestion1,true);
		xhr2.send();
	}
	
	function updateFields2()
	{
	if(xhr2.readyState==4)
	{
	div1=document.getElementById("audio");
	div1.innerHTML=xhr2.responseText;
	}
	}
	

	
	function show_suggestions_cal()
	{
		var suggest1=document.getElementById("suggest_cal").innerHTML;
		//alert(suggest1);
		var suggest2=suggest1.split("<br>").join(",");
		var suggest3=suggest2.split("<p>");
		//document.getElementById("txt").value=suggest3[0];
		var suggestion1=suggest3[0];
		//alert(suggestion1);
		xhr3 = new XMLHttpRequest();
		xhr3.onreadystatechange = updateFields3;
		xhr3.open("GET","sug.php?txt="+suggestion1,true);
		xhr3.send();
	}
	
	function updateFields3()
	{
	if(xhr3.readyState==4)
	{
	div1=document.getElementById("audio");
	div1.innerHTML=xhr3.responseText;
	}
	}
	

	
</script>
<style>

.stickynotes
{
box-shadow: 5px 5px 5px #888888;
padding:10px;
padding-bottom:10px;
font-family:cursive;
font-style:italic;
	}
</style>

</head>


<body style="background-image:url('theme/img/bg2.jpg');background-position: 50% 50%;background-size: cover;  "><!--
<div style="background-image:url('theme/img/bg2.jpg');width:100%;height:100px;">   </div>         
-->

<h2 style="margin-left:11%;padding-top:20px;color:white;font-family:cursive"><a style="color:white;text-decoration:none;" href="../smartJacket/Main.html">smartJacket</a>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Suggestions/Remedies   &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;         <a style="color:white;text-decoration:none;" href="Chart/smartJacket.html">View Your Stress Chart</a></h2>

<div style="padding:20px;border-radius:25px;background: radial-gradient(#CCEDE5,white);margin-left:11%;margin-top:5%;width:1000px;box-shadow: 5px 5px 5px 5px #888888;margin-bottom:100px;">
<h3 style="font-family:cursive;">Play Some Music &nbsp; <audio controls="controls">
<source src="audio/audio.mp3" type="audio/ogg" />
</audio>
<table cellpadding="75" style="width:100%;>">

<?php
	

	
	$query1 = "SELECT value FROM `graph` WHERE 1";
	
	$conn = mysql_connect('127.0.0.1','root','');
	
	$db = mysql_select_db('smartjacket_sensors');
	
	$results1= mysql_query($query1);
	
	
	
	while($row1 = mysql_fetch_array($results1,MYSQL_ASSOC))
	{

	$myArray[]=$row1['value'];

	}
	$s=sizeof($myArray);
	$stress_level=$myArray[$s-1];
	
	$query = "SELECT shortterm,longterm FROM `solutions` WHERE stress_level='$stress_level'";
	$results = mysql_query($query);
	echo "&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Your Current Stress Level:".$stress_level."</h3><tr>
<td>";
	?>
</div>
	<div id="audio"></div>

	<?php
	
	$found = false;
	while($row = mysql_fetch_array($results,MYSQL_ASSOC))
	{
		$found = true;
		
		echo"<div class='stickynotes' id='suggest_shortterm' style='transform: rotate(10deg);background-color:#FFFF00;'>";
		echo "ShortTerm Solutions,,<br>";
		echo ($row['shortterm']);
		echo ' <p><img onclick="show_suggestions_shortterm()" src="img/mike.png" style="cursor: pointer; curwidth:30px;height:30px;">';
		echo "</div></td>";
		
		echo"<td><div class='stickynotes' id='suggest_longterm' style='transform: rotate(-10deg);background-color:#FFFF00;'>";
		echo "LongTerm Solutions.,<br>";
		echo ($row['longterm']);
		echo ' <p><img onclick="show_suggestions_longterm()" src="img/mike.png" style="cursor: pointer; curwidth:30px;height:30px;">';
		echo"</div></td>";
	}
	echo "</tr>";
	
	echo "<br><tr><td>";
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
	echo"<div class='stickynotes' id='suggest1' style='transform: rotate(-10deg);background-color:#FF0000;'>";
	echo("Start earlier to escape peak hour traffic.");
	echo "<br>";
}

$sql = "SELECT answer FROM questionnaire_answer WHERE question_number = 3";
$retval = mysql_query( $sql, $conn );
$ans = mysql_fetch_row($retval);
if($ans[0]<5)
{echo"";
	echo("Switch from caffinated to decaffeinated coffee or herbal tea, Leave work at lunchtime to take a short walk or relax outside your work environment,Take a 5-minute relaxation break – practice a relaxation exercise.
");
	echo "<br>";
}

$sql = "SELECT answer FROM questionnaire_answer WHERE question_number = 7";
$retval = mysql_query( $sql, $conn );
$ans = mysql_fetch_row($retval);
if($ans[0] == "Yes")
{
	echo("Contact human resources to clear the air, Conversation is key to solving every problem\n");
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
	echo("Approach a dietician for stabilising a healthy weight for your age and height,Also eat lots of fruits and vegetables and drink lots of water.");
	echo "<br>";
}

echo '<p><img onclick="show_suggestions_longterm()" src="img/mike1.png" style="cursor: pointer; width:30px;height:30px;">';
	echo"</div></td>";

$sql = "SELECT eventDate FROM calendar_processed WHERE level='highcal'";
$retval = mysql_query( $sql, $conn );

while($row = mysql_fetch_array($retval,MYSQL_ASSOC))
	{
		
		foreach($row as $key=>$value)
		{
			echo"<td><div class='stickynotes' id='suggest_cal' style='transform: rotate(10deg);background-color:#FF0000;'>";
			echo "You have a very busy schedule on this day,";
			echo "$value";
			echo ",,Try and readjust your schedule if possible ,or try and be better prepared for your meetings, in order to boost your confidence.";
			echo '<p><img onclick="show_suggestions_cal()" src="img/mike1.png" style="cursor: pointer; curwidth:30px;height:30px;">';
			echo "</div></td>";
	}
		
	}

//	echo ' <input onclick="show_suggestions()" name="submit" type="submit" value="Convert" /> ';

	
	
	
?>
<tr><td>

<div class='stickynotes' id='suggest1' style='transform: rotate(10deg);background-color:#FFFF00;'>
The Best relaxation technique for you<br>
Do you tend to become angry, agitated, or keyed up? <br>
	You may respond best to relaxation techniques that quiet you down, such as meditation, deep breathing, or guided imagery<br>
Do you tend to become depressed, withdrawn, or spaced out?<br>
	You may respond best to relaxation techniques that are stimulating and that energize your nervous system, such as rhythmic exercise<br>
Do you tend to freeze-speeding up internally, while slowing down externally?<br>
	Your challenge is to identify relaxation techniques that provide both safety and stimulation to help you reboot your system. Techniques such as mindfulness walking or power yoga might work well for you<br>
</div></td>
<td>
<div class='stickynotes' id='suggest1' style='transform: rotate(-10deg);background-color:#FFFF00;'>
Relaxation Technique 1 Visualization meditation<br>
Visualization, or guided imagery, is a variation on traditional meditation that requires you to employ not only your visual sense, but also your sense of taste, touch, smell, and sound. <br>
Find a quiet, relaxed place.<br>
Close your eyes and let your worries drift away. Imagine your restful place. <br>
Picture it as vividly as you can everything you can see, hear, smell, and feel.<br>
When visualizing, choose imagery that appeals to you; dont select images because someone else suggests them, or because you think they should be appealing.
Let your own images come up and work for you<br>

</div>
</td>
</tr>
<tr>
<td>
<div class='stickynotes' id='suggest1' style='transform: rotate(10deg);background-color:#FF0000;'>
Move slowly up through your body, contracting and relaxing the muscle groups as you go.Relaxation Technique 2 Progressive Muscle relaxation <br>
Progressive muscle relaxation involves a two-step process in which you systematically tense and relax different muscle groups in the body.Before practicing Progressive Muscle Relaxation, consult with your doctor if you have a history of muscle spasms, back problems, or other serious injuries that may be aggravated by tensing muscles.<br>
Loosen your clothing, take off your shoes, and get comfortable<br>
Take a few minutes to relax, breathing in and out in slow, deep breaths.<br>
When youre relaxed and ready to start, shift your attention to your right foot. Take a moment to focus on the way it feels.<br>
Slowly tense the muscles in your right foot, squeezing as tightly as you can. Hold for a count of 10.<br>
Relax your right foot. Focus on the tension flowing away and the way your foot feels as it becomes limp and loose.<br>

</div>
</td>
<td>
<div class='stickynotes' id='suggest1' style='transform: rotate(-10deg);background-color:#FF0000;'>
Relaxation technique 3  Breathing Meditation<br>
With its focus on full, cleansing breaths, deep breathing is a simple, yet powerful, relaxation technique. Its easy to learn, can be practiced almost anywhere, and provides a quick way to get your stress levels in check.<br>
Sit comfortably with your back straight. Put one hand on your chest and the other on your stomach.<br>
Breathe in through your nose. The hand on your stomach should rise. The hand on your chest should move very little.<br>
Exhale through your mouth, pushing out as much air as you can while contracting your abdominal muscles. The hand on your stomach should move in as you exhale, but your other hand should move very little.<br>
Continue to breathe in through your nose and out through your mouth. Try to inhale enough so that your lower abdomen rises and falls. Count slowly as you exhale.<br>

</div>
</td>

</div>
</table>
</body>