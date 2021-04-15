Title: TESS Data Release Notes
Save_as: data_release_notes.html

[TOC]

As the TESS mission has evolved, so has the processing and delivery of its data. Whilst a [data release note (DRN)](https://archive.stsci.edu/tess/tess_drn.html) is provided for every sector of the mission, this page hi-lights important changes that might affect you, the user, and your handling/understanding of the data.

##Key updates
Below we outline some of the most important issues or data product modifications. For more details please see the Sector tables provided below, and the DRNs listed within.

- [**Sector 32:**](data_release_notes.html#sector-32) Approximately 26 hrs lost due to a star tracker anomaly.<p></p>
- [**Sector 31:**](data_release_notes.html#sector-31) Approximately 4 days lost due to a star tracker anomaly.<p></p>
- [**Sector 30:**](data_release_notes.html#sector-30) As of Sector 30, co-trending basis vector (CBV) files only include the first eight principal components for the Single Scale co-trending mode. <p></p>
- [**Sector 27:**](data_release_notes.html#sector-27) This is the first data release for the extended mission. Key changes have occurred including the collection of 10 min FFI data instead of 30 min, and 20 second target pixel files.<p></p>
<p>The background correction was updated for the extended mission, with the new method providing improved results for fainter and crowded stars. 
<p>For targets observed in both Year 1 and Year 3, Year 3 processing was done using TIC 8.1 while TIC 7 was used for Year 1 processing; this may result in differences in results for certain targets.</p>

<a class="btn btn-default btn-xs" href="key_updates_archive.html">Key update archive &raquo;</a>

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

##Cycle 3 DRN Tables
Below we provide a brief summary of the DRNs for each Sector in Cycle 3. 

###Sector 34

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_34.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>
       
       <tr>  
       <td colspan="3">Space craft pointing:</td>
       <td colspan="5">Camera 1 and Camera 4 were both used for guiding in orbit 75 of Sector 34. Camera 4 alone was used for guiding in orbit 76.</td>
       </tr>

</table>
</div>
</div>

###Sector 33

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       
       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
        <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_33.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>
       
       <tr>  
       <td colspan="3" >Scattered light:</td>
       <td colspan="5" >In Sector 33, the Moon introduces a strong glint in Camera 1 at the end of orbit 73.</td>
       </tr>

       <tr>  
       <td colspan="3" ><b> Big update:</b></td>
       <td colspan="5" >
       <p>As of Sector 30, co-trending basis vector (CBV) files only include the first eight principal components for the Single Scale co-trending mode.</p> 
       <p>As a reminder, the pipeline only uses the first eight CBVs for co-trending, because subsequent CBVs are usually dominated by stochastic noise. When using CBVs beyond 8, users should check for excess noise being introduced into the detrended light curve</p> 
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

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_32.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>


       <tr>
       <td colspan="3" >Star tracker anomaly:</td>
       <td colspan="5" > UTC 2020-11-16 10:37, instrument turned off and collection of data for orbit 71 started 29 hrs later than scheduled. Normal operation started 2020-11-20-17-13-00 UTC.</td>
       </tr>
      

       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="5" >Camera 4 alone was used for guiding in Sector 72.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="5" >In Sector 32, the Moon introduces a strong glint in Camera 1 at the end of orbit 71.</td>
       </tr>

</table>
</div>
</div>

###Sector 31

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       
       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_31.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>

        <tr>
       <td colspan="3">Star tracker anomaly:</td>
       <td colspan="5"> At UTC 2020-11-16 10:37, there was a star tracker anomaly which led to the instrument being turned off. As a result, the data collection period in orbit 70 ended 2.08 days earlier than scheduled. The cameras were turned on and returned to normal operations on 2020-11-20, at the beginning of Sector 32.</td>
       </tr>


       <tr>
       <td colspan="3">Space craft pointing:</td>
       <td colspan="5">Camera 1 suffered from strong scattered light signals at the end of orbit 69 and orbit 70, and so Camera 4 alone was used for guiding during this sector.</td>
       </tr>      

       <tr>
       <td colspan="3">Scattered light:</td>
       <td colspan="5">In Sector 31, the Moon introduces a strong glint in Camera 1 at the end of orbit 69, followed by scattered light signals in all cameras caused by the Earth. Due to the star tracker anomaly, no data were taken during periods of high scattered light in orbit 70.</td>
       </tr>       

</table>
</div>
</div>

###Sector 30

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_30.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>

       
       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="5" >Camera 1 suffered from strong scattered light signals at the end of orbit 67 and orbit 68, and so Camera 4 alone was used for guiding during this sector.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="5" >In Sector 30, the Moon introduces a strong glint in Camera 1 at the end of orbit 67, and the Earth introduces scattered light signals in all cameras at the end of both orbits.</td>
       </tr>
       

</table>
</div>
</div>

###Sector 29

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_29.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>

       
       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="5" >Camera 1 suffered from strong scattered light signals at the end of orbit 65 and orbit 66, and so Camera 4 alone was used for guiding during this sector.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="5" >In Sector 29, the Moon introduces a strong glint in Camera 1 at the end of orbit 65, and the Earth introduces scattered light signals in all cameras at the end of both orbits.</td>
       </tr>
       

</table>
</div>
</div>

###Sector 28

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
        <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_28.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>


       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="5" >In Sector 28, the Earth introduces scattered light signals at the end of both orbits.</td>
       </tr>

</table>
</div>
</div>

###Sector 27

<div class="panel panel-primary">
  <div class="panel-heading">
    <h3 class="panel-title">Information</h3>
  </div>

<table class="table table-striped table-hover" style="font-size: 0.77em;">
       <col style="width:5%">
       <col style="width:5%">
       <col style="width:25%">
       <col style="width:25%">
       <col style="width:13.3%">
       <col style="width:13.3%">
       <col style="width:13.3%">

       <thead>
       <tr>
       <th style="vertical-align: middle;">DRN</th>
       <th style="vertical-align: middle;">Orbits</th>
       <th style="vertical-align: middle;">Dates (UTC) <p>Start - End</p></th>
       <th style="vertical-align: middle;">Cadence # <p>Start - End</p></th>
       <th style="vertical-align: middle;">Data pause <p>(days)</p></th>
       <th style="vertical-align: middle;">Science data (days)</th>
       <th style="vertical-align: middle;">Momentum dumps</th>
       <th style="vertical-align: middle;">Problematic <p>TIC ID's</p></th>
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
       <td><a href="sector_27.html">list</a></td>
       </tr>

 	<td colspan="3" style="vertical-align: middle;"><b>Issue</b></td>
	<td colspan="5" style="vertical-align: middle;"><b>Description</b></td>


       <tr>
       <td colspan="3" >Space craft pointing:</td>
       <td colspan="5" >Year 3 is a re-observation of the southern ecliptic hemisphere, which will take place over 13 sectors. The pointing strategy is the same as for Year 1, except the locations of Sectors 27–39 are offset in ecliptic longitude with respect to Sectors 1–13. All sectors in Year 3 are planned for a spacecraft pointing of −54 degrees in ecliptic latitude.</td>
       </tr>

       <tr>
       <td colspan="3" >Scattered light:</td>
       <td colspan="5" >In Sector 27, the Earth is a significant source of scattered light throughout both orbits.</td>
       </tr>

       <tr>
       <td colspan="3" ><b><p>Big Updates!</p>
       <p>This is the first data release for the extended mission</p><b></td>
       <td colspan="5" >
	<p>FFI data is collected every 10 min, rather than 30.</p>
	<p>Selected pixel stamps are collected at a 20-sec cadence.</p>
	<p>Data products for the 20 second mode have the keyword "fast" in the file names.</p>
	<p>For 20-second data, only target pixel files, light curve files, collateral pixel files, and co-trending basis vectors (CBVs) were produced.</p>
	<p>As usual cosmic rays were mitigated in the 2-minute cadence data and 10-minute FFIs by an algorithm running on the instrument firmware - see DRN pg. 8, for more info. Note however, that in the new 20-second pixel data cosmic rays were identified and removed in the pipeline, and that they can be restored in the pixel data and light curves if necessary.</p>
	<p>The background correction employed throughout the primary mission was updated for the extended mission. The new method provides improved results for fainter and crowded stars. The correction is applied only to 2-min and 20-sec data. A full explanation of this correction is on pg. 10 of the DRN</p>
        <p>For targets observed in both Year 1 and Year 3, Year 3 processing was done using TIC 8.1 while TIC 7 was used for Year 1 processing; this may result in different results for certain targets. Differences for some crowded and/or dim targets may also result from the background correction algorithm update. Reprocessing of Year 1 data with TIC 8.1 and the latest codebase is underway at the SPOC, as of Fall 2020. </p>
       </tr>

</table>
</div>
</div>


##Cycle 2 DRN Tables
Below we provide a brief summary of the DRNs for each Sector in Cycle 2. <p></p>
<a class="btn btn-default btn-xs" href="cycle2_drn.html">Cycle 2 Tables &raquo;</a>


##Cycle 1 DRN Tables
Below we provide a brief summary of the DRNs for each Sector in Cycle 1. <p></p>
<a class="btn btn-default btn-xs" href="cycle1_drn.html">Cycle 1 Tables &raquo;</a>

##Useful links

Below we list some potentially useful urls for those users wishing to learn more about TESS (and Kepler) data processing. 

- [TESS Science Data Products Description Document](https://archive.stsci.edu/missions/tess/doc/EXP-TESS-ARC-ICD-TM-0014.pdf)

- [TESS Instrument Handbook](https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/active-missions/tess/_documents/TESS_Instrument_Handbook_v0.1.pdf)

- [Kepler Data Processing Handbook ](https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/kepler/_documents/KSCI-19081-003-KDPH.pdf)
