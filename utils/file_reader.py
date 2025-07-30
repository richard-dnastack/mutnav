#!/usr/bin/env python


import pandas as pd
from pathlib import Path
from pygeneconverter import ensembl_to_hugo


# Base directory where our data lives
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def read_ssm_summary(filename: str) -> str:
    """
    Read a SSM file and return a simple summary.
    Args:
        filename: Name of the SSM file (e.g. 'ssm.tsv')
    Returns:
        A string describing the file's contents.
    """
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path, delimiter='\t')
    return f"SSM file '{filename}' has {len(df)} rows and {len(df.columns)} columns."

def read_ssm_column_names(filename: str) -> str:
    """
    Read a SSM file and return the column names.

    Args:
        * filename: Name of the file to process

    Returns:
        A string containing all the column names from the file.
    """
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path, delimiter='\t')
    return f"The column names in the SSM file are: {', '.join(df.columns)}"

def read_ssm_unique_ensembl_gene_names(filename: str) -> str:
    """
    Read a SSM file and return the total number of unique genes.

    Args:
        * filename: Name of the file to process

    Returns:
        A string containing the number of unique genes from the file.
    """
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path, delimiter='\t')
    return f"The unique Ensembl genes are:\n{df['gene_affected'].unique()}"

def read_ssm_unique_hugo_gene_names(filename: str) -> str:
    """
    Read a SSM file and return the total number of unique genes.

    Args:
        * filename: Name of the file to process

    Returns:
        A string containing the number of unique genes from the file.
    """
    file_path = DATA_DIR / filename
    #df = pd.read_csv(file_path, delimiter='\t')
    df = append_hugo_gene_name(filename)
    return f"The unique HUGO genes are:\n{df['HGNC_ID'].unique()}"

def append_hugo_gene_name(filename: str):
    """
    Import a SSM file as a dataframe and append the HUGO gene symbols to it.

    Args:
        * filenname: name of the file to process

    Returns:
        Returns a Pandas dataframe with HUGO gene symbol appended.
    """
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path, delimiter='\t')
    hugo_df = ensembl_to_hugo(df['gene_affected'].tolist())
    return df.merge(hugo_df, left_on='gene_affected', right_on='ENSEMBL_ID', how="left")

def return_recurrent_mutated_ensembl_genes(filename: str) -> str:
    """
    Import a SSM file as a Pandas dataframe and determine the top 5
    recurrent mutated gene.
        
    Args:
        * filename: Name of the file to process
        * gene_id:  Either "ensembl" or "hugo" (default: "ensembl")")

    Returns:
        Return the top 5 recurrently mutated gene as a string.
    """
    df_merged = append_hugo_gene_name(filename=filename)
    gene_type = 'gene_affected'
    counts = df_merged[gene_type].value_counts().reset_index()
    results = []
    for i in range(5):
        out_string = f'{counts.iloc[i][gene_type]} : {counts.iloc[i]["count"]}'
        results.append(out_string)
    return ', '.join(results)

def return_recurrent_mutated_hugo_genes(filename: str) -> str:
    """
    Import a SSM file as a Pandas dataframe and determine the top 5
    recurrent mutated hugo genes.
        
    Args:
        * filename: Name of the file to process

    Returns:
        Return the top 5 recurrently mutated gene as a string.
    """
    df_merged = append_hugo_gene_name(filename=filename)
    gene_type = 'HGNC_ID'
    counts = df_merged[gene_type].value_counts().reset_index()
    results = []
    for i in range(5):
        out_string = f'{counts.iloc[i][gene_type]} : {counts.iloc[i]["count"]}'
        results.append(out_string)
    return ', '.join(results)

def return_average_total_read_count(filename: str) -> str:
    """
    Return the average total read count.

    Args:
        * filename: Name of the file to process

    Returns:
        Return the average total read count for a mutation
    """
    df = append_hugo_gene_name(filename=filename)
    return f'The average total read count is: {str(round(df["total_read_count"].mean(), 2))}'
