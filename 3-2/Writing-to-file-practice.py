import sys

date = sys.argv[1]

file = open('file_vectorq.exec', 'w')

#Vector
file.write("!/bin/csh")

file.write("set dhdir = /Users/helenfellow/Documents/cnn_paper/data/atlantic-data/dh/" + "\n")
file.write("set dendir = /Users/helenfellow/Documents/cnn_paper/data/atlantic-data/density/"+ "\n")
file.write("set auxdir = /Users/helenfellow/Documents/cnn_paper/data/atlantic-data/aux/"+ "\n")
file.write("set outdir = /Users/helenfellow/Documents/cnn_paper/data/atlantic-data/omega/"+ "\n")
file.write("set fileinfo = {$dir}info_pr.dat"+ "\n")
file.write("set filedh =  {$dhdir}/nw_dh_"+ date + ".gr"+ "\n")
file.write("set filest =  {$dendir}/nw_density_" + date + ".gr"+ "\n")
file.write("set filestm = {$auxdir}/st0/nw_" + date + ".dat"+ "\n")
file.write("set filequ =  {$outdir}/u/nw_" + date + ".gr"+ "\n")
file.write("set fileqv =  {$outdir}/v/nw_" + date + ".gr"+ "\n")
file.write("set fileqdi = {$auxdir}/qdi/nw_" + date + "_qdi.gr"+ "\n")

file.write("./vectorq.exe << !"+ "\n")
file.write("'$fileinfo'	#>>>>>Escribe info file info.dat:"+ "\n")
file.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:"+ "\n")
file.write("'$filest'	#>>>>>Escribe fichero de densidad:"+ "\n")
file.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:"+ "\n")
file.write("'$filequ'	#>>>>>Escribe fichero Qu:"+ "\n")
file.write("'$fileqv'	#>>>>>Escribe fichero Qv:"+ "\n")
file.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:"+ "\n")

