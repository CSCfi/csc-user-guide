import re
import subprocess
import sys
def run_bash(command):
    command_as_list=command.split(" ")
    Output=subprocess.run(command_as_list,stdout=subprocess.PIPE,stderr=subprocess.PIPE)#,capture_output=True)
    return Output


class Docs:
    # To lazy to do a proper parsers for the options
    def __init__(self):
        self.working_dir="tests/python_link_tests/"
        self.input_files =4*[""]
        self.input_files[0]="links.txt"
        self.input_files[1]="files.txt"
        self.input_files[2]="headders.txt"
        self.input_files[3]="nav.txt"
        self.input_files  = list(map(lambda x: self.working_dir+x,self.input_files))
        self.bash_script_name=self.working_dir+"get_all_data.sh"
        self.files={}
        self.nav_links=[]
        self.whitelist=[]


        self.dump_data()
        self.parse_data()
        self.convert_site_to_doc_links()

    def dump_data(self):
        command = " ".join(["bash",self.bash_script_name]+self.input_files)  
        run_bash(command)

    def parse_data(self):

        # Parse file names
        with open(self.input_files[1]) as fp:
            for line in fp:
                
                line_stripped=line.strip()
                sep=line_stripped.rsplit('/',1)

                file_name=sep[1]
                file_path=sep[0]
                is_md= file_name[-3:]==".md"
                is_index = file_name =="index.md"

                self.files[line_stripped]=Doc_file(file_path,file_name,is_md,is_index)

        # Parse links
        with open(self.input_files[0]) as fp:
            for line in fp:
                line_stripped=line.strip()
                data=line_stripped.split(":")
                data=list(map(lambda x: x.strip() ,data ))
                source_file=self.files[data[0]]
                if(len(data)==4):
                    source_file.add_link(Internal_link(source_file,data[1],data[2],data[3]))
                else:
                    source_file.add_link(Internal_link(source_file,data[1],data[2]))
    
        # Parse links
        with open(self.input_files[3]) as fp:
            for line in fp:
                self.nav_links.append(line.strip())

        # Parse whitelist
        with open(self.working_dir+"whitelist") as fp:
            for line in fp:
                pars=line.strip()
                if(pars[0]!='#'):
                    self.whitelist.append(pars)

        


    def file_exists(self,file_path):
        return file_path in self.files

  
    def convert_site_to_doc_links(self):
        for fileo in self.files.values():
            for link in fileo.links:
                if(not link.file_link_is_broken):
                    file_path="docs/"+link.valid_site_target[5:]
                    if(link.link_file_target==""):
                        file_path=fileo.path+"/"+fileo.name
                    if(self.file_exists(file_path)):
                        link.valid_docs_target=file_path
                    else:
                        file_path=file_path[:-11]+".md"
                        if(self.file_exists(file_path)):
                            link.valid_docs_target=file_path
                        else:
                            file_path="docs/"+link.valid_site_target[5:]         
                            file_path=file_path[:-4]+"md"
                            if(self.file_exists(file_path)):
                                link.valid_docs_target=file_path
                            

    def list_of_file_links(self):
        return [link.valid_docs_target for fileo in self.files.values() for link in fileo.links]


    def report_hidden_files(self):
        file_links=self.list_of_file_links()
        output=""
        for filo in self.files.values():
            file_path=filo.path+"/"+filo.name
            if(file_path not in file_links and file_path not in self.nav_links and filo.is_markdown_file and file_path not in self.whitelist):
                output+= filo.path+"/"+filo.name + "\n"

        if(output!=""):
            output="The following files have no links pointing to them and are not whitelisted:\n"+output
            return(1,output[:-1])
        else:
            output="No hidden files found"
            return (0,output) 

    def report_broken_file_links(self):
        output=""
        for fileo in self.files.values():
            for link in fileo.links:
                if(link.file_link_is_broken):
                    output+="The file link " +link.link_file_target+" in file "+fileo.path+"/"+fileo.name +" on line " +link.line_number+ " is broken\n"


        if(output==""):
            return(0,"No broken file links found")
        else:
            return(1,output[:-1])

    def report_broken_section_links(self):
        output=""
        for fileo in self.files.values():
            for link in fileo.links:
                if(link.link_section_target!="" and not link.file_link_is_broken):
                    command="grep -- " +"\"" + link.link_section_target  +  "\"" +" " + link.valid_site_target 
                    grep_res=run_bash(command)
                    if(grep_res.returncode!=0):
                        output+="The section link " +link.link_file_target+"#" +link.link_section_target+ " in file "+fileo.path+"/"+fileo.name +" on line " +link.line_number+ " is broken\n"
                    


        if(output==""):
            return(0,"No broken section links found")

        else:
            return(1,output[:-1])



class Internal_link:
    def __init__(self,f,ln,ft,st=""):
        self.source_file=f
        self.line_number=ln
        self.link_file_target=ft
        self.link_section_target=st
        # Default value is True
        self.file_link_is_broken=True
        self.valid_site_target=""
        self.valid_docs_target=""
        
        # No file target, so the link must point to
        # a section in the same file (which must be .md)
       
        if(ft=="" and st==""):
            return

        if(ft==""):
            self.link_file_target=self.source_file.name

        self.is_absolute= self.link_file_target[0]=='/'         
        self.ends_with_md=self.link_file_target[-3:]==".md"
        self.source_is_index=self.source_file.is_index_file
        self.target_is_index= self.link_file_target[-8:]=="index.md"
        self.has_file_ending=re.search("\.[A-Z,a-z,0-9]*$",ft) !=None
        self.has_other_ending=(self.has_file_ending and not self.ends_with_md)
        source=""
        target=""

        source=self.source_file.path
        source="site/"+source[5:]

        # Check that the md file exists
        if(self.ends_with_md):
            if(self.is_absolute):
                path_to_md="docs/"+ft
            else:
                path_to_md=f.path+"/"+ft 
            command="readlink -ev -- " +path_to_md
            res=run_bash(command)
            if(res.returncode==1):
                return
            



        if(not self.source_is_index):
            target="../"+target
            source=source+"/"+self.source_file.name
            source=source[:-3]+"/"

        if(not self.has_file_ending and ft!=""):
            target=""

        if(self.is_absolute):
            source="site/"
            target=self.link_file_target
            
            if(not self.has_other_ending):
                target=target+"/index.html"

        else:
            target=target+self.link_file_target
            if(self.ends_with_md):
                target=target[:-3]
           
            if(self.target_is_index):
               target=target[:-5]

            if(not self.has_other_ending):
                target=target +"/index.html"


        path_to_check=source+"/"+target 
        




        command="readlink -ev -- " +path_to_check
        res=run_bash(command)
        if(res.returncode==0):
            self.file_link_is_broken=False

            abs_path_len=len(run_bash("pwd").stdout)

            self.valid_site_target= str(res.stdout[abs_path_len:-1],'utf-8')
        else:
            self.file_link_is_broken=True

        



# Not naming this just file

class Doc_file:
    def __init__(self,p,n,is_md,is_index):
        self.path=p
        self.name=n
        self.is_markdown_file=is_md
        self.is_index_file=is_index
        self.links=[]

    def add_link(self, link):
        self.links.append(link)


