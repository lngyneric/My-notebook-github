import httpx
import asyncio
import sys

BASE_URL = "http://127.0.0.1:8000"

async def test_health():
    print(f"Testing Health Check ({BASE_URL}/)...")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/")
            if response.status_code == 200:
                print("✅ Health Check Passed:", response.json())
            else:
                print("❌ Health Check Failed:", response.status_code, response.text)
    except Exception as e:
        print(f"❌ Health Check Error: {e}")

async def test_wecom_login():
    print(f"\nTesting WeCom Login URL Generation ({BASE_URL}/auth/wecom/login)...")
    try:
        async with httpx.AsyncClient() as client:
            # Test without credentials (expecting 500 or success if mocked/configured)
            # Since credentials are mostly placeholders, we might get an error or a URL with placeholders.
            # But the code checks `if not WECOM_CORP_ID: raise HTTPException`
            # So if env is not set, it should fail.
            
            response = await client.get(f"{BASE_URL}/auth/wecom/login", params={"redirect_uri": "http://localhost:3000"})
            if response.status_code == 200:
                print("✅ WeCom Login URL Generated:", response.json())
            elif response.status_code == 500 and "not configured" in response.text:
                print("⚠️ WeCom Login Check: Server returned 500 as expected (Credentials not configured).")
                print("   This confirms the endpoint is reachable and logic is executing.")
            else:
                print("❌ WeCom Login Failed:", response.status_code, response.text)
    except Exception as e:
        print(f"❌ WeCom Login Error: {e}")

async def main():
    print("Starting Deployment Verification...")
    await test_health()
    await test_wecom_login()
    print("\nVerification Complete.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
