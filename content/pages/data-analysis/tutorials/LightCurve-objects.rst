LightCurve objects
##################
:save_as: LightCurve-object-Tutorial.html

Understanding LightCurve objects
================================

Learning goals
--------------

In our `TargetPixelFile tutorial <Target-Pixel-File-Tutorial.html>`__ we
learned, how to obtain data files for our objects of interest and how to
examine the ``metadata`` stored in the headers.

In this tutorial we will learn the following, - How to use *Lightkurve*
to create a
`TESSLightCurve <https://docs.lightkurve.org/api/lightkurve.lightcurve.TessLightCurve.html#lightkurve.lightcurve.TessLightCurve>`__
object. - How to examine the object data, and understand its format. -
What is simple aperture photometry (SAP). - How to plot a light curve.

What is LightCurve object?
--------------------------

You can create a ``TESSLightCurve`` object from a ``TargetPixelFile``
(TPF) object using Simple Aperture Photometry (SAP).

What is Simple Aperture Photometry (SAP)?
-----------------------------------------

Aperture Photometry is the act of summing up the values of all the
pixels in a pre-defined aperture as a function of time. By carefully
choosing the shape of the aperture mask, you can avoid nearby
contaminants or improve the strength of the specific signal you are
trying to measure relative to the background.

The SAP light curve is a pixel summation time-series of all calibrated
flux falling within the optimal aperture, as stored and defined in the
TPF.

In this notebook we will demonstrate, let’s create a ``TESSLightCurve``
from a ``TESSTargetPixelFile``.

Imports
-------

This tutorial requires that you import *Lightkurve*.

.. code:: ipython3

    %matplotlib inline 
    import lightkurve as lk

Defining terms
--------------

-  Target Pixel File (TPF): A file containing the original CCD pixel
   observations from which light curves are extracted.

-  LightCurve Object: Obtained from a TPF and contains light curve
   information derived using simple aperture photometry.

-  Cadence: The rate at which TESS photometric observations are stored.

-  Sector: One of TESS’s 27 (to date) observing periods, approximately
   ~27 days in duration.

-  Simple Aperture Photometry (SAP): The act of summing all pixel values
   in a pre-defined aperture as a function of time.

Downloading the TPF
-------------------

For this tutorial we will use the `L 98-59
System <https://arxiv.org/pdf/1903.08017.pdf>`__ focusing on planet c.

First we search for appropriate Target Pixel Files on
`MAST <https://archive.stsci.edu/tess/>`__ using the
`search_targetpixelfile <https://docs.lightkurve.org/api/lightkurve.search.search_targetpixelfile.html?highlight=search_targetpixelfile>`__
function.

.. code:: ipython3

    search = lk.search_targetpixelfile('TIC 307210830 c')
    search




.. raw:: html

    SearchResult containing 7 data products.
    
    <table id="table140359681659232">
    <thead><tr><th>#</th><th>observation</th><th>author</th><th>target_name</th><th>productFilename</th><th>distance</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 2</td><td>SPOC</td><td>307210830</td><td>tess2018234235059-s0002-0000000307210830-0121-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 5</td><td>SPOC</td><td>307210830</td><td>tess2018319095959-s0005-0000000307210830-0125-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 8</td><td>SPOC</td><td>307210830</td><td>tess2019032160000-s0008-0000000307210830-0136-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 9</td><td>SPOC</td><td>307210830</td><td>tess2019058134432-s0009-0000000307210830-0139-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 10</td><td>SPOC</td><td>307210830</td><td>tess2019085135100-s0010-0000000307210830-0140-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 11</td><td>SPOC</td><td>307210830</td><td>tess2019112060037-s0011-0000000307210830-0143-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 12</td><td>SPOC</td><td>307210830</td><td>tess2019140104343-s0012-0000000307210830-0144-s_tp.fits</td><td>0.0</td></tr>
    </table>



Our object of interest can be found in seven sectors. Let’s take the
first sector, sector 2 and download that.

.. code:: ipython3

    tpf = lk.search_targetpixelfile('TIC 307210830 c', sector=2).download()
    tpf




.. parsed-literal::

    TessTargetPixelFile(TICID: 307210830)



Creating and analizing the LightCurve object
--------------------------------------------

Great we now have our TPF! Lets convert this TPF into a
``TessLightCurve`` object using the
`to_lightcurve <https://docs.lightkurve.org/api/lightkurve.targetpixelfile.TessTargetPixelFile.html#lightkurve.targetpixelfile.TessTargetPixelFile.to_lightcurve>`__
function.

