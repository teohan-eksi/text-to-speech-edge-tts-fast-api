from .main import app

@app.get("/hw")
def getHW(): 
    return "Hello World"

"""import asyncio, edge_tts

async def main():
    tts = edge_tts.Communicate("Hello, this is my text.", voice="en-US-JennyNeural")
    await tts.save("output.mp3")

asyncio.run(main())"""
