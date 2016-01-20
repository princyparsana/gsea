# gsea
Gene set enrichment analysis using Fisher's exact test

####Instructions to use this:
##### 1. add gsea to $PATH
`export PATH=$PATH:path_to_gsea/`
##### 2. run gsea
`gsea file_name background_file_name geneset_name save_name`

Here,

`file_name` is file with test genes (one gene per line)

`background_file_name` is file with background genes (one gene per line)

`geneset_name` is filepath+name of a geneset downloaded from msigdb. Need not parse msigdb file. Script takes care of parsing

`save_name` is filepath+name for output file
