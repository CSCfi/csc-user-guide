# Using LLM models with Ollama in SD Desktop.


[Ollama](https://ollama.com/) is a popular tool for using LLMs, as it supports several state-of-the-art models which can be accessed via an API. 
Ollama can be used in  SD Desktop too.  Be default Ollama downloads the LLM modes from public repostories in internet.  
This is however not possible in SD Donnect. Because of that you must download the models somewhere and then import the modes 
to SD Desktop via SD Connect.

This tutorial provides example how a LLM model can be first downloaded to [Roihu supercomputer](../../../support/tutorials/roihu.md) 
at CSC and then imported to SD Desktop.

## Step 1. Downloading models to Roihu

First open login to [Roihu web interface](https://www.roihu.csc.fi/public/) and open a Login node shell in Roihu CPU. In the shell session
move to the scratch directry of your project.

```txt
cd /scractch/project_200xxxx/
```
Make a directory for Ollama and install it there:

```txt
mkdir ollama
cd ollama
wget https://ollama.com/download/ollama-linux-amd64.tar.zst
tar -xf ollama-linux-amd64.tar.zst
rm ollama-linux-amd64.tar.zst
export PATH=$PWD/bin:$PATH
```
Then make a directory for the LLM models and define OLLAMA_MODELS environment variable to point to that directory.

```txt
mkdir ollama_models
export OLLAMA_MODELS=$PWD/ollama_models
```

Then, start ollama service with command:
```txt
ollama serve &
```

Next download ollama models you need either using the LLM repository names or by downloading and importing the gguf files.

```txt
ollama pull llama3.1:8b

wget https://huggingface.co/mradermacher/Ahma-2-4B-Instruct-GGUF/resolve/main/Ahma-2-4B-Instruct.Q4_K_M.gguf
ollama create Ahma-2-4B-Instruct.Q4_K_M.gguf
```

The downloded models are now stored to ollama_models directory. Next we pack the directory into a tar file for transport:

```txt
tar cvf ollama_models.tar ollama_models
```

After that you need to acivate connection to SD Connect service and upload the tar package to SD Connect.
(repace 200xxxx with your project number)

```txt
module load allas
allas-conf –sdc
a-put –sdc ollama_models.tar -b 200xxxx-ollama
```

## Step 2. Using Ollama in SD Desktop

Ollama can be installed to SD Desktop virtual machines using the [SD Tool Installer](../sd-desktop-software.md#41-using-the-software-installer). 
Open DataGateway connection to SD Connect, open the SD Tool Installer and press *Ollama* button. 

In addition to the Ollama software, you need the LLM models that were uploaded to SD Connect 
in the previous step. As the models can require significant amout of storage space your 
should download them to the volume disc. Open a terminal in yor SD Desktop machine and give commands:

```txt
cd /media/volume
tar xvf $HOME/Projects/SD-Connect/*/20*-ollama/ollama_models.tar
```
Once the LLMs have been downloaded, set OLLAMA_MODELS environment variable to point to your *ollama_models* directory:

```txt
export OLLAMA_MODELS=/media/volume/ollama_models
```

Now you are ready to use Ollama. First start Ollama server

```txt
ollama serve > ollama-server-log  2>&1 &
```

After that you can list the available LLMs and test that they work:

```txt
ollama list
ollama run llama3.1:8b  “Describe shortly the main features llama3.1 langue model.”
```

While the Ollama server is running in your SD Desktop machine, you can use it from any terminal session. 
In addition you can use Ollama with Python scripts.  Ollama pythion library is not available in the default 
Python of SD Desktop, but it is included for example in _python3-for-medimaging_ python environment that can be installed 
with [auto-apptainer](./auto-apptainer.md):

```txt
auto-apptainer python3-for-medimaging
```

Sample Python script:

```
import ollama

#read input file 
file = open (“/media/volume/interview1.txt”, “r”)
content=file.read()

#define prompt for Ollama
myprompt = f”Replace names of persons with letter X in following text:\n\”\”\”\n{content}\n\”\”\””

#execute the prompt with Ollama
result = ollama.generate(model=’llama3.1:8b’, prompt=myprompt)

#write the results into file
anonymized = open(“/media/volume/interview1_anonymized.txt”, “w”)
anonymized.write(result[‘response’])
anonymized.close
```
