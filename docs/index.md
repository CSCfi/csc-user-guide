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
