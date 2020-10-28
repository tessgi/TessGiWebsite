Aperture Photometry
###################
:save_as: Aperture-Photometry-Tutorial.html

Understanding aperture photometry & making custom apertures.
============================================================

Learning goals
--------------

In our previous tutorials (`LightCurve
object <LightCurve-object-Tutorial.html>`__ and `LightCurveFile
object <LightCurveFile-Object-Tutorial.html>`__) we learned about aperture
photometry and the Simple Aperture Photometry (SAP) and Pre-search Data
Conditioning SAP (PDCSAP) flux.

We have not however discussed how these apertures are chosen by the
pipeline or how to examine them.

In this proposal we will cover the following, - How apertures are
defined. - How can we examine a pre-defined aperture. - How we can
define and modify an aperture and recover the light curve.

SPOC apertures
--------------

In aperture photometry A set of pixels in the image are chosen and we
sum those to produce a single flux value. The
`SPOC <https://heasarc.gsfc.nasa.gov/docs/tess/pipeline.html>`__
produces an *optimal aperture*, which is used by default in
*Lightkurve*, and determined by the `data processing
pipeline <https://github.com/nasa/kepler-pipeline>`__. This is the
default aperture used by *Lightkurve* and is optimized to ensure that
the stellar signal has a high signal to noise ratio, with minimal
contamination from the background.

We sum these same pre-selected pixels for every image at each cadence to
produce a light curve.

There are however, some cases where you might want to produce your own
aperture. The field may be crowded, or you may wish to change the
aperture size to change the relative contribution of the background.
*Lightkurve* offers tools to select pixels programmatically.

We will show you how to examine the pre-selected aperture and how to
modify it if you wish.

Imports
-------

This tutorial requires: - `Lightkurve <https://docs.lightkurve.org>`__ -
`Matplotlib <https://matplotlib.org/>`__ - `numpy <https://numpy.org>`__

Defining terms
--------------

-  Target Pixel File (TPF): A file containing the original CCD pixel
   observations from which light curves are extracted.

-  LightCurve Object: Obtained from a TPF and contains light curve
   information derived using simple aperture photometry.

-  LightCurveFile Object: Obtained from MAST and contains both SAP flux
   and PSDCSAP flux.

-  Cadence: The rate at which TESS photometric observations are stored.

-  Sector: One of TESS’s 27 (to date) observing periods, approximately
   ~27 days in duration.

-  Simple Aperture Photometry (SAP): The act of summing all pixel values
   in a pre-defined aperture as a function of time.

-  Pre-search Data Conditioning SAP flux (PDCSAP) flux : SAP flux from
   which long term trends have been removed using so-called Co-trending
   Basis Vectors (CBVs). PDCSAP flux is usually cleaner data than the
   SAP flux and will have fewer systematic trends.

.. code:: ipython3

    %matplotlib inline 
    import numpy as np
    import lightkurve as lk
    import matplotlib.pyplot as plt

Downloading the data
--------------------

For this tutorial lets use the `L 98-59
System <https://arxiv.org/pdf/1903.08017.pdf>`__ again, focusing on
planet c. First let’s search for a TPF for this object.

.. code:: ipython3

    search_result = lk.search_targetpixelfile('TIC 307210830')
    search_result




.. raw:: html

    SearchResult containing 7 data products.
    
    <table id="table140331758223544">
    <thead><tr><th>#</th><th>observation</th><th>author</th><th>target_name</th><th>productFilename</th><th>distance</th></tr></thead>
    <tr><td>0</td><td>TESS Sector 2</td><td>SPOC</td><td>307210830</td><td>tess2018234235059-s0002-0000000307210830-0121-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>1</td><td>TESS Sector 5</td><td>SPOC</td><td>307210830</td><td>tess2018319095959-s0005-0000000307210830-0125-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>2</td><td>TESS Sector 8</td><td>SPOC</td><td>307210830</td><td>tess2019032160000-s0008-0000000307210830-0136-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>3</td><td>TESS Sector 9</td><td>SPOC</td><td>307210830</td><td>tess2019058134432-s0009-0000000307210830-0139-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>4</td><td>TESS Sector 10</td><td>SPOC</td><td>307210830</td><td>tess2019085135100-s0010-0000000307210830-0140-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>5</td><td>TESS Sector 11</td><td>SPOC</td><td>307210830</td><td>tess2019112060037-s0011-0000000307210830-0143-s_tp.fits</td><td>0.0</td></tr>
    <tr><td>6</td><td>TESS Sector 12</td><td>SPOC</td><td>307210830</td><td>tess2019140104343-s0012-0000000307210830-0144-s_tp.fits</td><td>0.0</td></tr>
    </table>



Lets pick and download the data for sector 2.

.. code:: ipython3

    tpf_file = search_result[0].download()
    tpf_file




.. parsed-literal::

    TessTargetPixelFile(TICID: 307210830)



