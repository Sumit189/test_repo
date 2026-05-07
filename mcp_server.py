from typing import List

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("calculator-server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@mcp.tool()
def matrix_multiply(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    """Multiply two matrices and return their product."""
    if not matrix_a or not matrix_b:
        raise ValueError("Both matrices must be non-empty.")

    if not all(isinstance(row, list) and row for row in matrix_a):
        raise ValueError("matrix_a must be a non-empty list of non-empty lists.")

    if not all(isinstance(row, list) and row for row in matrix_b):
        raise ValueError("matrix_b must be a non-empty list of non-empty lists.")

    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])

    if any(len(row) != columns_a for row in matrix_a):
        raise ValueError("All rows in matrix_a must have the same length.")

    if any(len(row) != columns_b for row in matrix_b):
        raise ValueError("All rows in matrix_b must have the same length.")

    rows_b = len(matrix_b)

    if columns_a != rows_b:
        raise ValueError(
            "Cannot multiply matrices: the number of columns in matrix_a "
            "must equal the number of rows in matrix_b."
        )

    return [
        [
            sum(matrix_a[row_index][k] * matrix_b[k][column_index] for k in range(columns_a))
            for column_index in range(columns_b)
        ]
        for row_index in range(len(matrix_a))
    ]


if __name__ == "__main__":
    print("Calculator MCP Server running...")
    mcp.run(transport="stdio")
