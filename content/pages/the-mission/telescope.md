Title: Characteristics of the TESS space telescope
Save_as: the-tess-space-telescope.html

[TOC]

The TESS observatory consists of the spacecraft and the instrument. The TESS observatory has a single instrument, a camera suite composed of 4 wide field optical cameras and their associated hoods, mount, sun shield, and Data Handling Unit (ADHU). The spacecraft refers to the subset of the observatory that does not include the Instrument. The spacecraft provides power via two deployable solar arrays. 

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess-mit_image.jpg">
<br/>
*Artist’s conception of the  TESS  spacecraft and payload. Image Credit: MIT*


## TESS cameras

TESS is equipped with four identical refractive cameras with a combined field-of-view (FOV) of 24x96 degrees, known as an observing sector. Each camera consists of a CCD detector assembly, a lens assembly, and a lens hood. The lens assembly is a custom design housing seven lenses mounted into two separate aluminum barrels that are fastened together. The lens assembly has a 10.5 cm diameter entrance pupil and a focal ratio  f/1.4. All optical elements have antireflection coatings and one element has a long-pass filter coating to enforce a short-wavelength cutoff at 600 nm in the  TESS  bandpass.  

Each camera forms a 24x24 un-vignetted image on the detector in its focal plane. The lens assemblies were designed for consistent image spot size across the field-of-view (FOV) and to produce undersampled images similar to  Kepler. Operating at nominal focus and a flight temperature of -75 degrees C, the 50% ensquared-energy half-width is 15 𝜇m averaged over the FOV. This corresponds to 1 detector pixel or ≈21 arcseconds (≈0.35 arcmin) on sky. Along with an internal stray light baffle, each lens assembly aperture is equipped with a hood to reduce scattered light from the Earth and Moon. 

### CCD detectors

The detector assembly in each camera consists of a focal plane CCD array and associated electronics. Each CCD array contains four back-illuminated MIT/Lincoln Laboratory CCID-80 devices. The deep-depletion, frame-transfer CCDs consist of a 2048 x 2048 imaging array and a 2048 x 2048 frame-store region (for rapid shutterless readout ≈ 4 ms) with 15 x 15 𝜇m pixels. The four CCDs in each array are separated by 2mm and create an effective 4096 x 4096 pixel detector that is operated at -75 degrees C to reduce dark current. The detectors are read out at 625 kHz with <10  e- read noise. The detector electronics consist of two compact double-sided printed circuit boards seated beneath the CCD focal plane. The electronics transmit digitized data over a serial LVDS link to the Data Handling Unit. The four TESS cameras are bolted to a common plate such that their FOV’s are aligned to form a total simultaneous FOV of 24x96 degrees.


An overview of the FOV coverage and observing strategy for the mission can be found in the [Operations](operations.html) page.

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_spacecraft_cameras.jpg">
<br/>
*Image Credit: MIT*

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_lens_assembly.png">
<br/>
*Image Credit: MIT*

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_camera.png">
<br/>
*Image Credit: MIT*



<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_ccd_detector.png">
<br/>
*Image Credit: MIT*

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_camera_multi.png">
<br/>
*Image Credit: MIT*

### Bandpass
TESS will observe a large number of M dwarfs for several reasons. Planets are easier to detect around these small stars (the planets induce larger transit signals). Most nearby stars are M dwarfs. Because M dwarfs are cool and red, the TESS bandpass will be more sensitive to red wavelengths. These considerations led to the choice of a 600 to 1000 nm bandpass. The width of 400 nm was the largest practical choice for the optical design.


<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_bandpass.png">
*The TESS spectral response function (black line), defined as the product of the long- pass filter transmission curve and the detector quantum efficiency curve. Also plotted, for comparison, are the Johnson–Cousins V, R C , and I C filter curves and the Sloan Digital Sky Survey z filter curve. Each of the functions has been scaled to have a maximum value of unity. Image Credit: Ricker et al. (2015)*
<br/>




<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/tess_vs_kepler_bandpass.png">
<br/>
*TESS will monitor a much larger sample of M stars compared to Kepler, thus the bandpass extends further to red wavelengths. Image Credit: Zach Berta-Thompson with data from Sullivan at al. (2015)*


## Spacecraft

The spacecraft is being built by Orbital ATK in Dulles, VA, where the Mission Operations Center (MOC) is located. The spacecraft consists of the Mechanical, Electrical Power, Command & Data Handling, RF Communications, Attitude Control, Flight Software, Hydrazine Propulsion, Thermal Control, and Harness Subsystems. TESS will be based on Orbital ATK’s LEOStar(TM)-2 platform, a  exible, high-performance spacecraft for space and Earth science, remote sensing and other applications. LEOStar-2 can accommodate various instrument interfaces, deliver up to 2 kilowatt orbit average payload power, and support payloads up to 500 kilograms. Performance options include redundancy, propulsion capability, high data rate communications, and high-agility/high-accuracy pointing. TESS will be the eighth LEOStar-2 based spacecraft built for NASA.

<br/>
<img class="img-responsive" style="max-width:67%;" src="images/mission/spacecraft_orbital.png">
<br/>
*Image Credit: Orbital ATK*

Launch Mass: 350 kg (772 lb.)

Solar Arrays: 400 W (EoL) Two wing solar array, fixed and articulating modes

Stabilization: 3-Axis via 4 Hydrazine thrusters, Four wheel fine-pointing ACS

Orbit: 17 Earth-radii perigee, 59 Earth-radii apogee

