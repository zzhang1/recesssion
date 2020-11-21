<!DOCTYPE html>
<html>
<head>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-165280565-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-165280565-1');
</script>



        <link href="style/accordion2.css" rel="stylesheet">
        <title>Are we in a recession?</title>
        <meta content="width=device-width, initial-scale=1" name="viewport">
        <meta name="theme-color" content="#fab407">
        <meta name="apple-mobile-web-app-status-bar-style" content="#fab407">
</head>
<body>
        <div class="container">
	<h1 class="heading-primary"><?php include 'results/combined_result.txt';?></h1><br>
                <div class="accordion">
                        <dl>
                                <dt>
                                        <a aria-controls="v001" aria-expanded="false" class="accordion-title accordionTitle js-accordionTrigger" href="#v001">What does the CFNAI say?</a>
                                </dt>
                                <dd aria-hidden="true" class="accordion-content accordionItem is-collapsed" id="v001">
					
<p>
Are we in a recession? "We" in this case only refers to the United States, because data is easy to get. While there are many definitions for what constitutes a recession, the <a href=https://www.chicagofed.org/publications/cfnai/index>Chicago Federal Reserve Bank National Activity Index (CFNAI)</a> is a good monthly indicator, which represents current economic activity, where past recessions periods have coincided with its three-month moving average falling below -0.7.
</p>
<p>
                                                Using this moving average, we see: <?php include 'results/v001.txt'; ?>
                                                </p>
                                                <img class="responsive-image" src="results/v001.svg">
                                        
                                </dd>

                                <dt>
                                        <a aria-controls="v002" aria-expanded="false" class="accordion-title accordionTitle js-accordionTrigger" href="#v002">How close are we to a recession?</a>
                                </dt>
                                <dd aria-hidden="true" class="accordion-content accordionItem is-collapsed" id="v002">
                                	<p>Using a basic logistic regression on the monthly CFNAI indicator's underlying components (85 factors rolling up into production/income, consumption/housing, employment, and sales), we can estimate a probability of currently being in a recession. </p><p>Using that: 
									<?php include 'results/v002.txt' ?>
				</p>

                                        <img class="responsive-image" src="results/v002.svg">
                                </dd>

                                <dt>
                                        <a aria-controls="v003" aria-expanded="false" class="accordion-title accordionTitle js-accordionTrigger" href="#v003">What about past trends?</a>
                                </dt>
                                <dd aria-hidden="true" class="accordion-content accordionItem is-collapsed" id="v003">
					<p>Adding time lags to independent variables as far as 12 months ago, we can attempt to capture some trends instead of just deciding from today's values.
</p><p>This shows: 
									<?php include 'results/v003.txt' ?>
</p>
                                        <img class="responsive-image" src="results/v003.svg">
                                </dd>

                                <dt>
                                        <a aria-controls="v004" aria-expanded="false" class="accordion-title accordionTitle js-accordionTrigger" href="#v004">How likely is a future recession?</a>
                                </dt>
                                <dd aria-hidden="true" class="accordion-content accordionItem is-collapsed" id="v004">
					<p>While we can't predict the future, we know what the events leading up to past recessions looked like. By adding a forward lag to past recession periods, we can try to estimate the probability of a recession happening at any point in the next 12 months. 
</p><p>Result: 
									<?php include 'results/v004.txt' ?>
</p>
                                        <img class="responsive-image" src="results/v004.svg">
                                </dd>
                        </dl>
		</div>
Data source: Federal Reserve Bank of Chicago, Chicago Fed National Activity Index [CFNAI], retrieved from FRED, Federal Reserve Bank of St. Louis.<br>
                <?php include 'results/timestamp2.txt'; ?>
        </div>

        <script src="style/accordion2.js" type="text/javascript"></script>
</body>
</html>