To create the SAP lightcurve we will pass an **aperture_mask** to the
``to_lightcurve`` function. The default is to use the
`SPOC <https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html>`__
pipeline aperture, which sums all the pixels in its defined mask.

.. code:: ipython3

    lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)
    lc




.. raw:: html

    <i>TessLightCurve targetid=307210830 length=18317</i>
    <table id="table140359674564792" class="table-striped table-bordered table-condensed">
    <thead><tr><th>time</th><th>flux</th><th>flux_err</th><th>centroid_col</th><th>centroid_row</th><th>cadenceno</th><th>quality</th></tr></thead>
    <thead><tr><th></th><th>electron / s</th><th>electron / s</th><th>pix</th><th>pix</th><th></th><th></th></tr></thead>
    <thead><tr><th>object</th><th>float32</th><th>float32</th><th>float64</th><th>float64</th><th>int32</th><th>int32</th></tr></thead>
    <tr><td>1354.1088231272427</td><td>21566.349609375</td><td>16.116119384765625</td><td>664.6090864691554</td><td>339.4764484490161</td><td>91191</td><td>0</td></tr>
    <tr><td>1354.1102119888994</td><td>21563.88671875</td><td>16.118038177490234</td><td>664.6261723169015</td><td>339.46842003296774</td><td>91192</td><td>0</td></tr>
    <tr><td>1354.112989712153</td><td>21475.162109375</td><td>16.089221954345703</td><td>664.606630403678</td><td>339.4604662968742</td><td>91194</td><td>0</td></tr>
    <tr><td>1354.1143785738097</td><td>21583.30859375</td><td>16.12527084350586</td><td>664.6414481151693</td><td>339.4832617761526</td><td>91195</td><td>0</td></tr>
    <tr><td>1354.1157674355243</td><td>21575.640625</td><td>16.121679306030273</td><td>664.6354584758038</td><td>339.4735678477034</td><td>91196</td><td>0</td></tr>
    <tr><td>1354.1171562971804</td><td>21563.1015625</td><td>16.115528106689453</td><td>664.6334974032626</td><td>339.472138768046</td><td>91197</td><td>0</td></tr>
    <tr><td>1354.1185451588947</td><td>21552.935546875</td><td>16.112627029418945</td><td>664.625177003332</td><td>339.46675685339096</td><td>91198</td><td>0</td></tr>
    <tr><td>1354.1199340205515</td><td>21532.90234375</td><td>16.10567855834961</td><td>664.6301979867933</td><td>339.4699372207359</td><td>91199</td><td>0</td></tr>
    <tr><td>1354.1213228822667</td><td>21533.828125</td><td>16.105731964111328</td><td>664.6262018316135</td><td>339.46553338843</td><td>91200</td><td>0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>1381.5001032523294</td><td>21262.494140625</td><td>16.291688919067383</td><td>664.5744500858646</td><td>339.3513278016392</td><td>110913</td><td>0</td></tr>
    <tr><td>1381.5014921207378</td><td>21289.828125</td><td>16.302898406982422</td><td>664.5797804765874</td><td>339.3491398520347</td><td>110914</td><td>0</td></tr>
    <tr><td>1381.5028809891458</td><td>21266.3515625</td><td>16.29288673400879</td><td>664.5790106545255</td><td>339.3513312907625</td><td>110915</td><td>0</td></tr>
    <tr><td>1381.5042698574382</td><td>21234.845703125</td><td>16.279603958129883</td><td>664.5730941550626</td><td>339.3555631381705</td><td>110916</td><td>0</td></tr>
    <tr><td>1381.5056587258466</td><td>21244.953125</td><td>16.281909942626953</td><td>664.5782007755507</td><td>339.3468316465567</td><td>110917</td><td>0</td></tr>
    <tr><td>1381.5070475942555</td><td>21210.7578125</td><td>16.267162322998047</td><td>664.5770708377116</td><td>339.3442359060069</td><td>110918</td><td>0</td></tr>
    <tr><td>1381.508436462548</td><td>21231.01171875</td><td>16.27315330505371</td><td>664.5786574675517</td><td>339.34217245510536</td><td>110919</td><td>0</td></tr>
    <tr><td>1381.5098253309563</td><td>21250.466796875</td><td>16.277507781982422</td><td>664.5722297003167</td><td>339.3513272975753</td><td>110920</td><td>0</td></tr>
    <tr><td>1381.5112141992488</td><td>21236.35546875</td><td>16.2720890045166</td><td>664.582152318805</td><td>339.3452178427711</td><td>110921</td><td>0</td></tr>
    <tr><td>1381.5126030676577</td><td>21265.83984375</td><td>16.278945922851562</td><td>664.5729270180528</td><td>339.349710493043</td><td>110922</td><td>0</td></tr>
    </table>



