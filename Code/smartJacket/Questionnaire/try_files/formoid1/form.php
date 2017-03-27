<?php

define('EMAIL_FOR_REPORTS', '');
define('RECAPTCHA_PRIVATE_KEY', '@privatekey@');
define('FINISH_URI', 'http://');
define('FINISH_ACTION', 'message');
define('FINISH_MESSAGE', 'Thanks for filling out my form!');
define('UPLOAD_ALLOWED_FILE_TYPES', 'doc, docx, xls, csv, txt, rtf, html, zip, jpg, jpeg, png, gif');

define('_DIR_', str_replace('\\', '/', dirname(__FILE__)) . '/');
require_once _DIR_ . '/handler.php';

?>

<?php if (frmd_message()): ?>
<link rel="stylesheet" href="<?php echo dirname($form_path); ?>/formoid-solid-green.css" type="text/css" />
<span class="alert alert-success"><?php echo FINISH_MESSAGE; ?></span>
<?php else: ?>
<!-- Start Formoid form-->
<link rel="stylesheet" href="<?php echo dirname($form_path); ?>/formoid-solid-green.css" type="text/css" />
<script type="text/javascript" src="<?php echo dirname($form_path); ?>/jquery.min.js"></script>
<form class="formoid-solid-green" style="background-color:#1A2223;font-size:14px;font-family:'Roboto',Arial,Helvetica,sans-serif;color:#4aa1aa;max-width:480px;min-width:150px" method="post"><div class="title"><h2>smartJacket</h2></div>
	<div class="element-radio<?php frmd_add_class("radio"); ?>"><label class="title">1.	Did you loose any loved ones in the recent past?

</label>		<div class="column column1"><label><input type="radio" name="radio" value="Yes" /><span>Yes</span></label><label><input type="radio" name="radio" value="No" /><span>No</span></label></div><span class="clearfix"></span>
</div>
	<div class="element-radio<?php frmd_add_class("radio1"); ?>"><label class="title">2.Are you having any financial crisis?</label>		<div class="column column1"><label><input type="radio" name="radio1" value="Yes" /><span>Yes</span></label><label><input type="radio" name="radio1" value="No" /><span>No</span></label></div><span class="clearfix"></span>
</div>
	<div class="element-radio<?php frmd_add_class("radio2"); ?>"><label class="title">3.Are you unhappy with the job/job culture at work?</label>		<div class="column column1"><label><input type="radio" name="radio2" value="Yes" /><span>Yes</span></label><label><input type="radio" name="radio2" value="No" /><span>No</span></label></div><span class="clearfix"></span>
</div>
	<div class="element-radio<?php frmd_add_class("radio3"); ?>"><label class="title">4.	Did you have any childhood trauma?(difficult emotional experience as a child)</label>		<div class="column column1"><label><input type="radio" name="radio3" value="Yes" /><span>Yes</span></label><label><input type="radio" name="radio3" value="No" /><span>No</span></label></div><span class="clearfix"></span>
</div>
<div class="submit"><input type="submit" value="Submit"/></div></form><script type="text/javascript" src="<?php echo dirname($form_path); ?>/formoid-solid-green.js"></script>

<!-- Stop Formoid form-->
<?php endif; ?>

<?php frmd_end_form(); ?>