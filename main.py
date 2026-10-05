from fastmcp import FastMCP
import random
import json

mcp=FastMCP('Simple calculator server')

@mcp.tool
def add(a:int,b:int)->int:
    """Add two numers together.
    args-
    a: first  number
    b: second number
    
    return-
     Sum of a and b """
    return a+b

@mcp.tool
def random_number(min_value:int=1,max_value:int=10)->int:
    """Generate random number within the give range.
    args:
    min_value: the lower value (minimum value), default it is 1.
    max_value: the maximum value, default it is 10.

    returns-
    A random value between the given min_value and max_value
    """
    return random.randint(min_value,max_value)

@mcp.resource("info://server")
def server_info()->str:
    """get the info about this server."""
    info={
        "name":"simple calculator",
        "version":"1.0.0",
        "description":"A basic Mcp server with math tools",
        "tools":["add","random_number"],
        "author":"ABC-tester"
    }

    return json.dumps(info,indent=2)

if __name__ == "__main__":
    mcp.run(transport="http",host='0.0.0.0',port=8000)