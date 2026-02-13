from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("crypto")

@mcp.tool()
def get_crypto_currency_price(crypto: str) -> str:
    """
        Get the price of the cryptocurrency
        Args:
            crypto: symbol of cryptocurrency(e.g.,'bitcoin', 'ethereun')
    """
    try:
        api_url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {"ids":crypto.lower(), "vs_currencies":"usd"}
        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = data.get(crypto.lower(), {}).get("usd")
        return f"price of crypto {crypto} is ${price} USD" if price is not None else f"price for crypto {crypto} is not found,"
    except Exception as e:
        print(f"exception occurred {e}")

if __name__== '__main__':
    mcp.run()