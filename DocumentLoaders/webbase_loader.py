from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/Pant-Project-Relaxed-Stretchable-Stylish/dp/B0DGLTYVNC/ref=sr_1_3_sspa?crid=72B0BZTC1KDD&dib=eyJ2IjoiMSJ9.4nfp6TaDsPHz6v87qbwvd0YO3dIoTIK08QmW2EDSVKbG5SZNKjiLEUqWlffW19wIyDlhVY8Nz3vDcGlsr3pVR53ddg7YXwL0lQnTjHwjJmdwZlsTkN1xd1C0CaLS3Zvkq2Zpn10IjvGweqnYz633YraENdw1Exno9ujJ4PuYaABC1gtd0S_9JGc-6WtYlSsX1P-b-id8jI8096DQJGuj_QgKLcszDsTuHGAB1hccH0sEa4AwI6WiYBcnzU21OsFSaNzUO8KssFxu37wJipN0Cd5R6whp4UkLFQkWxiRlLEA.zIYnhO2ZNiA6l_JP3HU4mztaGSI00Rn4okipFnu0tNI&dib_tag=se&keywords=black%2Bjeans&qid=1784376863&sprefix=black%2Bjean%2Caps%2C279&sr=8-3-spons&aref=DMASVO2fEF&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1"

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(len(docs))