Title: Operations
Save_as: operations.html

[TOC]

## Launch and orbit

TESS  is scheduled for launch from the Cape Canaveral Air Force Station aboard a SpaceX Falcon 9. The Falcon 9 is a 2 stage, liquid oxygen and kerosene fueled rocket. The first stage is reusable and has 9 Merlin 1D engines, the second stage has a single Merlin engine. The system is designed for safe and efficient transport of satellites, cargo, and eventually crew, to low-earth orbit. TESS is the first NASA Astrophysics satellite mission to be launched under a contract with SpaceX. The current launch window is no-earlier-than March 20, 2018 and not-later-than June 2018.

TESS will observe from a unique elliptical high earth orbit (HEO) that will provide an unobstructed view of its field to obtain continuous light curves and a more stable platform for precise photometry than the low-Earth orbit. The launch will carry the observatory to parking orbit inclined by 28.5 degrees. The high earth orbit is achieved through a series of propulsion system burns and a lunar flyby. Two burns raise the orbit apogee to 400,000 km, one at perigee of the first phasing orbit and another at perigee of the second phasing orbit. Another small adjustment is made is made a third perigee before a lunar gravitational assist raises the ecliptic inclination to ~40 degrees. The final apogee and 13.7 day orbital period are achieved through a final period-adjustment maneuver after the lunar flyby. Final orbit is achieved around 60 days after launch and science operations begin shortly afterward.

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_orbit_Winnpresentation.jpg">
* Schematic of maneuvers and encounters leading to the final TESS orbit (light blue). The observatory orbits with a period of 13.7 days in a 2:1 resonance with the Moon. PLEA and PLEP are the post-lunar-encounter-apogee and -perigee, respectively. Image Credit: Ricker et al. 2015*
<br/>

The final orbit is elliptical with a period of 13.7 days and nominal perigee and apogee of 17 Earth radii and 59 Earth radii, respectively. The orbit places the spacecraft in a 2:1 resonance with the Moon and is inclined with respect to the Ecliptic plane. This avoids lengthy eclipses of the Earth and Moon through the FOV. The large apogee and perigee keep the spacecraft above the Earth’s radiation belts and provide a nearly constant thermal environment for the stable -75 degrees C operation of the CCDs. The orbit is operationally stable due to the Moon leading or lagging the apogee by about 90 degrees, effectively averaging out lunar perturbations. The period and semi-major axis are relatively stable, with long term inclination and eccentricity exchanges over periods of 8-12 years. There are additional short term perturbations caused by the Sun with a period of 6 months. The TESS high earth orbit is stable for decades or longer and requires no propulsion for station-keeping. TESS data are returned to Earth during each orbital perigee using the Deep Space Network.


## Field of view

TESS is equipped with four CCD cameras that have adjacent field-of-views to produce a 4 x 1 array, or 'observing sector', yielding a combined field-of-view of 96 x 24 degrees

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_observingsectorschematic_Winnpresentation.jpg">
<br/>

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_cameraFOVschematic_Winnpresentation.png">
<br/>


## Time sampling

TESS will collect brightness measurements of about 200,000 preselected stars ('postage stamps') every 2 minutes, and Full Frame Images (FFIs) (all pixels) at 30 minute cadence. The TESS cameras have an exposure time of 2 seconds, and the images are stacked for each 2 or 30 minute cadence onboard the spacecraft before they are compressed before stored in the solid state recorder. Each sector is observed for two orbits, each of which produces over 10k postage stamps and over 600 FFIs.

<br/>
<img class="img-responsive" style="max-width:95%;" src="images/mission/tess_onboard_formats.png">
<br/>
*Schematic of TESS time sampling, data processing, and storage.*

## Observing strategy

TESS will survey over 90% of the sky by observing 26 individual sectors, 13 in the southern hemisphere and 13 in the northern hemispheres. Each hemisphere will be observed for 1 year each in the 2 year prime mission, beginning in the south. Each sector will be observed for two orbits (27.4 days total), once complete TESS will re-orient to the next sector moving eastward until the hemisphere has been tiled by 13 sectors.  

Within each 96 x 24 degree sector TESS will observe 15,000 target stars on a 2 minute cadence and collect full frame images at 30 minute cadence. The sectors have ecliptic latitudes from 6 degrees to the ecliptic pole with increasing overlap at higher latitudes. There will be over 350 days of continuous coverage in the Continuous Viewing Zone (CVZ) at the ecliptic poles, which corresponds to the region accessible to NASA's upcoming James Webb Space Telescope.



<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_2yearskycoverage.png">
<br/>


## Science data flow 
The flow of data from the spacecraft to its final archive involves participation from multiple institutions that make up the TESS project team, as described below.

<br/>
<img class="img-responsive" style="max-width:75%;" src="images/mission/tess_operations2.png">
<br/>

Data from the TESS spacecraft will be downloaded through the Deep Space Network (DSN) and delivered to the Payload Operations Center (POC) at the Massachusetts Institute ofTechnology (MIT). The POC sends uncalibrated requantized pixel data, target lists, spacecraft configuration and engineering data, and focal plane characterization models (for calibration) to the Science Processing Operations Center (SPOC) at NASA Ames. The SPOC calibrates the science data in two steps, first by the orbit and then by the sector. The SPOC uses instrument calibration models provided by the POC to calibrate all science data. Once a full sector is calibrated the transiting planet search software is run by the SPOC to identify and flag threshold crossing events (TCEs). Calibrated target pixels and FFIs, light curves generated from 2-min cadence targets, and TCEs are sent to the TESS Science Office (TSO, which includes MIT and the Smithsonian Astrophysical Observatory, SAO). The TSO is responsible for detailed analysis of TCEs and the identification of TESS Objects of Interest (TOIs). The TSO will deliver lists of TOIs to the Mikulski Archive for Space Telescopes (MAST, located at the Space Telescope Science Institute, STScI) along with dispositions and information documenting the vetting process for each TOI on a regular schedule, nominally every four months. The processed data and meta-data from the SPOC will be archived at MAST. MAST is the primary science data archive for TESS and will provide tools to search and retrieve data. The TESS Science Support Center operates the Guest Investigator (GI) Program, which will supply a list of GI targets to the POC, and the GI proposers will retrieve their data from the MAST. All data archived at MAST will have no proprietary period and will be publicly available.


