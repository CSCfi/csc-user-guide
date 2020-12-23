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
<label for="number">Number A:</label>
<input type="number" id="n1" name="num_1">
<br>
<label for="number">Number B:</label>
<input type="number" id="n2" name="num_2">
<br>
<br>
<input type="button" onclick="myAdder()" value="Add">
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

