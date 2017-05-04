Title: Observing Technical Details
Save_as: observing-technical.html

[TOC]

The TESS mission provides the community with an opportunity to make ground-breaking discoveries in the field of exoplanets, astrophysics and planetary science. A
description of the mission concept can be found in
[Ricker et al. 2014](http://adsabs.harvard.edu/abs/2015JATIS...1a4003R) and the [TESS Observatory Guide](link-to-guidebook.something). 

## Overview

The Kepler spacecraft hosts a 0.95-m aperture Schmidt telescope in an
Earth-trailing heliocentric orbit, which insures a thermally stable environment and provides the ability to remain on a single pointing for the
duration of each Campaign. 
Pointing is maintained by a combination of two reaction wheels and thrusters, 
reacting to motion data provided by fine guidance sensors 
(fine-point observing) or star trackers (coarse-point observing). 

With only two remaining reaction wheels, 
these operations are only possible while pointing within 
the orbital plane of the spacecraft, which approximates to the ecliptic. 
Only this specific family of pointings yields operational configurations 
where solar pressure is largely mitigated by spacecraft geometry, 
thereby making viable precision pointing and photometry 
approaching the quality achieved for the Kepler mission. 

### Capabilities

Science observations are taken at one of two timing settings: long (30-min) or short (1-min) cadence. When in fine-point observing, [K2 is capable of achieving a benchmark photometric precision](k2-observing.html#fine-point-photometric-precision) on an m<sub>V</sub> = 12 G2V star of better than 170 parts-per-million (ppm) in 30 minutes of integration, i.e., one long cadence exposure. 
This corresponds to ~30 ppm over a 6.5-hour transit 
of an Earth-sized body around that star.

While stars brighter than m<sub>V</sub> = 11.5 will saturate some pixels, 
K2 performs well on stars as bright as m<sub>V</sub> = 4, 
provided the scientific benefit justifies the large number of pixels 
needed to capture saturated flux bleeding along CCD columns. 
Kepler also has many faint-target scientific applications 
where m<sub>V</sub> = 20 objects yield a photometric precision 
of 10% over 30 minutes.

The broad photometric bandpass has a half-maximum transmission range 
of 430 to 840 nm. 
The instrument has neither changeable filters, 
dispersing elements, nor a shutter. 
The detector has a pixel scale of 3.98 arcseconds. 
Image quality varies with position in the focal plane, 
with the 95% encircled energy diameter ranging from 3.1 to 7.5 pixels with a median value of 4.2 pixels. 
The percentage of point-source flux concentrated in the center pixel 
is between 20% and 62% with a median value of 45%.

### Sectors

K2 observations entail a series of sequential observing
["Campaigns"](k2-fields.html) of fields distributed around the
ecliptic plane. Each ecliptic Campaign is limited by Sun angle
constraints to a duration of approximately 80 days as illustrated in
the image below ([Howell et al. 2014](http://adsabs.harvard.edu/abs/2014PASP..126..398H)). 
Therefore, four to five K2 Campaigns can be performed 
during each 372-day orbit of the spacecraft.

<a href="http://www.nasa.gov/kepler/keplers-second-light-how-k2-will-work"><img class="img-responsive" style="max-width:90%;" src="images/k2_explained_25nov_story.jpg"></a>
*Image Credit: NASA Ames/W. Stenzel*

<br/>

K2 is a community-driven mission. All K2 targets are proposed by the community through the
[Guest Observer program](k2-proposing-targets.html). The K2 mission
welcomes all proposals including, but not exclusive to, exoplanet,
stellar, extragalactic and solar system science.  Since K2 offers a photometric precision [approaching that of the original Kepler mission](k2-observing.html#fine-point-photometric-precision), a variety of scientific goals can be readily
achieved with K2's continuous, high-precision photometry of fields
that span different parts of the galaxy (as illustrated in the image
below).

<br/>

<img class="img-responsive" style="max-width:75%;" src="images/k2_graphic_sm.jpeg">
*Image Credit: NASA Ames/W. Stenzel*

<br/>

### Data yield

Constraints imposed by onboard storage and communications 
dictate that at most 6% of the data from the full focal plane 
are saved and downloaded. 
Instead, data for specific, predetermined targets are saved 
and transmitted as subimages with a typical area of 160 pixels, 
depending on source brightness. 
The brighter a target, the more pixels required to capture it. 
Pixel apertures can be tailored further to accommodate 
extended or very bright, saturated objects. The Kepler Science Center derives pixel masks for those targets 
successfully justified by proposers and uploads these targets 
to the spacecraft before each Campaign. 

It is expected that on the order of 10,000 to 20,000 long cadence targets and 50 to 100 short cadence targets will be available per Campaign.  The number of observed targets in each Campaign varies based on the density of the field and on how many extended or bright objects are observed.  Such objects require larger aperture sizes and decrease the total number of targets available.  These targets must be justified carefully.

Data distribution and archival services are performed 
by the Space Telescope Science Institute’s 
<a href="https://archive.stsci.edu/k2">MAST archive</a>. 
Final data products available to observers 
include original and calibrated pixel values 
and light curves for each individual target (starting in Campaign 3). 
The calibration corrects for bias level, smear, galactic cosmic rays, 
flat fielding, dark current, background, and instrument noise. 
Simple aperture photometry is used to generate long cadence light curves (starting in Campaign 3). 

Data is delivered in Flexible Image Transport System (FITS) format. 
A thorough understanding of the noise sources and systematic errors of K2 
is needed by observers in order to generate their own light curves 
from the original (uncalibrated or calibrated) pixel data 
or interpret structure found in archived light curves.

There is no exclusive use period associated with any K2 data.

A comprehensive list of data products for K2 is given
[here](data-products.html#k2-product-overview).



## Photometric performance



### Typical noise levels





### Solar pressure-induced drift




### Fine-point pointing precision


### Point-spread function


## TESS Input Catalog


### Candidate Target List



## Learn more

<ul>
  <li>
    <a href="k2-fields.html">Campaign fields &raquo;</a>
  </li>
    <li>
    <a href="k2-proposing-targets.html">Proposing targets &raquo;</a>
  </li>
  <li>
    <a href="k2-approved-programs.html">Approved observing programs &raquo;</a>
  </li>
</ul>
