# Virtual machine flavors and billing unit rates

This article lists the types (flavors) of virtual machines and their
cost in billing units. Normally billing units are not invoiced for
academic use, learn more in here LINKTOBEADDED.

[TOC]

## Virtual machine flavors and Billing Unit rates

The cPouta and ePouta services consume  the same billing units as Sisu
and  Taito. You  can  find  more information  in  the  [CSC  Computing
environment user guide].

Users can  create virtual  machines with  larger compute  resources or
smaller   resources    based   upon    their   needs.    The   Virtual
Machine *flavors* available in cPouta and ePouta are listed below in
separate tables.

**Table**  Available virtual machine  flavors  in cPouta and their
Billing Unit coefficients. Note that the default  cPouta  user account
allows users to launch only a subset of the available virtual machine 
flavors . 

**New prices  starting from 18.03.2019.  The prices  before 18.03.2019
are shown in parentheses.**

!!! warning
    Vanhat taulukot on liian monimutkaisia markdownille. Noi vois purkaa osiin,
    otsikoida makuperheillä ja silleen. Vaikka miten formatoi, niin ei silti
    mahdu palstaan, mutta uskon että parempi useana omana taulukkona, kuin yhtenä
    jättitaulukkona.

!!! note
    Kannattaa vilkaista myös sorsaa - markdown on huomattavasti siistimpää
    noin niinkuin ylläpidon kannalta. Ellei sitten joudu joka tapauksessa
    käyttämään jotain pulautinta.

### cPouta Flavors
#### Standard flavors (with markdown syntax)


|Flavor|Cores|Memory <br/>(* GiB)|Disk <br/>(root)<br/>GB|Disk <br/>(ephemeral)<br/>GB|Disk <br/>(total)<br/>GB|Memory/<br/> core <br/>(* GiB)|Billing<br/> Units<br/>/h|
|--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|standard.tiny|1|1|80|0 |80 |1|0.25 (0.5)|
|standard.small|2|2|80 |0 |80 |1|0.5 (1)|
|standard.medium|3|4|80|0 |80 |1.3|1 (2)|
|standard.large|4|8|80 |0 |80 |2|2 (4)|
|standard.xlarge|6|16|80|0|80 |2.6|4 (8)|
|standard.xxlarge|8|32|80 |0 |80 |4|8 (16)|

##### sama html:nä

<table>
	<tbody>
		<tr>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><b>Flavor</b></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Cores</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (root)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (ephemeral)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (total)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory/<br/> core<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Billing Units/h</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.tiny</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0.25 (0.5)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.small</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0.5 (1)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.medium</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1.3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1 (2)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.large</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2 (4)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.xlarge</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">6</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">16</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2.6</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4 (8)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.xxlarge</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">32</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8 (16)</td>
		</tr>
		<tr>
</table>

## alkuperäinen taulu suoraan html:nä

