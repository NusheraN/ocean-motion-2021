#Omegainv
import sys

date = sys.argv[1]

om_file = open('file_omegainv', 'w')

om_file.write("!/bin/csh")
om_file.write("\n")

om_file.write("\n")
om_file.write("set dir = ./test/"+ "\n")
om_file.write("set fileinfo = {$dir}info_pr.dat"+ "\n")
om_file.write("set outdir = /Users/brownscholar/Documents/Intern/Data/omega/"+ "\n")
om_file.write("set auxdir = /Users/brownscholar/Documents/Intern/Data/aux/"+ "\n")
om_file.write("set filestm = {$auxdir}/st0/_" + date + "_st0.dat"+ "\n")
om_file.write("set fileqdi = {$auxdir}/qdi/_"+ date + "_qdi.gr"+ "\n")
om_file.write("set filew =  {$outdir}w/_"+ date + "_ww.gr"+ "\n")

om_file.write("\n")
om_file.write("./omegainv.exe << !"+ "\n")
om_file.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:"+ "\n")
om_file.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:"+ "\n")
om_file.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:"+ "\n")
om_file.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):"+ "\n")
om_file.write("'$filew'	#>>>>>Escribe fichero Salida W:"+ "\n")


om_file.close()