We’ve built a new ``TESSLightCurve`` object called ``lc``. Note although
we used the SPOC aperture mask you can pass your own aperture,
(specified by a boolean ``numpy`` array) as seen in the `Making Custom
Apertures tutorial <Making-Custom-Apertures-Tutorial.html>`__.

The above table displays all the light curve data.

Metadata
--------

``TESSLightCurve`` objects have many useful functions that you can use.
As with a TPF you can access the meta data very simply.

.. code:: ipython3

    lc.sector




.. parsed-literal::

    2



Of course you still have access to time and flux attributes. In a
light curve, there is only one flux point for every cadence.

.. code:: ipython3

    lc.flux, lc.time




.. parsed-literal::

    (<Quantity [21566.35 , 21563.887, 21475.162, ..., 21250.467, 21236.355,
                21265.84 ] electron / s>,
     <Time object: scale='tdb' format='btjd' value=[1354.10882313 1354.11021199 1354.11298971 ... 1381.50982533 1381.5112142
      1381.51260307]>)



You can also check the Combined Differential Photometric Precision
(CDPP) RMS per transit duration noise metric (see `Gilliland et al.,
2011 <https://iopscience.iop.org/article/10.1088/0067-0049/197/1/6/pdf>`__
for more details) of the light curve using the built in method
`estimate_cdpp <https://docs.lightkurve.org/api/lightkurve.lightcurve.FoldedLightCurve.html#lightkurve.lightcurve.FoldedLightCurve.estimate_cdpp>`__:

.. code:: ipython3

    lc.estimate_cdpp()




.. math::

    300.86106 \; \mathrm{ppm}



The above is the Savitzky-Golay CDPP noise metric in units
parts-per-million (ppm)

Plotting the light curve
------------------------

We can now use the built in ``plot`` function on the ``TESSLightCurve``
object to plot the time series. You can pass ``plot`` any keywords you
would normally pass to
`matplotlib.pyplot.plot <https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.plot.html>`__.

.. code:: ipython3

    %matplotlib inline
    lc.plot();



.. image:: images/LightCurve-objects_files/LightCurve-objects_23_0.png


Manipulating the light curve
----------------------------

There are a set of useful functions in
`LightCurve <https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve>`__
objects which you can use to work with the data. These include: \*
`flatten() <https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve.flatten>`__:
Remove long term trends using a `Savitzky–Golay
filter <https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter>`__
\*
`remove_outliers() <https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve.remove_outliers>`__:
Remove outliers using simple sigma clipping \*
`remove_nans() <https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve.remove_nans>`__:
Remove infinite or NaN values (these can occur during thruster firings)
\*
`fold() <https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve.fold>`__:
Fold the data at a particular period \*
`bin() <https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve.bin>`__:
Reduce the time resolution of the array, taking the average value in
each bin.

We can use these simply on a light curve object

.. code:: ipython3

    flat_lc = lc.flatten(window_length=401)
    flat_lc.plot();



.. image:: images/LightCurve-objects_files/LightCurve-objects_25_0.png


Folding the light curve
~~~~~~~~~~~~~~~~~~~~~~~

From the `L 98-59 System <https://arxiv.org/pdf/1903.08017.pdf>`__ paper
we know that planet c has a time corresponding to zero phase (noted as
epoch_time) of 1367.2755 BTJD days and period of 3.690621 days. We can
use the ``fold()`` function to find the transit in our data.

.. code:: ipython3

    folded_lc = flat_lc.fold(period=3.690621,  epoch_time=1367.2755)
    folded_lc.plot();



.. image:: images/LightCurve-objects_files/LightCurve-objects_27_0.png


Binning data
~~~~~~~~~~~~

Often to see a trend it can be beneficial to bin the data, this can be
achieved via the ``bin()`` function.

.. code:: ipython3

    binned_lc = folded_lc.bin(time_bin_size=0.025)
    binned_lc.plot();



.. image:: images/LightCurve-objects_files/LightCurve-objects_29_0.png


We can now see our transit very clearly! Note that we can achieve the
same plot from our data using one line of code instead of several, see
below.

.. code:: ipython3

    lc.remove_nans().flatten(window_length=401).fold(period=3.690621,  epoch_time=1367.2755).bin(time_bin_size=0.025).plot();



.. image:: images/LightCurve-objects_files/LightCurve-objects_31_0.png

