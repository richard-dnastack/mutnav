# tools/tsv_tools.py

from server import mcp
from utils.file_reader import read_ssm_summary, read_ssm_column_names, read_ssm_unique_ensembl_gene_names, read_ssm_unique_hugo_gene_names, return_recurrent_mutated_hugo_genes, return_recurrent_mutated_ensembl_genes, return_average_total_read_count


@mcp.tool()
def summarize_ssm_file(filename: str) -> str:
    """
    Summarize a SSM file by reporting its number of rows and columns.
    Args:
        filename: Name of the SSM file in the /data directory (e.g., 'ssm.tsv')
    Returns:
        A string describing the file's dimensions.
    """
    return read_tsv_summary(filename)

@mcp.tool()
def get_ssm_column_names(filename: str):
    """
    Return the names of the column headers in the SSM file.
    """
    return read_ssm_column_names(filename)

@mcp.tool()
def get_unique_genes_in_ssm(filename: str):
    """
    Return all the unique gene Ensembl IDs from a SSM file.
    """
    return read_ssm_unique_gene_names(filename)

@mcp.tool()
def get_recurrent_mutated_hugo_genes(filename: str) -> str:
    """
    A MCP compatible function to return recurrent HUGO mutated
    genes.
    """
    return return_recurrent_mutated_hugo_genes(filename)

@mcp.tool()
def get_recurrent_mutated_ensembl_genes(filename: str) -> str:
    """
    A MCP compatible function to return recurrent Ensembl mutated
    genes.
    """
    return return_recurrent_mutated_ensembl_genes(filename)

@mcp.tool()
def get_average_total_read_count(filename: str) -> str:
    """
    A MCP compatible function to return the average total read count.
    """
    return return_average_total_read_count(filename)