We now have a TPF file for our object in sector 2. The optimal aperture
is stored in the TPF as the ``pipeline_mask`` property. We can have a
look at it by calling it here:

.. code:: ipython3

    tpf_file.pipeline_mask




.. parsed-literal::

    array([[False, False, False, False, False, False, False, False, False,
            False, False],
           [False, False, False, False, False, False, False, False, False,
            False, False],
           [False, False, False, False, False, False, False, False, False,
            False, False],
           [False, False, False, False, False, False, False, False, False,
            False, False],
           [False, False, False, False, False, False, False, False, False,
            False, False],
           [False, False, False, False,  True,  True,  True, False, False,
            False, False],
           [False, False, False, False,  True,  True,  True,  True, False,
            False, False],
           [False, False, False, False,  True,  True,  True,  True, False,
            False, False],
           [False, False, False, False, False,  True,  True, False, False,
            False, False],
           [False, False, False, False, False, False, False, False, False,
            False, False],
           [False, False, False, False, False, False, False, False, False,
            False, False]])



As you can see, it is a boolean array detailing which pixels are
included. We can plot this aperture over the top of our TPF using the
``plot()`` function, and passing in the mask to the ``aperture_mask``
keyword.

.. code:: ipython3

    tpf_file.plot(aperture_mask=tpf_file.pipeline_mask);



.. image:: images/Aperture-Photometry_files/Aperture-Photometry_13_0.png


We now see the SPOC *optimal* aperture mask overlaid on top of our
object of interest.

Using the provided optimal aperture in ``pipeline_mask`` and the TPF we
can perform simple aperture photometry via the
`extract_aperture_photometry <https://docs.lightkurve.org/api/lightkurve.targetpixelfile.TessTargetPixelFile.html#lightkurve.targetpixelfile.TessTargetPixelFile.extract_aperture_photometry>`__
function as shown below,

.. code:: ipython3

    lc = tpf_file.extract_aperture_photometry()
    lc




.. raw:: html

    <i>TessLightCurve targetid=307210830 length=18317</i>
    <table id="table140331223478512" class="table-striped table-bordered table-condensed">
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



The same result can also be obtained via,

::

   lc = tpf_file.to_lightcurve(aperture_mask=tpf_file.pipeline_mask)

Creating your own masks
-----------------------

You don’t necessarily have to pass in the ``pipeline_mask`` to the
``plot()`` function, it can be any mask you choose yourself, provided it
is the right shape. We will now explain how to adjust this mask using
the
`create_threshold_mask <https://docs.lightkurve.org/api/lightkurve.targetpixelfile.TessTargetPixelFile.html?highlight=create_threshold_mask#lightkurve.targetpixelfile.TessTargetPixelFile.create_threshold_mask>`__
function. This method will identify the pixels in the TPF which show a
median flux that is brighter than threshold times the standard deviation
above the overall median. The standard deviation is estimated in a
robust way by multiplying the Median Absolute Deviation (MAD) with
1.4826. In this example we will pick 10 as our threshold.

.. code:: ipython3

    target_mask = tpf_file.create_threshold_mask(threshold=10, reference_pixel='center')
    n_target_pixels = target_mask.sum()
    n_target_pixels




.. parsed-literal::

    13



We have now created a target mask which covers 13 pixels. Lets plot this
up and see what it looks like.

.. code:: ipython3

    tpf_file.plot(aperture_mask=target_mask, mask_color='r');



.. image:: images/Aperture-Photometry_files/Aperture-Photometry_21_0.png


We see that this is slightly different to the *optimal* aperture
previously defined. It also looks like there might be too many
background pixels included. Lets see if we can adjust this.

Specify an aperture array
~~~~~~~~~~~~~~~~~~~~~~~~~

We need to define a new aperture array such that our aperture will cover
our object of interest only. We have seen that apertures are defined
within boolean arrays, based on this lets make up a new array.

.. code:: ipython3

    aper_new = np.zeros(tpf_file.shape[1:], dtype=bool)
    aper_new[5:8, 4:7] = True
    tpf_file.plot(aperture_mask=aper_new, mask_color='red')




.. parsed-literal::

    <matplotlib.axes._subplots.AxesSubplot at 0x7fa1790b85c0>




.. image:: images/Aperture-Photometry_files/Aperture-Photometry_24_1.png


OK great, it looks like we have covered our object,but not included too
much background. Lets now make this into a light curve.

.. code:: ipython3

    target_lc_new = tpf_file.to_lightcurve(aperture_mask=aper_new)
    target_lc_new




