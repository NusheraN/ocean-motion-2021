import sys

date = sys.argv[1]

file = open('file_vectorq', 'w')

#Vector
file.write("!/bin/csh")
file.write("\n")

file.write("\n")
file.write("set dhdir = /Users/brownscholar/Documents/Intern/Data/dynamic height/" + "\n")
file.write("set dendir = /Users/brownscholar/Documents/Intern/data/density/"+ "\n")
file.write("set auxdir = /Users/brownscholar/Documents/Intern/Data/aux/"+ "\n")
file.write("set outdir = /Users/brownscholar/Documents/Intern/Data/omega/"+ "\n")
file.write("set fileinfo = {$dir}info_pr.dat"+ "\n")
file.write("set filedh =  {$dhdir}/dynamic height_"+ date + ".gr"+ "\n")
file.write("set filest =  {$dendir}/density_" + date + ".gr"+ "\n")
file.write("set filestm = {$auxdir}/st0/_" + date + "_st0.dat"+ "\n")
file.write("set filequ =  {$outdir}/u/_" + date + "_qu.gr"+ "\n")
file.write("set fileqv =  {$outdir}/v/_" + date + "_qv.gr"+ "\n")
file.write("set fileqdi = {$auxdir}/qdi/_" + date + "_qdi.gr"+ "\n")

file.write("\n")
file.write("./vectorq.exe << !"+ "\n")
file.write("'$fileinfo'	#>>>>>Escribe info file info.dat:"+ "\n")
file.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:"+ "\n")
file.write("'$filest'	#>>>>>Escribe fichero de densidad:"+ "\n")
file.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:"+ "\n")
file.write("'$filequ'	#>>>>>Escribe fichero Qu:"+ "\n")
file.write("'$fileqv'	#>>>>>Escribe fichero Qv:"+ "\n")
file.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:"+ "\n")
