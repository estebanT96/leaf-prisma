import ee
import geemap

# ee.Authenticate(force=True)

ee.Initialize(project='leaf-prisma')

Map = geemap.Map(center=[29.4201, -110.91778], zoom=16)

Map.to_html("hermosillo_test.html")

print("Success! Open hermosillo_test.html in your browser.")