<table border="1" height="1010" width="600">
	<tbody>
		<tr>
			<td colspan="12" style="background-color: rgb(204, 204, 255); text-align: center;"><span style="font-size:22px;"><strong>cPouta Flavors</strong></span></td>
		</tr>
		<tr>
			<td colspan="8" style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Standard flavors</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><b>Flavor</b></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Cores</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (root)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (ephemeral)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (total)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory/<br/> core<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Billing Units/h</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.tiny</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0.25 (0.5)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.small</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0.5 (1)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.medium</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1.3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1 (2)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.large</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2 (4)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.xlarge</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">6</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">16</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2.6</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4 (8)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>standard.xxlarge</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">32</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8 (16)</td>
		</tr>
		<tr>
			<td colspan="8" style="background-color: rgb(204, 204, 255); text-align: center;"><strong>HPC flavors</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><b>Flavor</b></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Cores</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (root)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (ephemeral)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (total)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory/<br/>core<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Billing Units/h</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc.4.5core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">22</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4.3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">6 (10)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc.4.10core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">10</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">43</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4.3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">12 (20)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc.4.20core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">20</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">86</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4.3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">25 (40)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc.4.40core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">40</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">172</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4.3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">50 (80)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc.4.80core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">344</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4.3</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">100 (160)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen2.24core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">24</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">120</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">30 (45)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen2.48core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">48</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">240</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">60 (90)</td>
		</tr>
		<tr>
			<td colspan="8" style="background-color: rgb(204, 204, 255); text-align: center;"><strong>I/O flavors</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><b>Flavor</b></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Cores</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (root)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (ephemeral)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (total)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory/<br/>core<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Billing Units/h</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>io.70GB</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">10</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">20 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">70 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">90 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3 (5)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>io.160GB</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">20</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">20 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">160 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">180 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">6 (10)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>io.340GB</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">40</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">20 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">340 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">360 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">12 (20)</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>io.700GB</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">16</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">20 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">700 GB<br />
			(SSD/RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">720 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">24 (40)</td>
		</tr>
		<tr>
			<td colspan="8" style="background-color: rgb(204, 204, 255); text-align: center;"><strong>GPU flavors</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><b>Flavor</b></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Cores</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>GPUs</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (root)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (total)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory/<br/>core<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Billing Units/h</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>gpu.1.1gpu</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">14</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">120</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (SSD/RAID1)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8.5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">60</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>gpu.1.2gpu</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">28</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">240</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (SSD/RAID1)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8.5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">120</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>gpu.1.4gpu</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">56</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">480</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (SSD/RAID1)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8.5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">240</td>
		</tr>
		<tr>
			<td colspan="8" style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Deprecated flavors</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><b style="background-color: rgb(204, 204, 255);">Flavor</b></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Cores</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (root)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (ephemeral)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Disk (total)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Memory/<br/>core<br />
			(* GiB)</strong></td>
			<td style="background-color: rgb(204, 204, 255); text-align: center;"><strong>Billing Units/h</strong></td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen1.1core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">1</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3.7</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3.7</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen1.4core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">15</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3.7</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen1.8core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">30</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3.7</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">16</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen1.16core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">16</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">60</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">3.7</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">32</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen2.2core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">2</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">10</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">4</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen2.8core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">8</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">40</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">15</td>
		</tr>
		<tr>
			<td style="background-color: rgb(255, 255, 255); text-align: center;"><strong>hpc-gen2.16core</strong></td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">16</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB (RAID0)</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">0 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">80 GB</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">5</td>
			<td style="background-color: rgb(255, 255, 255); text-align: center;">30</td>
		</tr>
		<tr>
			<th>tiny</th>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">10 GB (RAID0)</td>
			<td style="text-align: center;">110 GB (RAID0)</td>
			<td style="text-align: center;">120 GB</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<th>mini</th>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">3.5</td>
			<td style="text-align: center;">10 GB (RAID0)</td>
			<td style="text-align: center;">110 GB (RAID0)</td>
			<td style="text-align: center;">120 GB</td>
			<td style="text-align: center;">1.7</td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<th>small</th>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">10 GB (RAID0)</td>
			<td style="text-align: center;">220 GB (RAID0)</td>
			<td style="text-align: center;">230 GB</td>
			<td style="text-align: center;">3.8</td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<th>medium</th>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">30</td>
			<td style="text-align: center;">10 GB (RAID0)</td>
			<td style="text-align: center;">440 GB (RAID0)</td>
			<td style="text-align: center;">450 GB</td>
			<td style="text-align: center;">3.8</td>
			<td style="text-align: center;">16</td>
		</tr>
		<tr>
			<th>large</th>
			<td style="text-align: center;">12</td>
			<td style="text-align: center;">45</td>
			<td style="text-align: center;">10 GB (RAID0)</td>
			<td style="text-align: center;">660 GB (RAID0)</td>
			<td style="text-align: center;">670 GB</td>
			<td style="text-align: center;">3.8</td>
			<td style="text-align: center;">24</td>
		</tr>
		<tr>
			<th>fullnode</th>
			<td style="text-align: center;">16</td>
			<td style="text-align: center;">60</td>
			<td style="text-align: center;">10 GB (RAID0)</td>
			<td style="text-align: center;">900 GB (RAID0)</td>
			<td style="text-align: center;">910 GB</td>
			<td style="text-align: center;">3.8</td>
			<td style="text-align: center;">32</td>
		</tr>
	</tbody>
</table>


TABLE TOO COMPLICATED FOR markdown format
  
**\*** Not all memory amounts round  exactly to GiB, the closest value
has been used.

TABLE TOO COMPLICATED FOR markdown format

**Table**  Available virtual  machine flavors in ePouta  and their
Billing Unit coefficients.
  
**\*** Not all memory amounts round  exactly to GiB, the closest value
has been used.

Please  note: The flavors in the two tables are slightly different.
This is  because
different hardware  is used in  these two  clouds. Any storage  with a
comment  in  parenthesis such  as  (SSD/RAID0)  means that  particular
storage is  local to the compute  node. In ePouta, the  HPC root disks
and  standalone  volumes are  hosted  in  the centralized  Ceph  block
storage system.

### Which type of flavor should I use?

#### **Standard flavors**

Typical use cases:

-   Web services (non-HPC)
-   Software development

These  are generic  flavors that  are useful  for running  regular web
services  like a  web server  with a  database backend  or some  other
relatively light  usage. They provide better  availability compared to
HPC flavors.

Cloud administrators  can move  these virtual  machines from  one host
machine to another without causing a break in service. This means that
you are likely less impacted by maintenance.

These  flavors   are  not   suitable  for   computationally  intensive
workloads.    The   virtual  CPUs   used   in   these  instances   are
overcommitted,  which means  32 hyperthreaded  CPU cores  are used  to
provide more than 32 virtual cores.

** Flavor characteristics:**

-   Redundant power
-   CPU: Varies
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored on central storage
-   Single node or disk failures may cause downtime, but your instance
    is recoverable.

#### **HPC flavors**

Typical use cases:

-   Scientific applications

If your use  case is computationally intensive, you should  use one of
the HPC flavors.  The availability for these instances is  not as high
as with the standard flavors, but  you get better performance. The HPC
flavors have faster CPUs and no overcommitment of CPU cores.

**cPouta HPC flavor characteristics:**

**hpc.4.\*:**

-   Not redundant power
-      CPU:   Intel(R)    Xeon(R)   Gold    6148   CPU    @   2.40GHz,
    ***hyper-threading***
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored on central storage
-   Single node or disk failures may cause downtime, but your instance
    is recoverable.

**hpc-gen2.\*:**

-   No redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Single 40 Gb/s
-   Flavor disk: Local SATA disk, no RAID
-   Your instance can be lost due to a single node or disk failure.

**ePouta HPC flavor characteristics:**

**hpc.4\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU Gold 6148, with hyper-threading
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored on central storage
-   Single node or disk failures may cause downtime, but your instance
    is recoverable.

**hpc.3\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading
-   Network: Redundant 25 Gb/s
-   Flavor disk: Stored on central storage
-   Single node or disk failures may cause downtime, but your instance
    is recoverable.

**hpc.\*.haswell:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2690 v3, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Stored on central storage
-   Single node or disk failures may cause downtime, but your instance
    is recoverable.

#### **I/O flavors**

Typical use cases:

-   Hadoop/Spark
-   Non-critical centralized databases
-   Clustered databases

I/O flavors are intetended to give you the best I/O performance on the
virtual machine  root and  ephemeral disks. They  are backed  by local
SSDs on the servers  they run on. The SSDs are  configured in a RAID-0
configuration  for  maximal  performance.   This  means  there  is  an
increased  risk of  loss  of a  virtual machine  in  case of  hardware
problems.  The risk  of  disk  failure is  larger  than  on the  other
flavors, so  it's especially  important to  be aware  of the  risks of
data-loss on these flavors.

As these  instances are  also tightly  tied to  the hardware,  you may
expect  downtime  of instances  during  maintenance  of the  hardware.
Resize/migration functionality also does not work for these instances.
The bulk  of the storage is  available as an ephemeral  disk, normally
under /dev/vdb.

Often  you  want  to  create   clusters  of  servers  with  the  io.\*
flavors.  In  these cases  you  probably  want  to have  your  virtual
machines land on different physical servers. This can not currently be
done  in the  web  interface. To  achieve this,  please  refer to  the
anti-affinity group commands in our [command line instructions.]

The  availability for  these  instances is  not as  high  as with  the
standard   flavors,    but   you   get   significantly    better   I/O
performance.  Maintenance work  can cause  larger disruption,  and the
resize functionality does not work.

**cPouta IO flavor characteristics:**

**io.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Redundant 10 Gb/s or 40 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Your instance can be lost due to a single node or disk failure.

**ePouta IO flavor characteristics:**

**io.haswell.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v3, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Your instance can be lost due to a single node or disk failure.

#### GPU Flavors

Typical Usecases:

-   High Performance Compute applications leveraging GPUs
-   Machine and deep learning for ex. [TensorFlow]
-   Rendering

GPU flavors are intended to  give you high performance computing using
GPGPU   (General    Purpose   computing   on    Graphical   Processing
Units).  GPGPUs  can  significantly   speed  up  some  algorithms  and
applications. The  gpu.1.  flavors  in cPouta  have NVIDIA  Tesla P100
GPGPUs. The gpu.2.1gpu in ePouta have NVIDIA Tesla V100 GPGPU

The GPGPUs  are suitable  for deep  learning, scientific  computing as
well  as for  remote desktop,  rendering or  visualization. The  GPGPU
flavors are backed by local SSD on  the servers. The SSD in cPouta are
configured in RAID-1 and this is where  the OS root disk is stored. In
ePouta the SSD  are bigger than in cPouta and  the SSDs are configured
in RAID-0 for faster staging of  datasets. You can use the volumes for
storing larger data sets. If you need  to read and write a lot of data
between the disk and GPGPU, this might affect the performance.

To  take  advantage of  the  acceleration  which GPGPUs  provide,  the
applications you  run must have support  for using them. If  you write
your own  applications, the [Optimization  Service] can offer  help in
leveraging the GPGPUs.

We know GPGPUs can  be used for a lot of  cool and interesting things,
but please remember the resource usage  must comply with the [Terms of
Use].

Limitations & caveats: 

-    As  we use  PCI  passthrough  to get  the  whole  GPGPU into  the
    instance, the administrators are not  able to access the GPGPU and
    check its health. Please report errors or problems with the GPGPUs
    to CSC (and attach the output  of the command "nvidia-smi -q" when
    you do so).
-   Applications must be able to utilize the GPU to get a speedup.

These instances are also tightly tied  to the hardware, you may expect
downtime of instances  during maintenance of the  hardware. The NVIDIA
Tesla V100  GPGPU are  also available  in the  batch system  on Taito:
<https://research.csc.fi/taito-gpu>.

**cPouta flavor characteristics:**

**gpu.1.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU E5-2680 v4, with hyper-threading
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-1
-   Your instance can be lost due to a single node or disk failure.

**ePouta flavor characteristics:**

**gpu.2.\*:**

-   Only available via request to servicedesk@csc.fi
-   Redundant power
-   CPU: Intel(R) Xeon(R) Gold 6148, with hyper-threading
-   NUMA Aware: yes (CPU &lt;&gt; Memory, not PCI devices)
-   Network: Redundant 10 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Your instance can be lost due to a single node or disk failure.

#### Installation and configuration of GPU Flavors

We have  specific CUDA images  available for  use with the  GPU nodes.
These images come pre-installed with  the freshest CUDA version.  Note
that the CUDA images  are not configure with auto update.  One may use
any other images with the GPU flavors, but in this case, you will have
to install  the required libraries yourself.  If you want to  use your
own   images,[ https://research.csc.fi/pouta-adding-images] has   more
details about how CSC customizes the images.

#### High Memory Flavors (only in ePouta)

Typical use cases:

-   Scientific applications requiring large amounts of memory

These flavors have large amount of memory, and are meant for use cases
which require, and can utilize this amount of memory. Typical usecases
of  these flavors  include  scientific applications  with huge  memory
requirements for  example Gnome  sequencing and  analysis applications
etc.

Resize/migration functionality does not work for these instances.

If  you need  to move  a workload  from  another type  of VM  to a  TB
instance, either move  all data and install  all applications manually
to  the new  TB VM,  or create  a snapshot  from the  source VM.  Then
convert that  snapshot to a volume,  and use the volume  to create the
new TB flavor VM.

If you need to move a workload from a TB instance to another instance,
either move  all data and install  all applications manually to  a new
VM, or create a snapshot from  the source VM**. Please note** that all
ephemeral disk data will be lost in the process and will not be stored
in the snapshot, only the TB VM root disk.

**Flavor characteristics:**

**tb.3.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU  E5-2680 v4, with hyper-threading **or**
    Intel(R) Xeon(R) CPU E5-2698 v4, with hyper-threading
-   Network: Redundant 25 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Your instance can be lost due to a single node or disk failure.

**tb.4.\*:**

-   Redundant power
-   CPU: Intel(R) Xeon(R) CPU Gold 6148, with hyper-threading
-   Network: Redundant 25 Gb/s
-   Flavor disk: Local SSD disks, RAID-0
-   Your instance can be lost due to a single node or disk failure.

#### Deprecated flavors

This  is  the  set  of   original  flavors  that  has  been  available
since launch. **You should  not launch any new  virtual machines using
any  of these  flavors.  <span  style="color: rgb(0, 0, 0);">Existing
virtual   machines   that  use   these   flavors   will  continue   to
work. </span>**We will  maintain these flavors  for a period  of time,
but they will be removed at some point in the near future.

  [CSC Computing environment user guide]: https://research.csc.fi/csc-guide-projects-and-resource-allocation
  [command line instructions.]: https://research.csc.fi/pouta-client-usage
  [TensorFlow]: https://www.tensorflow.org
  [Optimization Service]: https://research.csc.fi/optimization-service
  [Terms of Use]: https://https://research.csc.fi/pouta-user-policy
  [https://research.csc.fi/pouta-adding-images]: https://,%20https://research.csc.fi/pouta-adding-images
