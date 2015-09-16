__author__ = 'athanas'

#Bootcamp Expression Analysis Homework
"""
Data file: data_set_HL60_U937_NB4_Jurkat.txt

A. How many distinct genes are in the data file?
B. For each cell type, what are the most correlated time points? What is their correlation?
C. Across all cell types, which two are the most highly correlated?
D. Find the ten genes that are the most stable across the time points.
E. How many genes have at least a two-fold expression increase during the course of the experiment?
F. Find the genes that have at least a two-fold difference between cell types HL60 and U937 cells at 0 hours.
"""

Data_File = open("Inputs/data_set_bootcamp.txt")
Data = Data_File.readlines()
Data_File.close()

Data_Format = []

for i in Data:
    Data_Format.append(i.strip().split('\t'))


