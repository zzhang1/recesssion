<!DOCTYPE html>
<html>
<head>
	<link href="style/accordion2.css" rel="stylesheet">
	<title>Are we in a recession?</title>
	<meta content="width=device-width, initial-scale=1" name="viewport">
	<meta name="theme-color" content="#934449">
	<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
</head>
<body>
	<div class="container">
		<h1 class="heading-primary">Are we in a recession?</h1><br>
		<div class="accordion">
			<dl>
				<dt>
					<a aria-controls="v001" aria-expanded="true" class="accordion-title accordionTitle" href="#v001">What does the CFNAI Say?</a>
				</dt>
				<dd aria-hidden="false" class="accordion-content accordionItem" id="accordion1">
					<p>
						<?php include 'results/v001.txt'; ?>
						<br>
						<img class="responsive-image" src="results/v001.svg">
					</p>
				</dd>
				<dt>
					<a aria-controls="v002" aria-expanded="false" class="accordion-title accordionTitle js-accordionTrigger" href="#v002">How close are we to a recession?</a>
				</dt>
				<dd aria-hidden="true" class="accordion-content accordionItem is-collapsed" id="accordion2">
				<p>Using a basic logistic regression on the same indicator and its underlying components, we can estimate a probability of currently being in a recession. Using that: 
<?php include 'results/v002.txt' ?>
<br>

						<img class="responsive-image" src="results/v002.svg">

</p>
				</dd>
			</dl>
		</div>
		<?php include 'results/timestamp2.txt'; ?>
	</div>

	<script src="style/accordion2.js" type="text/javascript"></script>
</body>
</html>
