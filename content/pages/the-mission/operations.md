Title: Operations
Save_as: operations.html

[TOC]

## Launch and orbit

TESS launched successfully on April 18, 2018 from Cape Canaveral Air Force Station aboard a SpaceX Falcon 9 rocket.

The Falcon 9 is a 2 stage, liquid oxygen and kerosene fueled rocket. The first stage is reusable and has 9 Merlin 1D engines, the second stage has a single Merlin engine. The system is designed for safe and efficient transport of satellites, cargo, and eventually crew, to low-earth orbit. TESS is the first NASA Astrophysics satellite mission to be launched under a contract with SpaceX. 

TESS observes from a unique elliptical high Earth orbit (HEO) that provides an unobstructed view of its field to obtain continuous light curves and a more stable platform for precise photometry than the low Earth orbit. The launch carried the observatory to parking orbit inclined by 28.5 degrees. The high Earth orbit was achieved through a series of propulsion system burns and a lunar flyby. Two burns raised the orbit apogee to 400,000 km, one at perigee of the first phasing orbit and another at perigee of the second phasing orbit. Another small adjustment was made before a lunar gravitational assist raised the ecliptic inclination to ~40 degrees. The final apogee and ~13.7 day orbital period were achieved through a final period-adjustment maneuver after the lunar flyby. Final orbit was achieved around 60 days after launch and regular science operations began July 25, 2018.

<br/>
<img class="img-responsive" style="max-width:75%;" src="images/mission/tess_orbit_Winnpresentation.jpg">
* Schematic of maneuvers and encounters leading to the final TESS orbit (light blue). The observatory orbits with a period of ~13.7 days in a 2:1 resonance with the Moon. PLEA and PLEP are the post-lunar-encounter-apogee and -perigee, respectively. Image Credit: Ricker et al. (2015)*
<br/>

The final orbit is elliptical with a period of ~13.7 days and nominal perigee and apogee of 17 Earth radii and 59 Earth radii, respectively. The exact orbital period varies between 12-15 days. The orbit places the spacecraft in a 2:1 resonance with the Moon and is inclined with respect to the Ecliptic plane. This avoids lengthy eclipses of the Earth and Moon through the FOV. The large apogee and perigee keep the spacecraft above the Earth's radiation belts and provide a nearly constant thermal environment for the stable -75 degrees C operation of the CCDs. The orbit is operationally stable due to the Moon leading or lagging the apogee by about 90 degrees, effectively averaging out lunar perturbations. The period and semi-major axis are relatively stable, with long term inclination and eccentricity exchanges over periods of 8-12 years. There are additional short term perturbations caused by the Sun with a period of 6 months. The TESS high Earth orbit is stable for decades or longer and requires no propulsion for station-keeping. 

At the  TESS  orbit perigee (varies between 12-20 Earth radii), science operations are interrupted for no more than 16 h to point TESS's antenna toward Earth, downlink data, and resume observing. This timeframe includes the nominal 4-h period for Ka-band science data downlink using NASA's Deep Space Network (DSN). TESS will also use its hydrazine thrusters to unload angular momentum built up from solar photon pressure at perigee and throughout the orbit.


## Field of view

TESS is equipped with four CCD cameras that have adjacent field-of-views to produce a 4 x 1 array, or 'observing sector', yielding a combined field-of-view of 96 x 24 degrees.

*The pointings for Sectors 14-16 were shifted toward the North ecliptic pole to minimize impacts of scattered light from the Earth and Moon. See the [technical details page](observing-technical.html) for additional information.*

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_observingsectorschematic_Winnpresentation.jpg">
<br/>

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_cameraFOVschematic_Winnpresentation.png">
<br/>


## Time sampling

Over its 2-year prime mission, TESS will collect brightness measurements of about 200,000 preselected stars ('postage stamps') every 2 minutes, and Full Frame Images (FFIs) (all pixels) at 30 minute cadence. The TESS cameras have an exposure time of 2 seconds, and the images are stacked for each 2 or 30 minute cadence onboard the spacecraft before they are compressed and stored in the solid state recorder. Each sector is observed for two orbits, each of which produces over 10k postage stamps and over 600 FFIs.

In the extended mission TESS is changing the FFIs cadence to 10 minutes and adding a new 20 second cadence mode. 

<br/>
<img class="img-responsive" style="max-width:95%;" src="images/mission/tess_onboard_formats.png">
<br/>
*Schematic of TESS time sampling, data processing, and storage.*

## Observing strategy

By the end of the primary mission, TESS will have surveyed over 75% of the sky by observing [26 individual sectors in its 2-year prime mission](status.html), 13 in the southern hemisphere and 13 in the northern hemisphere during the primary mission. Each hemisphere was observed for 1 year each in the 2-year prime mission, beginning in the south in July 2018. Each sector was observed for two orbits (27.4 days total), and once complete, TESS will re-orient to the next sector moving eastward until the hemisphere has been tiled by 13 sectors. 

