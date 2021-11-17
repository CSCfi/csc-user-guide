from docs import *

csc_docs=Docs()

result_file_link = csc_docs.report_broken_file_links()
result_section_link = csc_docs.report_broken_section_links()
result_hidden_file = csc_docs.report_hidden_files()
print(result_section_link[1])
print(result_file_link[1])
print(result_hidden_file[1])
sys.exit(max(result_file_link[0],result_hidden_file[0],result_section_link[0]))
