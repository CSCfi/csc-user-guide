
import subprocess

def run_bash(command):
    command_as_list=command.split(" ")
    Output=subprocess.run(command_as_list,capture_output=True)
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

    def file_exist(self,name):
        return this.files.has_key(name)

    def report_broken_links(self):
        output=""
        for fileo in self.files.values():
            for link in fileo.links:
                if(link.file_link_is_broken):
                    output+="Link " +link.link_file_target+ " in file "+fileo.path+"/"+fileo.name +" on line " +link.line_number+ " is broken\n"


        if(output==""):
            print("No broken file links found")
        else:
            print(output[:-1])


class Internal_link:
    def __init__(self,f,ln,ft,st=""):
        self.source_file=f
        self.line_number=ln
        self.link_file_target=ft
        self.link_section_target=st
        # Default value is True
        self.valid_html_target=""
        self.valid_md_target=""
        self.file_link_is_broken=True
        
        # No file target, so the link must point to
        # a section in the same file (which must be .md)
        if(ft!=""):
            self.is_absolute= ft[0]=='/'         
            self.ends_with_md=ft[-3:]==".md"
            self.source_is_index=self.source_file.is_index_file
            self.target_is_index= ft[-8:]=="index.md"
            self.has_other_ending=("." in ft and not self.ends_with_md)
            source=""
            target=""

            source=self.source_file.path
            source="site/"+source[5:]

            if(not self.source_is_index):
                target="../"+target
                source=source+"/"+self.source_file.name
                source=source[:-3]+"/"
                
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
        else:
            self.file_link_is_broken=False
    def has_section_link():
        return self.lin_section != ""


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


if __name__ == "__main__":
    csc_docs=Docs()
    csc_docs.dump_data()
    csc_docs.parse_data()
    csc_docs.report_broken_links()