Within each 96 x 24 degree sector TESS will observe 15,000 target stars on a 2 minute cadence and collect full frame images at 30 minute cadence. The sectors have ecliptic latitudes from 6 degrees to the ecliptic pole with increasing overlap at higher latitudes. There will be over 350 days of continuous coverage in the Continuous Viewing Zone (CVZ) at the ecliptic poles, which corresponds to the region accessible to NASA's upcoming James Webb Space Telescope.

In the extended mission TESS will target fields in the North, South, and in the Ecliptic Plane. Postage stamp targets will be collected at 20 second and two minute cadence, while the FFI cadence will be 10 minutes.

A video illustrating the TESS survey strategy, along with the pathway to the spacecraft orbit, can be seen [here](http://www.youtube.com/watch?v=mpViVEO-ymc).



<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_2yearskycoverage.png">
<br/>
*Schematic showing observing baselines on the celestial sphere including sector overlap regions. The dashed black circle enclosing the Ecliptic pole shows the region where the JWST has continuous viewing capabilities.* *The pointings for Sectors 14--16 were shifted toward the North ecliptic pole by 31 degrees to minimize impacts of scattered light from the Earth and Moon. See the [technical details page](observing-technical.html) for additional information.*


## Commissioning

The commissioning period for TESS was separated into multiple phases that included spacecraft initialization, instrument initialization, fine pointing updates, and instrument calibration. Commissioning was successfully completed, and science operations began on July 25, 2018.

## Science data flow 
The flow of data from the spacecraft to its final archive involves participation from multiple institutions that make up the TESS project team, as described below.

<br/>
<img class="img-responsive" style="max-width:75%;" src="images/mission/tess_operations2.png">
<br/>

Data from the TESS spacecraft are downloaded through the Deep Space Network (DSN) and delivered to the Payload Operations Center (POC) at the Massachusetts Institute ofTechnology (MIT). The POC sends uncalibrated requantized pixel data, target lists, spacecraft configuration and engineering data, and focal plane characterization models (for calibration) to the Science Processing Operations Center (SPOC) at NASA Ames. The SPOC calibrates the science data in two steps, first by the orbit and then by the sector. The SPOC uses instrument calibration models provided by the POC to calibrate all science data. Once a full sector is calibrated the transiting planet search software is run by the SPOC to identify and flag threshold crossing events (TCEs). Calibrated target pixels and FFIs, light curves generated from 2-min cadence targets, and TCEs are sent to the TESS Science Office (TSO, which includes MIT and the Smithsonian Astrophysical Observatory, SAO). The TSO is responsible for detailed analysis of TCEs and the identification of TESS Objects of Interest (TOIs). The TSO will deliver lists of TOIs to the Mikulski Archive for Space Telescopes (MAST, located at the Space Telescope Science Institute, STScI) along with dispositions and information documenting the vetting process for each TOI on a regular schedule, nominally every four months. The processed data and meta-data from the SPOC are archived at MAST. MAST is the primary science data archive for TESS and provides tools to search and retrieve data. The TESS Science Support Center operates the Guest Investigator (GI) Program, which supplies a list of GI targets to the POC, and the GI proposers may retrieve their data from the MAST. All data archived at MAST has no proprietary period and is publicly available.


## Science data processing 

The TESS data processing pipeline was developed by the Science Processing Operations Center (SPOC) at NASA Ames Research Center and builds on the legacy of the Kepler data processing pipeline. A brief overview is presented below, and more details can be found in the SPOC paper available in the [documentation](documentation.html) page.

The SPOC receives raw data via the Payload Operations Center (POC) at MIT. The SPOC pipeline processes the raw pixels, extracts photometry and astrometry for each target star, identifies and removes systematic errors, flags transiting planet signatures, and performs a suite of diagnostic tests. Many software modules developed for Kepler have significant overlap with what is needed to process TESS data. 

One of the primary differences between TESS and Kepler pipeline processing is the volume of data that TESS will produce over the course of the 2 year nominal mission. TESS science data have a nominal cadence of 2 min compared to 29.4 min for Kepler. The Full Frame Images (FFIs), which are calibrated by the SPOC, are collected at 30 min cadence compared to Kepler's monthly FFIs. Furthermore, there is a faster turn-around time for processing the science data, a higher on-board storage capacity for TESS (192 GB vs. 17 GB), and a much higher data rate since TESS' orbit is closer to Earth. All of these factors introduce new challenges to pipeline processing, which (like Kepler) are processed on the NASA Advanced Supercomputing (NAS) Division's Pleiades supercomputer.

### Pipeline products

The SPOC pipeline products include:

* Target Pixel files (raw and calibrated pixel data)
* Target Light Curve files (photometric analysis and systematic error-corrected time series data)
* FFI files (raw, calibrated, and uncertainty images of the CCDs)
* Collateral Pixel files (raw and calibrated collateral pixel data)
* Data validation products
* Ancillary files that include pipeline meta-data and co-trending basis vectors (CBVs)

SPOC products are archived at the Mikulski Archive for Space Telescopes (MAST). There is no proprietary data period for any TESS data products. Further information on the data products can be found on the [data access](data-access.html) page.


