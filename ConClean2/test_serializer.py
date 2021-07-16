import songs
import serializers
song = songs.Song('1', 'Water of Love', 'Dire Straits')
serializer = serializers.ObjectSerializers()

print(serializer.serialize(song, 'JSON'))
#'{"id": "1", "title": "Water of Love", "artist": "Dire Straits"}'

print(serializer.serialize(song, 'XML'))
#'<song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>'

#serializer.serialize(song, 'YAML')
""" Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./serializer_demo.py", line 30, in serialize
    raise ValueError(format)
ValueError: YAML """