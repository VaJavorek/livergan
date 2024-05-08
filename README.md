# livergan - Image Domain Transfer for Liver Analysis in Histology

Using GANs to transform the domain of large microscopic liver images obtained from live samples into a different domain that represents decellularized liver tissue.

<img src="/img/examples/default_A1.png" width="400"/> <img src="/img/examples/default_A2.png" width="400"/> 
<img src="/img/examples/default_B1.png" width="400"/> <img src="/img/examples/default_B2.png" width="400"/>

By erasing this domain gap, we can overcome some of the constraints of liver tissue analysis and unlock new possibilities for comprehensive image-based studies, for example, using proven analysis tools from the [scaffan](https://github.com/mjirik/scaffan) library in the desired domain and comparing the results of given selected metric with comparable data. This allows further higher quality evaluation of the sample.

<img src='img/fade.gif' width=800>

## About

This is a repository for a master's thesis work, developed by [Václav Javorek](https://github.com/vjavorek) under the supervision of [Miroslav Jiřík](https://github.com/mjirik).

**AtoB** = Decellularized to live domain transfer

**BtoA** = Live to decellularized domain transfer

## Demo examples
Example [colab](https://colab.research.google.com/drive/1t37bkfKHP6NpLtD5jlUkbahKO65xXX0P?usp=sharing) - transformation inference

Example [colab](https://colab.research.google.com/drive/1DDdi8x68rShRWBMQPJ9aq9zxtGmUsFqM?usp=sharing) - splitting, processing and merging back a whole slide (.czi) image

## Models comparison

AtoB

<img src="/img/comparison/Comparison_PIG-002_J-18-0092_HE__-1_split_1200.png" width="400"/> <img src="/img/comparison/Comparison_PIG-002_J-18-0092_HE__-1_split_1254.png" width="400"/> 

BtoA

<img src="/img/comparison/Comparison_J10_3_a_split_822.png" width="400"/> <img src="/img/comparison/Comparison_J10_3_c_split_1119.png" width="400"/> 

## FID scoring of different models

<img src="/img/FID.jpg" width="300"/>

## Merging examples

AtoB + post-processing

<img src="/img/merging/PIG-002_J-18-0092_HE__-1.png" width="260"/> <img src="/img/merging/PIG-002_J-18-0092_HE__-1_fullres2A.png" width="260"/> <img src="/img/merging/PIG-002_J-18-0092_HE__-1_fullres2A_pp.png" width="260"/>

BtoA + post-processing

<img src="/img/merging/J18_6_d.png" width="260"/> <img src="/img/merging/J18_6_d_fullres7B.png" width="260"/> <img src="/img/merging/J18_6_d_fullres7B_pp10.png" width="260"/>
