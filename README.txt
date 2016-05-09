FINAL PROJECT README FILE, last updated 05/09/16
---------------------------------------------------------------------------
GENERAL INFORMATION - running information
---------------------------------------------------------------------------
This program was written in Python 2.7.  The distribution that was used
to download python was Anaconda. It is assumed that all the packages
that would be installed with Anaconda are installed on the users computer
(numpy, json, etc)

Note: not all files in this github are intended to be run, some of them
were used for an intermediate step in the process, and will not 
compile as expected.  More information will be specified below on the different 
files
-----------------------------------------------------------------------------
FILE BREAK-DOWN
-----------------------------------------------------------------------------
\blosum_mat
	contains all the files needed to retrieve the Blosum matrices for alignment
	it also includes their probabilities (pre-normalization)

\collected_amino_acids_seq
	\Canis_Familiaris
	\Gorilla_gorilla
	\Loxodonta_africana
	\Mus_musculus
	\Oreochromis_niloticus
	\Ovis_aries
	collected_genes.txt
	All of the folders contain the collected genes from Ensembl,  each file name 
	is the actual Ensembl id.  collected_genes.txt contains a list of all the 
	collected gene ids from all the species.

\processsed_cluster_data_v2
	contains json files of all the data of the orthologous gene sets that
	have already been clustered and multiple sequence alignment has been performed
	The following is an example of what they look like
	{
	"0": "ENSCAFP00000002558",
	"1": "ENSGGOP00000028279",
	"2": "ENSLAFP00000003856",
	"3": "ENSMUSP00000037443",
	"4": "ENSONIP00000013531",
	"5": "ENSOARP00000013549",
	
	NOTE: \processed_cluster_data IS OLDER DATA which is not being used anymore

	
*Paths are all local and need to be changed in code accordingly
[done this way because of bug in computer python environment]


read_in_bosum.py
	this is the initial parser for the blosum matrices files.
	needs to be run befor rna_aligner
	
rna_aligner.py
	(*)first run read_in_bosum.py
	This file is used to read in the blosum_mat.  It automatically is set to return
	Blosum62, but could be easily changed.
	Needs to be run before most other scripts
	
	
NOTE: read_in_bosum and rna_aligner are helper classes.  There is 
no need to use them stand alone

dna_alignment_tool.py
	(*) first run read_in_bosum.py
	(*) then run rna_aligner.py
	Now this is the main class that does the alignment
	Below is an example of how to run the code
	
	d= DnaAligner()
	d.run('AB','CB')
		The command above will run the alignment on the two sequences
		that are input
		The results are returned in this format
		
	(merged DNA, score, alignment seq1, alignment seq2)
	So for the example above:
	('CB', 0.5, 'AB', 'CB')
	
cluster-information.txt
	each line represents a different cluster, and the genes are 
	tab delimited on the lines
	
	ex: species1|geneName 	species2|geneName2	....

run_pairwise.py
	(*) first run read_in_bosum.py
	(*) then run rna_aligner.py
	(*) then run dna_alignment_tool.py
	just run this script and it will start doing
	the multiple sequence alignment for
	clusters that have not been processed yet
	clustered_processed_v2.txt contains a list of 
	all the clusters that have already been processed
	that processed information is saved
	to the processed_cluster_data_v2 folders
	clustered_processed and processed_cluster_data are older 
	sets of data that are not used anymore

The methods above are the main methods used for the 
the alignment

The next will breakdown the methods used to develop the 
synthetic data
Since these methods are only used for testing they
might not run as expected

blosum62_qij_script.py
	use this script, and move the appropriate Blosum__.qij
	into the folder. change path as needed. This normalizes the blosum matrix
	so it is ready to use
	It also creates necessary lookup dictionaries for indexing

tree_gen.py
	(*) first run read_in_bosum.py
	(*) then run rna_aligner.py
	(*) run blosum62_qij_script.py
	this will generate synthetic trees which
	will be stored in the tree_synthetic_a.json
	
distance_normalizer.py
	used to produce the aggregated distance matrices for the phylogeny trees
	modified as needed
	
	
*The rest of the scripts are either used for evaluation,
immediate steps OR are not of use anymore



-----------------------------------------------------------------------------
SAMPLE INPUT AND OUTPUT FILES
-----------------------------------------------------------------------------

The following are locations of  genes which
are orthologous.  These amino acids sequences
can directly be used as input to the run method in 
dna_aligner (directions are provided above)

Below is the cluster line:
Ovis_aries|ENSOARP00000014520	Canis_familiaris|ENSCAFP00000038084	Loxodonta_africana|ENSLAFP00000028344	Oreochromis_niloticus|ENSONIP00000026101	Mus_musculus|ENSMUSP00000091053	Oreochromis_niloticus|ENSONIP00000025843	Oreochromis_niloticus|ENSONIP00000025777	Oreochromis_niloticus|ENSONIP00000025445	Oreochromis_niloticus|ENSONIP00000026103	Oreochromis_niloticus|ENSONIP00000026177	Oreochromis_niloticus|ENSONIP00000020119	Oreochromis_niloticus|ENSONIP00000004381	Oreochromis_niloticus|ENSONIP00000006903	Oreochromis_niloticus|ENSONIP00000008064	Oreochromis_niloticus|ENSONIP00000025055	Oreochromis_niloticus|ENSONIP00000000350	Oreochromis_niloticus|ENSONIP00000006949	Oreochromis_niloticus|ENSONIP00000007595	Oreochromis_niloticus|ENSONIP00000007733	Oreochromis_niloticus|ENSONIP00000026699	Oreochromis_niloticus|ENSONIP00000026698

(located in cluster-information.txt line 148)

the exact location of each file is as follows below:

collected_amino_acids_seq\Ovis_aries\ENSOARP00000014520.json
collected_amino_acids_seq\Canis_familiaris\ENSCAFP00000038084.json
collected_amino_acids_seq\Loxodonta_africana\ENSLAFP00000028344.json
collected_amino_acids_seq\Mus_musculus\ENSMUSP00000091053.json
collected_amino_acids_seq\Oreochromis_niloticus\ENSONIP00000026101.json

These are examples of input sequence files
You can run the pairwise alignment easily given the example above

The multiple sequence alignment is more complicated but here is an example of
the output for the given genes above

\processed_cluster_data_v2\_147.json

This file contains all the information necessary from the multiple sequence alignment

Additionally

tree_synthetic_a.json contains examples of different synthetic gene trees made by different blosum matrices