.. raw:: html

    <i>TessLightCurve targetid=307210830 length=18317</i>
    <table id="table140331496638336" class="table-striped table-bordered table-condensed">
    <thead><tr><th>time</th><th>flux</th><th>flux_err</th><th>centroid_col</th><th>centroid_row</th><th>cadenceno</th><th>quality</th></tr></thead>
    <thead><tr><th></th><th>electron / s</th><th>electron / s</th><th>pix</th><th>pix</th><th></th><th></th></tr></thead>
    <thead><tr><th>object</th><th>float32</th><th>float32</th><th>float64</th><th>float64</th><th>int32</th><th>int32</th></tr></thead>
    <tr><td>1354.1088231272427</td><td>20049.26953125</td><td>15.38568115234375</td><td>664.5377949438838</td><td>339.37615072204693</td><td>91191</td><td>0</td></tr>
    <tr><td>1354.1102119888994</td><td>20029.6015625</td><td>15.380707740783691</td><td>664.5539189658597</td><td>339.3674922369538</td><td>91192</td><td>0</td></tr>
    <tr><td>1354.112989712153</td><td>19982.47265625</td><td>15.365057945251465</td><td>664.5351012281784</td><td>339.36145689194564</td><td>91194</td><td>0</td></tr>
    <tr><td>1354.1143785738097</td><td>19994.115234375</td><td>15.368595123291016</td><td>664.5664578479</td><td>339.38061605675574</td><td>91195</td><td>0</td></tr>
    <tr><td>1354.1157674355243</td><td>20003.728515625</td><td>15.371517181396484</td><td>664.5610361707227</td><td>339.37135598634495</td><td>91196</td><td>0</td></tr>
    <tr><td>1354.1171562971804</td><td>19999.60546875</td><td>15.368359565734863</td><td>664.5594608485563</td><td>339.3702259541033</td><td>91197</td><td>0</td></tr>
    <tr><td>1354.1185451588947</td><td>20019.8046875</td><td>15.375614166259766</td><td>664.5527183393958</td><td>339.3662359200094</td><td>91198</td><td>0</td></tr>
    <tr><td>1354.1199340205515</td><td>19982.787109375</td><td>15.361979484558105</td><td>664.5567752197887</td><td>339.36859919546725</td><td>91199</td><td>0</td></tr>
    <tr><td>1354.1213228822667</td><td>20002.78515625</td><td>15.369135856628418</td><td>664.5538246562905</td><td>339.3650181579328</td><td>91200</td><td>0</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>1381.5001032523294</td><td>19974.763671875</td><td>15.560335159301758</td><td>664.5105008707154</td><td>339.2613672501821</td><td>110913</td><td>0</td></tr>
    <tr><td>1381.5014921207378</td><td>19988.509765625</td><td>15.56753158569336</td><td>664.5151411160459</td><td>339.25840629283164</td><td>110914</td><td>0</td></tr>
    <tr><td>1381.5028809891458</td><td>19959.5</td><td>15.55550765991211</td><td>664.5136800320821</td><td>339.2605986305007</td><td>110915</td><td>0</td></tr>
    <tr><td>1381.5042698574382</td><td>19942.931640625</td><td>15.547529220581055</td><td>664.5087002343405</td><td>339.2654600563855</td><td>110916</td><td>0</td></tr>
    <tr><td>1381.5056587258466</td><td>19961.890625</td><td>15.553683280944824</td><td>664.514156119857</td><td>339.2574522478159</td><td>110917</td><td>0</td></tr>
    <tr><td>1381.5070475942555</td><td>19938.53515625</td><td>15.542488098144531</td><td>664.5135819475233</td><td>339.25510331494837</td><td>110918</td><td>0</td></tr>
    <tr><td>1381.508436462548</td><td>19942.68359375</td><td>15.544118881225586</td><td>664.513915654913</td><td>339.25242635657816</td><td>110919</td><td>0</td></tr>
    <tr><td>1381.5098253309563</td><td>19965.841796875</td><td>15.549737930297852</td><td>664.5082952466375</td><td>339.2615657982662</td><td>110920</td><td>0</td></tr>
    <tr><td>1381.5112141992488</td><td>19945.671875</td><td>15.542808532714844</td><td>664.5173951664624</td><td>339.25568362598784</td><td>110921</td><td>0</td></tr>
    <tr><td>1381.5126030676577</td><td>19982.890625</td><td>15.55328369140625</td><td>664.5085713660441</td><td>339.2605124583506</td><td>110922</td><td>0</td></tr>
    </table>



Compare data & light curves
---------------------------

We have now created light curve objects using both the SPOC pre-defined
aperture and a mask of our own devising. Lets plot these light curves up
and examine the difference.

.. code:: ipython3

    lc.plot();



.. image:: images/Aperture-Photometry_files/Aperture-Photometry_29_0.png


.. code:: ipython3

    target_lc_new.plot();



.. image:: images/Aperture-Photometry_files/Aperture-Photometry_30_0.png


As you can see the light curves from the two apertures look very
different. It looks as if the aperture we have defined manually may have
less background or contaminating flux from scattered than the SPOC
aperture. We will learn more about contamination in our `next
tutorial <Visual-inspection-Tutorial.html>`__.
