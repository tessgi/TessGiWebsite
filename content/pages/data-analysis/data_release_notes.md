Title: TESS Data Release Notes
Save_as: data_release_notes.html

[TOC]

As the TESS mission has evolved, so has the processing and delivery of its data. Whilst a [data release note (DRL)](https://archive.stsci.edu/tess/tess_drn.html) is provided for every sector of the mission, this page hi-lights important changes that might affect you, the user, and your handling/understanding of the data.

##Key updates
Below we outline some of the most important issues or data product modifications. For more details please see the Sector tables provided below, and the DRNs listed within.

- [**Sector 32:**](http://localhost:8000/data_release_notes.html#sector-32) Star tracker anomaly between  2020-11-16 10:37 UTC  &  2020-11-20-17-13-00 UTC.<p></p>
- [**Sector 31:**](http://localhost:8000/data_release_notes.html#sector-31)  Star tracker anomaly between  2020-11-16 10:37 UTC &  2020-11-20, at the beginning of Sector 32.<p></p>
- [**Sector 30:**](http://localhost:8000/data_release_notes.html#sector-30) As of Sector 30, co-trending basis vector (CBV) files only include the first eight principal components for the Single Scale co-trending mode. <p></p>
- [**Sector 27:**](http://localhost:8000/data_release_notes.html#sector-27) This is the first data release for the extended mission. Key changes have occurred including the collection of 10 min FFI data instead of 30 min, and 20 second target pixel files. <p></p>
	Additionally, the pixel level uncertainties have been over estimated since Sector 5, after the 2D block model was updated. <p></p>
	For targets observed in both Year 1 and Year 3, Year 3 processing was done using TIC 8.1 while TIC 7 was used for Year 1 processing; this may result in differences in results for certain targets. <p></p>
- [**Sector 26:**](http://localhost:8000/data_release_notes.html#sector-26) The TESS spacecraft configuration file was updated from version ‘0187’ to ‘0188’ between orbit 59 and 60. <p></p>
- [**Sector 22:**](http://localhost:8000/data_release_notes.html#sector-22) There were three "watchdog resets" (2/29/20, 3/3/20, 3/12/20), where the instrument computer unexpectedly hung resulting in a quick reboot. These resets resulted in the loss a total of four FFI cadences. 
Two 2-minute cadences are missing from, TJD 1909.46004 to 1909.4642 (2/29/20),  TJD 1911.9267 to 1911.9309 (3/3/20), and TJD 1921.0560 to 1921.0602 (3/12/20).<p></p>
	<p>There were also several corrections to data product timestamps</p>
- [**Sector 21:**](http://localhost:8000/data_release_notes.html#sector-21) The FFI timestamps have been adjusted for the 0.5 second staggered readouts of the four cameras and the 0.02 second staggered readouts for individual CCDs within a camera. 

##Quick look mission information

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:20%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">Year</th>
       <th style="vertical-align: middle;">Hemisphere</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Sectors</th>
       <th style="vertical-align: middle;">Mission</th>
       </tr>
       </thead>

 	<tr>  
       <td>1</td>
       <td>Southern</td> 
       <td>07/25/18 - 07/18/19</td>
       <td><a href ="https://tess.mit.edu/observations/sector-1/">1</a>, 
       <a href ="https://tess.mit.edu/observations/sector-2/">2</a>,
       <a href ="https://tess.mit.edu/observations/sector-3/">3</a>,
       <a href ="https://tess.mit.edu/observations/sector-4/">4</a>,
       <a href ="https://tess.mit.edu/observations/sector-5/">5</a>,
       <a href ="https://tess.mit.edu/observations/sector-6/">6</a>,
       <a href ="https://tess.mit.edu/observations/sector-7/">7</a>,
       <a href ="https://tess.mit.edu/observations/sector-8/">8</a>,
       <a href ="https://tess.mit.edu/observations/sector-9/">9</a>,
       <a href ="https://tess.mit.edu/observations/sector-10/">10</a>,
       <a href ="https://tess.mit.edu/observations/sector-11/">11</a>,
       <a href ="https://tess.mit.edu/observations/sector-12/">12</a>,
       <a href ="https://tess.mit.edu/observations/sector-13/">13</a>
       </td>
       <td><a href ="https://heasarc.gsfc.nasa.gov/docs/tess/primary.html">Prime</a></td>
       </tr>
       
       
        	<tr>  
       <td>2</td>
       <td>Northern</td> 
       <td>07/18/19 - 07/04/20</td>
       <td><a href ="https://tess.mit.edu/observations/sector-14/">14</a>, 
       <a href ="https://tess.mit.edu/observations/sector-15/">15</a>,
       <a href ="https://tess.mit.edu/observations/sector-16/">16</a>,
       <a href ="https://tess.mit.edu/observations/sector-17/">17</a>,
       <a href ="https://tess.mit.edu/observations/sector-18/">18</a>,
       <a href ="https://tess.mit.edu/observations/sector-19/">19</a>,
       <a href ="https://tess.mit.edu/observations/sector-20/">20</a>,
       <a href ="https://tess.mit.edu/observations/sector-21/">21</a>,
       <a href ="https://tess.mit.edu/observations/sector-22/">22</a>,
       <a href ="https://tess.mit.edu/observations/sector-23/">23</a>,
       <a href ="https://tess.mit.edu/observations/sector-24/">24</a>,
       <a href ="https://tess.mit.edu/observations/sector-25/">25</a>,
       <a href ="https://tess.mit.edu/observations/sector-26/">26</a>
       </td>
       <td><a href ="https://heasarc.gsfc.nasa.gov/docs/tess/primary.html">Prime</a></td>
       </tr>
       
        <tr>  
       <td>3</td>
       <td>Southern</td> 
       <td>07/04/20 - 06/24/21</td>
       <td><a href ="https://tess.mit.edu/observations/sector-27/">27</a>, 
       <a href ="https://tess.mit.edu/observations/sector-28/">28</a>,
       <a href ="https://tess.mit.edu/observations/sector-29/">29</a>,
       <a href ="https://tess.mit.edu/observations/sector-30/">20</a>,
       <a href ="https://tess.mit.edu/observations/sector-31/">31</a>,
       <a href ="https://tess.mit.edu/observations/sector-32/">32</a>,
       <a href ="https://tess.mit.edu/observations/sector-33/">33</a>,
       <a href ="https://tess.mit.edu/observations/sector-34/">34</a>,
       <a href ="https://tess.mit.edu/observations/sector-35/">35</a>,
       <a href ="https://tess.mit.edu/observations/sector-36/">36</a>,
       <a href ="https://tess.mit.edu/observations/sector-37/">37</a>,
       <a href ="https://tess.mit.edu/observations/sector-38/">38</a>,
       <a href ="https://tess.mit.edu/observations/sector-39/">39</a>
       </td>
       <td><a href ="https://heasarc.gsfc.nasa.gov/docs/tess/extended.html">Extended</a></td>
       </tr>
       
       
        <tr>  
       <td>4</td>
       <td>Northern</td> 
       <td>06/24/21 - 09/01/22</td>
       <td><a href ="https://tess.mit.edu/observations/sector-40/">40</a>, 
       <a href ="https://tess.mit.edu/observations/sector-41/">41</a>,
       <a href ="https://tess.mit.edu/observations/sector-42/">42</a>,
       <a href ="https://tess.mit.edu/observations/sector-43/">43</a>,
       <a href ="https://tess.mit.edu/observations/sector-44/">44</a>,
       <a href ="https://tess.mit.edu/observations/sector-45/">45</a>,
       <a href ="https://tess.mit.edu/observations/sector-46/">46</a>,
       <a href ="https://tess.mit.edu/observations/sector-47/">47</a>,
       <a href ="https://tess.mit.edu/observations/sector-48/">48</a>,
       <a href ="https://tess.mit.edu/observations/sector-49/">49</a>,
       <a href ="https://tess.mit.edu/observations/sector-50/">50</a>,
       <a href ="https://tess.mit.edu/observations/sector-51/">51</a>,
       <a href ="https://tess.mit.edu/observations/sector-52/">52</a>
       <a href ="https://tess.mit.edu/observations/sector-53">53</a>
       <a href ="https://tess.mit.edu/observations/sector-54/">54</a>
       <a href ="https://tess.mit.edu/observations/sector-55/">55</a>
       </td>
       <td><a href ="https://heasarc.gsfc.nasa.gov/docs/tess/extended.html">Extended</a></td>
       </tr>
       
     </table>
</div>
</div>

##DRN Tables
Below we provide a brief summary of the DRN for each Sector.

###Sector 34

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>

       <tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_34_drn50_v01.pdf">50</a></td>
       <td><p>75</p> 
       <p>76</p></td>
       <td><p>2021-01-14 - 2021-01-26</p>
       <p>2021-01-27 - 2021-02-08</p></td>
       <td><p>720929 - 729684</p>
       <p>730459 - 739159<p></td>
       <td>1.08</td>
       <td>24.24</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>
	
	<tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 34 ID's are provided <a href="sector_34.html">here</a></td>
       </tr>
       
       <tr>  
       <td colspan="3">Space craft pointing:</td>
       <td colspan="4">Camera 1 and Camera 4 were both used for guiding in orbit 75 of Sector 34. Camera 4 alone was used for guiding in orbit 76.</td>
       </tr>

</table>
</div>
</div>

###Sector 33

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
        <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>


	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_33_drn49_v02.pdf">49</a></td>
       <td><p>73</p> 
       <p>74</p></td>
       <td><p>2020-12-18 -- 2020-12-30</p>
       <p>2020-12-31 -- 2021-01-13</p></td>
       <td><p>701476 -- 710214</p>
       <p>711341 -- 7720084<p></td>
       <td>1.57</td>
       <td>24.23</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

       <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 33 ID's are provided <a href="sector_33.html">here</a></td>
       </tr>
       
       <tr>  
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >In Sector 33, the Moon introduces a strong glint in Camera 1 at the end of orbit 73.</td>
       </tr>

       <tr>  
       <td colspan="3" ><b> Big update:</b></td>
       <td colspan="4" >
       <p>As of Sector 30, co-trending basis vector (CBV) files only include the first eight principal components for the Single Scale co-trending mode.</p> 
       <p>As a reminder, the pipeline only uses the first eight CBVs for co-trending, because subsequent CBVs are usually dominated by stochastic noise.</p> 
       <p>In Sectors 30–33, the values for CBVs 9–16 are set to 0.</p>
       </td>
       </tr>

</table>
</div>
</div>

###Sector 32

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>

	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_32_drn48_v02.pdf">48</a></td>
       <td><p>71</p> 
       <p>72</p></td>
       <td><p>2020-11-20 -- 2020-12-02</p>
       <p>2020-12-03 -- 2020-12-16</p></td>
       <td><p>681670 -- 690109</p>
       <p>690829 -- 700399<p></td>
       <td>1.0</td>
       <td>25.01</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>


       <tr>
       <td colspan="3" >Star tracker anomaly:</td>
       <td colspan="4" > UTC 2020-11-16 10:37, instrument turned off and collection of data for orbit 71 started 29 hrs later than scheduled. Normal operation started 2020-11-20-17-13-00 UTC.</td>
       </tr>
       
       <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 32 ID's are provided <a href="sector_32.html">here</a></td>
       </tr>

       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="4" >Camera 4 alone was used for guiding in Sector 72.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >In Sector 32, the Moon introduces a strong glint in Camera 1 at the end of orbit 71.</td>
       </tr>

</table>
</div>
</div>

###Sector 31

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>


	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_31_drn47_v02.pdf">47</a></td>
       <td><p>69</p> 
       <p>70</p></td>
       <td><p>2020-10-22 -- 2020-11-03</p>
       <p>2020-11-05 -- 2020-11-16</p></td>
       <td><p>660279 -- 669599</p>
       <p>670609 -- 678592<p></td>
       <td>1.4</td>
       <td>24.03</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

        <tr>
       <td colspan="3">Star tracker anomaly:</td>
       <td colspan="4"> UTC 2020-11-16 10:37, which led to the instrument being turned off. As a result, the data collection period in orbit 70 ended 2.08 days earlier than scheduled. The cameras were turned on and returned to normal operations on 2020-11-20, at the beginning of Sector 32.</td>
       </tr>

   <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 31 ID's are provided <a href="sector_31.html">here</a></td>
       </tr>

       <tr>
       <td colspan="3">Space craft pointing:</td>
       <td colspan="4">Camera 1 suffered from strong scattered light signals at the end of orbit 69 and orbit 70, and so Camera 4 alone was used for guiding during this sector.</td>
       </tr>      

       <tr>
       <td colspan="3">Scattered light:</td>
       <td colspan="4">In Sector 31, the Moon introduces a strong glint in Camera 1 at the end of orbit 69, followed by scattered light signals in all cameras caused by the Earth. Due to the star tracker anomaly, no data was not taken during periods of high scattered light in orbit 70.</td>
       </tr>       

</table>
</div>
</div>

###Sector 30

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>


	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_30_drn45_v02.pdf">45</a></td>
       <td><p>67</p> 
       <p>68</p></td>
       <td><p>2020-09-23 -- 2020-10-06</p>
       <p>2020-10-07 -- 2020-10-20</p></td>
       <td><p>639666 -- 649212</p>
       <p>649979 -- 659352<p></td>
       <td>1.07</td>
       <td>26.28</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

       <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 30 ID's are provided <a href="sector_30.html">here</a></td>
       </tr>
       
       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="4" >Camera 1 suffered from strong scattered light signals at the end of orbit 67 and orbit 68, and so Camera 4 alone was used for guiding during this sector.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >In Sector 30, the Moon introduces a strong glint in Camera 1 at the end of orbit 67, and the Earth introduces scattered light signals in all cameras at the end of both orbits.</td>
       </tr>
       

</table>
</div>
</div>

###Sector 29

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>

	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_29_drn43_v02.pdf">43</a></td>
       <td><p>65</p> 
       <p>66</p></td>
       <td><p>2020-08-26  -- 2020-09-08</p>
       <p>2020-09-09 -- 2020-09-21</p></td>
       <td><p>619761 -- 629222</p>
       <p>629904 -- 638624<p></td>
       <td>0.95</td>
       <td>25.25</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

       <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 29 ID's are provided <a href="sector_29.html">here</a></td>
       </tr>
       
       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="4" >Camera 1 suffered from strong scattered light signals at the end of orbit 65 and orbit 66, and so Camera 4 alone was used for guiding during this sector.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >In Sector 29, the Moon introduces a strong glint in Camera 1 at the end of orbit 65, and the Earth introduces scattered light signals in all cameras at the end of both orbits.</td>
       </tr>
       

</table>
</div>
</div>

###Sector 28

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
        <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>

	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_28_drn41_v02.pdf">41</a></td>
       <td><p>63</p> 
       <p>64</p></td>
       <td><p>2020-07-31 -- 2020-08-12</p>
       <p>2020-08-13 -- 2020-08-25</p></td>
       <td><p>600761 -- 609484</p>
       <p>610341 -- 618942<p></td>
       <td>1.19</td>
       <td>24.06</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>


   <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 28 ID's are provided <a href="sector_28.html">here</a></td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >In Sector 28, the Earth introduces scattered light signals at the end of both orbits.</td>
       </tr>

</table>
</div>
</div>

###Sector 27

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>
       
       
       <tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_27_drn38_v02.pdf">38</a></td>
       <td><p>61</p> 
       <p>62</p></td>
       <td><p>2020-07-05 -- 2020-07-17</p>
       <p>2020-07-18 -- 2020-07-30</p></td>
       <td><p>582349 -- 590884</p>
       <p>591619 -- 599894<p></td>
       <td>1.02</td>
       <td>23.35</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

   <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 27 ID's are provided <a href="sector_27.html">here</a></td>
       </tr>

       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="4" >Year 3 is a re-observation of the southern ecliptic hemisphere, which will take place over 13 sectors. The pointing strategy is the same as for Year 1, except the locations of Sectors 27–39 are offset in ecliptic longitude with respect to Sectors 1–13. All sectors in Year 3 are planned for a spacecraft pointing of −54 degrees in ecliptic latitude.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >In Sector 27, the Earth is a significant source of scattered light throughout both orbits.</td>
       </tr>

       <tr>
       <td colspan="3" ><b><p>Big Updates!</p>
       <p>This is the first data release for the extended mission</p><b></td>
       <td colspan="4" >
	<p>FFI data is collected every 10 min, rather than 30.</p>
	<p>Selected pixel stamps are collected at a 20-sec cadence.</p>
	<p>Data products for the 20 second mode have the keyword "fast" in the file names.</p>
	<p>For 20-second data, only target pixel files, light curve files, collateral pixel files, and co-trending basis vectors (CBVs) were produced.</p>
	<p>Cosmic rays were mitigated in the 2-minute cadence data and 10-minute FFIs by an algorithm running on the instrument firmware - see DRL pg. 8, for more info.</p>
	<p>The background correction employed in throughout the primary mission was updated for the extended mission. The new method provides improved results for fainter and crowded stars. The correction is applied only to 2-min and 20-sec data. A full explanation of this correction on pg. 10.</p>
	<p>Important note: The pixel level uncertainties have been over estimated since Sector 5, after the 2D block model was updated. Primary affected dim stars whose uncertainties were dominated by noise sources other than shot noise. Use empirical estimates of the scatter for anything realized before - see pg. 10 of DRN.</p>
        <p>For targets observed in both Year 1 and Year 3, Year 3 processing was done using TIC 8.1 while TIC 7 was used for Year 1 processing; this may result in differences in results for certain targets. Differences for some crowded and/or dim targets may also result from the background correction algorithm update. Reprocessing of Year 1 data with TIC 8.1 and the latest codebase is underway at the SPOC, as of Fall 2020. </p>
       </tr>

</table>
</div>
</div>

###Sector 26

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>

       <tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_26_drn37_v02.pdf">37</a></td>
       <td><p>59</p> 
       <p>60</p></td>
       <td><p>2020-06-09 -- 2020-06-21</p>
       <p>2020-06-22 -- 2020-07-04</p></td>
       <td><p>563621 -- 572209</p>
       <p>572871 -- 581529<p></td>
       <td>0.919</td>
       <td>23.95</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

   <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 26 ID's are provided <a href="sector_26.html">here</a></td>
       </tr>

       <tr>  
       <td colspan="3">Space craft pointing:</td>
       <td colspan="4"><p>The pointing in Sector 26 was set at +85 degrees in ecliptic latitude so that Camera 2 and Camera 3 straddle the ecliptic pole.</p>
      <p>Camera 1 suffered from strong scattered light signals at the midpoint of orbit 59 and orbit 60, and so Camera 4 alone was used for guiding during this sector.</p></td>
       </tr>

       <tr>
       <td colspan="3">Scattered light:</td>
       <td colspan="4">In Sector 26, the Earth is a significant source of scattered light throughout both orbits.</td>
       </tr>

       <tr>
       <td colspan="3"><b> Big Updates!<b></td>
       <td colspan="4">The TESS spacecraft configuration file was updated from version ‘0187’ to ‘0188’ between orbit 59 and 60. The SPOC data products include this 4 digit identification code near the end of the filename. Therefore the FFIs from orbit 59 have a different 4 digit identification number than those from orbit 60.</td>
       </tr>

</table>
</div>
</div>

###Sector 25

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Sector 25</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>

       <tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_25_drn36_v02.pdf">36</a></td>
       <td><p>57</p> 
       <p>58</p></td>
       <td><p>2020-05-14 -- 2020-05-26</p>
       <p>2020-05-27 -- 2020-06-08</p></td>
       <td><p>544444 -- 553089</p>
       <p>554009 -- 562932<p></td>
       <td>1.28</td>
       <td>24.4</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

       <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 25 ID's are provided <a href="sector_25.html">here</a></td>
       </tr>

       <tr>  
       <td colspan="3">Space craft pointing:</td>
       <td colspan="4"><p>As in Sector 14, the pointing in Sector 25 was set at +85 degrees in ecliptic latitude so that Camera 2 and Camera 3 straddle the ecliptic pole.</p>
       <p>Camera 1 suffered from strong scattered light signals at the beginning of orbit 57 and orbit 58, and so Camera 4 alone was used for guiding during this sector.</p></td>
       </tr>

       <tr>
       <td colspan="3">Scattered light:</td>
       <td colspan="4">In Sector 25, the Earth is a significant source of scattered light throughout both orbits.</td>
       </tr>

</table>
</div>
</div>

###Sector 24

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>


	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_24_drn35_v02.pdf">35</a></td>
       <td><p>55</p> 
       <p>56</p></td>
       <td><p>2020-04-16 -- 2020-04-28</p>
       <p>2020-04-29 -- 2020-05-12</p></td>
       <td><p>524401 -- 533442</p>
       <p>534104 -- 543474<p></td>
       <td>>0.92</td>
       <td>25.57</td>
       <td><p>0</p>
       <p>1</p></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

   <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 24 ID's are provided <a href="sector_24.html">here</a></td>
       </tr>

       <tr>  
       <td colspan="3">Space craft pointing:</td>
       <td colspan="4"><p>As in Sector 14, the pointing in Sector 24 was set at +85 degrees in ecliptic latitude so that Camera 2 and Camera 3 straddle the ecliptic pole.</p>
       <p>In Sector 24 there is an anomalously high pointing jitter was observed for the last 3–4 days of that orbit.</p></td>
       </tr>
       
       <tr>  
       <td colspan="3">Scattered light:</td>
       <td colspan="4">In Sector 24, the Earth is a significant source of scattered light throughout both orbits.</td>
       </tr>

</table>
</div>
</div>

###Sector 23

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>


	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_23_drn32_v03.pdf">34</a></td>
       <td><p>54</p> 
       <p>53</p></td>
       <td><p>2020-03-19 - 2020-04-01</p>
       <p>2020-04-02 -- 2020-04-15</p></td>
       <td><p>504464 -- 513659</p>
       <p>514351 -- 523742<p></td>
       <td>>0.96</td>
       <td>25.81</td>
       <td><p>1</p>
       <p>1</p></td>
       </tr>


 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

       <tr>
       <td colspan="3" >Instrument issues:</td>
       <td colspan="4" >The spacecraft passed through the shadow of Earth from approximately TJD 1940.38 – 1940.48. The instrument was not turned off, and other than the instrument heaters turning on resulting in a minor pointing offset, there is no indication that science quality was affected.</td>
       </tr>
       
          <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 23 ID's are provided <a href="sector_23.html">here</a></td>
       </tr>
       
        <tr>  
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="4" >In orbit 1 of Sector 23, anomalously high pointing jitter was observed for about 1.5 days before the momentum dump starting at ∼ TJD 1936.15. The peak-to-peak amplitude of the jitter is less than 1.5 arcseconds on 2 minute timescales.</td>
       </tr>

       <tr>  
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >Camera 1 suffered from strong scattered light signals at the beginning of orbit 53 and orbit 54, and so Camera 4 alone was used for guiding during this sector. The Earth is a significant source of scattered light at the start of both orbits. The Moon also passes close to the field of view of Camera 1 during orbit 54.</td>
       </tr>

  

</table>
</div>
</div>

###Sector 22

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">


       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
        <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>


	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_22_drn31_v02.pdf">31</a></td>
       <td><p>51</p> 
       <p>52</p></td>
       <td><p>2020-02-19 -- 2020-03-04</p>
       <p>2020-03-05 -- 2020-03-17</p></td>
       <td><p>483729 -- 493234</p>
       <p>494001 -- 503307<p></td>
       <td>1.07 </td>
       <td>26.13</td>
       <td><p>Every 6.625 days</p>
       <p>Every 6.75 days</p></td>
       </tr>


 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>


   <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 22 ID's are provided <a href="sector_22.html">here</a></td>
       </tr>

       <tr>  
       <td colspan="3">Space craft pointing:</td>
       <td colspan="4">Camera 1 and Camera 4 were both used for guiding in orbit 51; Camera 4 alone was used for guiding in orbit 52.</td>
       </tr>

       <tr>  
       <td colspan="3">Scattered light:</td>
       <td colspan="4">In Sector 22, the Earth is a significant source of scattered light at the start of both orbits. The Moon also passes through the field of view of Camera 1 at the start of orbit 52, saturating the detectors Camera 4 alone was used for guiding in orbit 52.</td>
       </tr>

       <tr>  
       <td colspan="3">Watchdog Resets:</td>
       <td colspan="4"><p>The instrument computer unexpectedly hung, most likely due to space radiation induced errors in the computer processor or memory, resulting in a quick reboot of the computer.</p>
       <p>There were three watchdog timer resets in Sector 22: on 2/29/20, 3/3/20, and 3/12/20.</p>
       <p>Besides introducing short gaps in the 2m cadence data, these resets resulted in the loss a total of four FFI cadences.</p>
       <p>Two 2-minute cadences are missing from TJD 1909.46004 to 1909.4642 (2/29/20), from TJD 1911.9267 to 1911.9309 (3/3/20), and from 1921.0560 to 1921.0602 (3/12/20).<p></td>
       </tr>

       <tr>  
       <td colspan="3"><b>Big Update: Corrections to Data Product Timestamps</b></td>
       <td colspan="4"><p>The reported times for previous data products are too large by 2 seconds. This issue has been fixed for Sector 22 data products, which have updated and accurate timestamps.</p>
       <p>Timestamps from previous sectors can be corrected by subtracting 2 seconds. Future data releases will include reprocessed data with corrected timestamps.</p>
       <p>The start times of integrations for every 2 minute and 30 minute cadence have been shifted forward by 31 milliseconds, and the end times have been shifted forward by 11 milliseconds.</p>
       <p>These offsets correct for effects in the focal plane electronics that were not accounted for in previous data releases. Until data is re-processed the times must be adjusted by adding correct values to headers.</p>
       <p>Two-minute data products report the TJD at mid-exposure, and so should be corrected by adding 21 milliseconds to the timestamps.</p>
       <p>Note that the correction only applies to the timestamps themselves; the reported exposure times in data product headers and flux values (electrons per second) are correct.</p></td>
       </tr>

</table>
</div>
</div>

###Sector 21

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">

       <col style="width:5%">
       <col style="width:5%">
       <col style="width:20%">
       <col style="width:20%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       </tr>
       </thead>

	<tr>  
       <td><a href="https://archive.stsci.edu/missions/tess/doc/tess_drn/tess_sector_21_drn29_v03.pdf">29</a></td>
       <td><p>49</p> 
       <p>50</p></td>
       <td><p>2020-01-21 -- 2020-02-04</p>
       <p>2020-02-05 -- 2020-02-18</p></td>
       <td><p>462941 -- 472707</p>
       <p>473374 -- 482634<p></td>
       <td>0.93</td>
       <td>24.42</td>
       <td><p>Every 6.25 days</p>
       <p>Every 6.5 days</p></td>
       </tr>


 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

       <tr>
       <td colspan="3" >Instrument reset:</td>
       <td colspan="4" >Occurred in orbit 50, no data collected for 2 min between TJD 1892.50598 and 1892.50875.</td>
       </tr>
   
       <tr>
       <td colspan="3" >Science data:</td>
       <td colspan="4" > days</td>
       </tr>
       
       <tr>  
       <td colspan="3">Problematic TIC ID's:</td>
       <td colspan="4">A list of Sector 21 ID's are provided <a href="sector_21.html">here</a></td>
       </tr>
       
        <tr>  
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="4" >Camera 1 and Camera 4 were both used for guiding in orbit 49; Camera 4 alone was used for guiding in orbit 50.</td>
       </tr>

       <tr>  
       <td colspan="3" >Scattered light:</td>
       <td colspan="4" >In Sector 21, the Moon passes through the field of view of Camera 1 at the start of orbit 50, saturating the detectors. A strong glint also appears in Camera 2 during this time.</td>
       </tr>

       <tr>  
       <td colspan="3" ><b>Big Update: Corrections to Data Product Timestamps</b></td>
       <td colspan="4" >In Sector 21, the the FFI timestamps have been adjusted for the 0.5 second staggered readouts of the four cameras and the 0.02 second staggered readouts for individual CCDs within a camera.
       TSTART and TSTOP in the FFIs of previous sectors need to be adjusted for the readout offsets of each camera—see DRN 25 for additional details.
       </td>
       </tr>

</table>
</div>
</div>

###Reprocessing of Sectors 14–19

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<div class="panel-body">

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:18%">
       <col style="width:18%">
       <col style="width:14.3%">
       <col style="width:14.3%">
       <col style="width:14.3%">

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="4" style="vertical-align: middle;"><b>Description</b></td>

       <tr>
       <td colspan="3" >Timestamps:</td>
       <td colspan="4" >The timestamps for 2 minute cadence and FFI data are more accurate. The differences between reprocessed data and previous data releases are less than 2.0 seconds in all cases.</td>
       </tr>

       <tr>
       <td colspan="3" >Apertures:</td>
       <td colspan="4" >Photometric apertures were increased in size for targets with Tmag < 11</td>
       </tr>

       <tr>
       <td colspan="3" >Data Anomaly Flags:</td>
       <td colspan="4" >Three new flags were added to mitigate the effects of scattered light.</td>
       </tr>

      
       <tr>
       <td colspan="3" >Planet search:</td>
       <td colspan="4" >Given the re-porcessed light curves a different set of TCEs from the original processed data, were obtained. There is a 83% overlap with previous results. Not every TCE from previous data releases were recovered.</td>
       </tr>

</table>
</div>
</div>