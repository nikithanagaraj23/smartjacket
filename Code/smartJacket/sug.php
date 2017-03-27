<?php
//if (isset($_POST['txt']) && isset($_POST['filename']))
if (isset($_GET['txt']))
{
	$text=htmlentities($_GET['txt']);
	$filename='suggest1.ogg';
	
	$querystring = http_build_query(array(
		"text" => $text
	));
	
	//for wav file format use http://speechutil.com/convert/wav? below
	if ($soundfile = file_get_contents("http://speechutil.com/convert/ogg?".$querystring))
	{
		file_put_contents($filename,$soundfile);
		echo ('
			<audio autoplay="autoplay" controls="controls" style="display:none">
			<source src="'.$filename.'" type="audio/ogg" />
			</audio>
			'
		);
	}
	else echo("<br />Audio could not be saved");

}
?>
