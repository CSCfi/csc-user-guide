---
template: main-index.html
---


## Mathjax

\[
\frac{3\times x +y}{\sum_{i=0}^{10} o_i}
\]

## Details

??? success "I'm hiding some content"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

## Custom Admonitions

!!! mahti "Mahti supercomputer"
    Mahti has many AMD cores, while Puhti is using intel.

## Tabbing

### MPI

=== "Mahti"
    ```
    #!/bin/bash
    #SBATCH --job-name=example
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=02:00:00
    #SBATCH --nodes=10
    #SBATCH --ntasks-per-node=128

    srun myprog <options>

    ```
=== "Puhti"
    ```
    #!/bin/bash
    #SBATCH --job-name=example
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=02:00:00
    #SBATCH --ntasks=80
    #SBATCH --mem-per-cpu=4000

    srun myprog <options>
    ```

## Simple raw Javascript
<form >
<label for="n1">Number A:</label>
<input type="number" id="n1" style="border:3px solid " name="num">
<br>
<label for="n2">Number B:</label>
<input type="number" id="n2" style="border:3px solid " name="num">
<br>
<br>
<input type="button" onclick="myAdder()" style="border:3px solid " value="Add">
</form>

<script>
function myAdder(){
   var n1 = document.getElementById("n1").value;
   var n2 = document.getElementById("n2").value;
   var res= +n1 + +n2;
   document.getElementById("ans").innerHTML = res;
}
</script>
<br>
The Answer is: <p id="ans"></p>



## Complicated external package

<script type="text/javascript" src="javascripts/jsxgraphcore.js"></script>

<div id="box" class="jxgbox" style="width:500px; height:500px;"></div>
<script type="text/javascript">
var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-10, 10, 10, -10]});
var a = board.create('slider', [[1,8],[5,8],[0,1,4]],{name:'a'});
var b = board.create('slider', [[1,9],[5,9],[0,0.25,4]],{name:'b'});

var c = board.create('curve', [function(phi){return a.Value()+b.Value()*phi; }, [0, 0],0, 8*Math.PI],
             {curveType:'polar', strokewidth:4});      

var g = board.create('glider', [c]);
var t = board.create('tangent', [g], {dash:2,strokeColor:'#a612a9'});
var n = board.create('normal', [g], {dash:2,strokeColor:'#a612a9'});
</script>

## Batch script "Wizard"

<script>
function hideMahtiP(){
 var x = document.getElementById("partitions_mahti");
 var y = document.getElementById("partitions_puhti");
 x.style.display = "none";
 y.style.display = "block";
}
function hidePuhtiP(){
 var x = document.getElementById("partitions_mahti");
 var y = document.getElementById("partitions_puhti");
 x.style.display = "block";
 y.style.display = "none";
}
</script>


**System:**
<form id=system_form>
  <input type="radio" id="puhti" name="system" value="puhti" onclick="hideMahtiP();" checked=checked>
  <label for="puhti">Puhti</label>
  <input type="radio" id="mahti" name="system" value="mahti" onclick="hidePuhtiP();">
  <label for="mahti">Mahti</label><br>
</form>

**Partition:**
<form  id=partitions_puhti>
<select name="partition" id="partitions_p">
  <option value="test">test</option>
  <option value="small">small</option>
  <option value="large">large</option>
  <option value="longrun">longrun</option>
  <option value="hugemem">hugemem</option>
</select>
</form>

<form hidden id="partitions_mahti">
<select name="partition" id="partitions_m">
  <option value="test">test</option>
  <option value="medium">medium</option>
  <option value="large">large</option>
  <option value="gc">gc</option>
  <option value="hugemem">hugemem</option>
</select>    
</form>

**Number of tasks**
<input type="number" id="core_s" style="border:3px solid " >

**Duration**
<input type="text" id="time" style="border:3px solid " >

**Project**
<input type="text" id="project" style="border:3px solid " >

<input type="button" onclick="GenerateBatch()" style="border:3px solid " value="Generate">
<script>
function GenerateBatch(){
var radios = document.getElementsByName('system');
var partition=""

for (var i = 0, length = radios.length; i < length; i++) {
  if (radios[i].checked) {
    if(radios[i].value == "mahti"){
        partition=document.getElementById("partitions_m").value
    }
    else if(radios[i].value == "puhti"){
        partition=document.getElementById("partitions_p").value
    }

  break;
  }
}
 var str="#!/bin/bash"
 str+= "\n#SBATCH --partition="
 str+= partition
 str+= "\n#SBATCH --time=" + document.getElementById("time").value
 str+= "\n#SBATCH --account=" + document.getElementById("project").value
 str+= "\n#SBATCH --ntasks=" + document.getElementById("core_s").value
document.getElementById("batch_code").innerHTML = str;
}

</script>

<div class="tabbed-content">
<div class="highlight" style="background-color:#ddd;"><pre id="wizard"><span></span><button class="md-clipboard" title="Copy to clipboard" data-clipboard-target="#wizard pre, #wizard code"><span class="md-clipboard__message"></span></button><code id=batch_code>
</code></pre></div>
</div>

